# 🚀 AI Project Builder

AI Project Builder is a Python 3.14 application that uses Google's Gemini API to generate complete software projects from natural language descriptions.

Instead of manually creating folder structures, boilerplate code, setup files, and documentation, simply describe your project idea and let AI generate a working starter project.

---

## ✨ Features

### 🏗 Project Generation

Generate complete software projects from a simple prompt.

Example:

> Create a FastAPI todo application with authentication and SQLite database.

The AI automatically generates:

* Folder structure
* Source code
* requirements.txt
* README.md
* Installation scripts
* Configuration files

---

### 💡 Idea Generator

Generate unique project ideas for:

* AI Applications
* Machine Learning
* Automation
* Cybersecurity
* Developer Tools
* Startups
* Data Science
* Web Development

Perfect for portfolio projects and hackathons.

---

### 📦 ZIP Export

Projects are automatically packaged into a downloadable ZIP archive.

---

### 🎨 Gradio Interface

Modern browser-based UI built with Gradio.

No command-line knowledge required.

---

### 🐍 Python 3.14 Ready

All generated code is designed specifically for:

* Python 3.14
* Modern libraries
* Current best practices

---

## 🧠 Planned AI Agent System

Future versions will include a multi-agent workflow:

Idea Generator
↓
Architect Agent
↓
Builder Agent
↓
Reviewer Agent
↓
Fixer Agent
↓
Tester Agent
↓
Documentation Agent
↓
ZIP Export

### Architect Agent

Designs project structure and file layout.

### Builder Agent

Writes source code.

### Reviewer Agent

Finds bugs, security issues, and bad practices.

### Fixer Agent

Automatically corrects detected problems.

### Tester Agent

Creates automated tests.

### Documentation Agent

Generates README files and setup guides.

---

## 📂 Project Structure

```text
AIProjectBuilder/
│
├── main.py
├── generator.py
├── project_builder.py
├── zip_exporter.py
├── requirements.txt
├── .env.example
│
├── generated/
│
└── ui/
    ├── __init__.py
    └── gradio_ui.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AIProjectBuilder.git
cd AIProjectBuilder
```

### Create Virtual Environment

```bash
py -3.14 -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
py -3.14 -m pip install --upgrade pip
py -3.14 -m pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get an API key from Google AI Studio.

---

## ▶️ Run

```bash
py -3.14 main.py
```

The Gradio interface will open in your browser.

---

## 📝 Example Prompt

```text
Create a FastAPI blog application with:

- User authentication
- SQLite database
- CRUD operations
- requirements.txt
- README.md
- Docker support
```

---

## 🛠 Tech Stack

* Python 3.14
* Gradio
* Google Gemini API
* python-dotenv

---

## 🎯 Roadmap

* [ ] Architect Agent
* [ ] Reviewer Agent
* [ ] Fixer Agent
* [ ] Tester Agent
* [ ] Documentation Agent
* [ ] Project Templates
* [ ] Docker Generation
* [ ] GitHub Repository Creation
* [ ] CI/CD Workflow Generation
* [ ] Hugging Face Space Deployment

---

## 🤝 Contributing

Pull requests, ideas, and feedback are welcome.

If you discover a bug or have a feature request, open an issue.

---

## 📜 License

MIT License

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub.
It helps the project grow and motivates future development.
