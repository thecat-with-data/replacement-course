import os
import re
from bs4 import BeautifulSoup

def sanitize_filename(name):
    return re.sub(r'[<>:"|?*\\]', '', name).replace('/', '-')

def parse_lesson_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')

    # Skip if already processed (has Lesson Sections h2)
    if soup.find('h2', string='Lesson Sections'):
        return

    # Extract lesson number from filename
    basename = os.path.basename(filepath)
    match = re.match(r'Lesson (\d+) - (.+)\.html', basename)
    if not match:
        print(f"Skipping {filepath}, doesn't match pattern")
        return
    lesson_num = int(match.group(1))
    lesson_title = match.group(2)

    # Find H1, HR, intro, then H2s
    h1 = soup.find('h1')
    hr = soup.find('hr')
    if not h1 or not hr:
        print(f"Skipping {filepath}, no H1 or HR")
        return

    # Intro content: from after HR to first H2
    intro_elements = []
    current = hr.next_sibling
    while current and current.name != 'h2':
        if current.name:  # skip text nodes
            intro_elements.append(current)
        current = current.next_sibling

    # Now collect sections
    sections = []
    h2s = soup.find_all('h2')
    for i, h2 in enumerate(h2s):
        section_title = h2.get_text().strip()
        content = []
        current = h2.next_sibling
        while current and (i+1 >= len(h2s) or current != h2s[i+1]):
            if current.name and current.name != 'hr':  # stop at HR for Quick Reference
                content.append(current)
            elif current.name == 'hr':
                break
            current = current.next_sibling
        sections.append((section_title, content))

    if not sections:
        return  # Skip files with no H2 sections (already split sub-files)

    # If there's content after last H2 and HR, it's Quick Reference
    last_h2 = h2s[-1] if h2s else None
    if last_h2:
        current = last_h2.next_sibling
        while current and current.name != 'hr':
            current = current.next_sibling
        if current and current.name == 'hr':
            qr_h1 = current.next_sibling
            if qr_h1 and qr_h1.name == 'h1' and 'Quick Reference' in qr_h1.get_text():
                qr_content = []
                current = qr_h1.next_sibling
                while current:
                    if current.name:
                        qr_content.append(current)
                    current = current.next_sibling
                sections.append(('Quick Reference', [qr_h1] + qr_content))

    return lesson_num, lesson_title, intro_elements, sections

def promote_headers(soup_fragment):
    # Promote H3 to H2, H4 to H3, etc.
    for tag in soup_fragment.find_all(['h3', 'h4', 'h5', 'h6']):
        tag.name = 'h' + str(int(tag.name[1]) - 1)

def create_overview(filepath, lesson_num, lesson_title, intro_elements, sections):
    soup = BeautifulSoup('', 'html.parser')
    # Header
    html = soup.new_tag('html')
    head = soup.new_tag('head')
    meta_utf = soup.new_tag('meta', charset='utf-8')
    meta_viewport = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'})
    title = soup.new_tag('title')
    title.string = f'Lesson {lesson_num}: {lesson_title}'
    link = soup.new_tag('link', rel='stylesheet', href='https://s.brightspace.com/lib/fonts/0.6.1/fonts.css')
    head.append(meta_utf)
    head.append(meta_viewport)
    head.append(title)
    head.append(link)
    html.append(head)

    body = soup.new_tag('body', style="color: rgb(32, 33, 34); font-family: &quot;Lato&quot;, sans-serif; font-size: 19px;")
    p_img = soup.new_tag('p')
    img = soup.new_tag('img', src='../../../img/banner.png', alt=f'Module X: {lesson_title} Banner', **{'class': 'courseware-helper-bg-img'})
    p_img.append(img)
    body.append(p_img)

    h1 = soup.new_tag('h1')
    h1.string = f'Lesson {lesson_num}: {lesson_title}'
    body.append(h1)

    hr = soup.new_tag('hr')
    body.append(hr)

    # Intro
    for elem in intro_elements:
        body.append(elem)

    # Sections list
    h2_sections = soup.new_tag('h2')
    h2_sections.string = 'Lesson Sections'
    body.append(h2_sections)

    ul = soup.new_tag('ul')
    for i, (sec_title, _) in enumerate(sections, 1):
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=f'Lesson {lesson_num} Part {i} - {sec_title}.html')
        a.string = sec_title
        li.append(a)
        ul.append(li)
    body.append(ul)

    html.append(body)
    soup.append(html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def create_sub_file(dirpath, lesson_num, part_num, sec_title, content_elements):
    sanitized_title = sanitize_filename(sec_title)
    filepath = os.path.join(dirpath, f'Lesson {lesson_num} Part {part_num} - {sanitized_title}.html')
    print(f"Creating {filepath}")
    soup = BeautifulSoup('', 'html.parser')
    # Header
    html = soup.new_tag('html')
    head = soup.new_tag('head')
    meta_utf = soup.new_tag('meta', charset='utf-8')
    meta_viewport = soup.new_tag('meta', attrs={'name': 'viewport', 'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'})
    title = soup.new_tag('title')
    title.string = f'Lesson {lesson_num} Part {part_num} - {sec_title}'
    link = soup.new_tag('link', rel='stylesheet', href='https://s.brightspace.com/lib/fonts/0.6.1/fonts.css')
    head.append(meta_utf)
    head.append(meta_viewport)
    head.append(title)
    head.append(link)
    html.append(head)

    body = soup.new_tag('body', style="color: rgb(32, 33, 34); font-family: &quot;Lato&quot;, sans-serif; font-size: 19px;")
    p_img = soup.new_tag('p')
    img = soup.new_tag('img', src='../../../img/banner.png', alt=f'Module X: Lesson {lesson_num} Banner', **{'class': 'courseware-helper-bg-img'})
    p_img.append(img)
    body.append(p_img)

    h1 = soup.new_tag('h1')
    h1.string = f'Lesson {lesson_num} Part {part_num} - {sec_title}'
    body.append(h1)

    hr = soup.new_tag('hr')
    body.append(hr)

    # Content
    for elem in content_elements:
        promote_headers(elem)
        body.append(elem)

    html.append(body)
    soup.append(html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def process_lesson(filepath):
    result = parse_lesson_file(filepath)
    if not result:
        return
    lesson_num, lesson_title, intro_elements, sections = result

    dirpath = os.path.dirname(filepath)

    # Create overview
    create_overview(filepath, lesson_num, lesson_title, intro_elements, sections)

    # Create sub-files
    for i, (sec_title, content) in enumerate(sections, 1):
        create_sub_file(dirpath, lesson_num, i, sec_title, content)

def main():
    import glob
    root = os.getcwd()
    # Find all lesson files in Microsoft Word modules, exclude already processed
    pattern = 'Microsoft Word/Module */lessons/Lesson *.html'
    files = [os.path.join(root, f) for f in glob.glob(pattern)]
    for f in files:
        if 'Part' in f:  # Skip already processed
            continue
        print(f"Processing {f}")
        process_lesson(f)

if __name__ == '__main__':
    main()