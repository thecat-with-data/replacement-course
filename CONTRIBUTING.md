# Contributing to Office Pro Replacement Course

Thank you for contributing! This document describes how to contribute content, fixes, and improvements.

## Branching and workflow

1. Fork the repository.
2. Create a topic branch:
   - `feature/word-module-3` for new module content.
   - `fix/module2-quiz` for bug fixes.
3. Make changes.
4. Commit with clear message.
5. Push and open a Pull Request.

## Content guidelines

- Keep HTML self-contained and avoid external runtime dependencies.
- Follow existing folder conventions:
  - `Microsoft Word/Module X - .../lessons/`
  - `Microsoft Word/Module X - .../labs/`
  - `Microsoft Word/Module X - .../quizzes/`
- Use consistent naming (e.g., `Lesson 1 - ... .html`, `W-Lab 3 - ... .html`).
- Confirm files render in a local browser:
  - `python -m http.server 8000`
  - open `http://localhost:8000`

## Review checklist

- [ ] Content is accurate and completes learning objectives.
- [ ] Pages are accessible (headings, alt text for images).
- [ ] Hyperlinks are valid.
- [ ] Module status updated in `README.md`.

## Testing in LMS

1. Upload updated folder to LMS.
2. Run through each lesson/lab/quiz.
3. Record issues and fix.

## Licensing

Contributions are covered by the repository `LICENSE` (MIT License).

## Questions

Reach out to the project maintainer for guidance on module scope and learning objective mapping.
