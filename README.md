# Office Pro Replacement Course

A lightweight, LMS-agnostic courseware repository for Microsoft Office training.

Designed for HTML-based LMS platforms (D2L, Canvas, Blackboard, etc.) with simple file-folder deployment.

---

## 📦 Repository structure

- `Microsoft Word/`
  - `Module 1 - Word Foundations/`
    - `Module 1 - Overview.html`
    - `lessons/`, `labs/`, `quizzes/`
  - `Module 2 - Word Structure/`
  - `Module 3 - Word Graphics & Collaboration/`
- `Microsoft Excel/`
  - `Module 1 - Excel Foundations/`
- `templates/`
  - `GeneralKnowledge.csv`
  - `D2L/…`
  - `HTML Template Library/…`
- `introduction/`
  - instructor notes and course intro pages
- `README.md`
- `CONTRIBUTING.md`
- `LICENSE`

---

## 🎯 Goals

1. Replace TestOut Office Pro for Microsoft Office curriculum tracks.
2. Be compatible with any LMS accepting static HTML pages.
3. Keep the course modular for easy maintenance, review, and extension.

---

## 📌 Status overview

### Module 1 – Word Foundations
- Lessons: complete
- Labs: complete
- Quizzes: complete

### Module 2 – Word Structure
- Lessons: complete
- Labs: complete
- Quizzes: mostly complete

### Module 3 – Word Graphics & Collaboration
- Lessons: complete
- Labs: in progress
- Quizzes: pending

### Excel Module(s)
- Module 1 scaffold: in place
- Content: in progress

---

## 🚀 Quick start (LMS deployment)

1. Clone this repo.
2. Upload or import HTML folders into LMS course sections.
3. Link `introduction/` pages to course landing content.
4. Validate:
   - heading/navigation
   - images and media
   - links and quizzes
5. Run pilot learner walkthrough and note any required platform-specific file path updates.

---

## 🛠️ Contribution workflow

1. Fork and clone repository.
2. Create a feature branch (`feature/<module>-<update>`).
3. Edit or add HTML in `Microsoft Word` / `Microsoft Excel`.
4. Update module progress metadata in this README (or a status file).
5. Push and submit pull request.
6. Reviewer validates in target LMS and signs off.

---

## 🗺️ Roadmap (recommended)

- [ ] Finish Module 3 labs + quizzes
- [ ] Complete Excel Module 1 lessons/labs/quizzes
- [ ] Add Module 4 (if needed)
- [ ] Add accessibility checks (WCAG 2.1)
- [ ] Add versioning + changelog (`CHANGELOG.md`)

---

## 💡 Optional improvements

- Add landing page for instructors (syllabus + learning objectives)
- Add direct mapping table: objective → lesson → quiz → lab
- Add `draft` vs `published` tag metadata in page headers
- Enable dynamic index via script (optional)

