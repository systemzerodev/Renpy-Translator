# RenPy Translator

RenPy Translator is a tool designed to simplify the translation workflow for **Ren'Py visual novel games**.

The tool scans Ren'Py script files (`.rpy`), extracts dialogue text, and prepares it for translation and patch generation.

This project aims to provide a simple and efficient way to create translation patches for Ren'Py games.

---

# Features

Current and planned features:

- Scan Ren'Py game directories
- Detect `.rpy` script files
- Extract dialogue text from scripts
- Store dialogue data for translation
- Translation editor interface _(planned)_
- Translation patch generator _(planned)_
- Auto translation support _(future)_

---

# Project Structure

```
renpy-translator
│
├─ core/                 # Core engine
│   ├─ parser.py         # Extract dialogue from scripts
│   ├─ scanner.py        # Locate .rpy files
│   └─ models.py         # Dialogue data structures
│
├─ ui/                   # User interface
│   └─ app.py
│
├─ tests/                # Unit tests
│   └─ test_parser.py
│
├─ docs/                 # Technical documentation
│   ├─ architecture.md
│   └─ parser_design.md
│
├─ assets/               # Static resources (icons, images)
│
├─ .pre-commit-config.yaml
├─ .gitignore
├─ requirements.txt
├─ LICENSE
└─ README.md
```

---

# Architecture Overview

The system is designed as a modular pipeline:

```
Ren'Py Game
     │
     ▼
Scanner
(find .rpy files)
     │
     ▼
Parser
(extract dialogue)
     │
     ▼
Dialogue Models
(store translation data)
     │
     ▼
UI Editor
(translation interface)
     │
     ▼
Patch Generator
(create translation patch)
```

The goal is to keep **core logic independent from the user interface**, making the project easier to maintain and extend.

---

# Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/renpy-translator.git
```

Navigate into the project directory:

```
cd renpy-translator
```

Create a virtual environment:

```
python -m venv venv
```

Activate the virtual environment:

Windows:

```
venv\Scripts\activate
```

Linux / macOS:

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Development Setup

This project uses **pre-commit hooks** to enforce consistent code formatting.

Install hooks:

```
pre-commit install
```

Run checks manually:

```
pre-commit run --all-files
```

Tools used:

- **Black** → code formatter
- **Ruff** → linter
- **isort** → import sorting

---

# Usage

Run the application entry point:

```
python ui/app.py
```

Example output:

```
RenPy Translator UI starting...
```

Currently this is a placeholder while the core engine is under development.

---

# Roadmap

Planned development stages:

### Phase 1 — Core Engine

- Implement `.rpy` file scanner
- Build dialogue parser
- Design translation data model

### Phase 2 — Translation Workflow

- Dialogue extraction
- Translation data storage
- Patch generator

### Phase 3 — User Interface

- Translation editor UI
- File management tools

### Phase 4 — Advanced Features

- Auto translation support
- Translation memory
- Better script parsing

---

# Contributing

Contributions are welcome.

Steps:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

Issues and feature requests are also appreciated.

---

# License

This project is licensed under the **MIT License**.
