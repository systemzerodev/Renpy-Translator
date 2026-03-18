Contributing to RenPy Translator

First off, thank you for considering contributing! 🎉

We welcome contributions of all kinds:

- Bug reports
- Feature suggestions
- Code improvements
- Documentation updates

---

🛠 Getting Started

1. Fork this repository
2. Clone your fork:
   git clone https://github.com/systemzerodev/renpy-translator.git
3. Create a new branch:
   git checkout -b feature/your-feature-name

---

💻 Development Setup

1. Create virtual environment:
   python -m venv venv
2. Activate it:
   venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt

---

🧪 Running Tests

python tests/test_parser.py
python tests/test_scanner.py

---

🎯 Code Style

We use:

- "black" for formatting
- "ruff" for linting
- "isort" for imports

Before committing:

ruff check .
black .
isort .

---

📌 Commit Guidelines

Use clear commit messages:

feat: add dialogue editor
fix: resolve parser bug
chore: update dependencies

---

🚀 Pull Request Process

1. Push your branch
2. Open a Pull Request
3. Describe what you changed
4. Wait for review

---

💡 Notes

- Keep changes focused
- Avoid large unrelated commits
- Write clean and readable code

---

Thanks for contributing ❤️
