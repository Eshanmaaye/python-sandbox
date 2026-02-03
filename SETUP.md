# 🚀 Quick Setup Guide

Welcome! Get started with Python Sandbox in 5 minutes.

## ⚡ Prerequisites

- ✅ Python 3.7 or higher ([Download Python](https://www.python.org/downloads/))
- ✅ pip (comes with Python)
- ✅ Git ([Download Git](https://git-scm.com/downloads))
- ✅ Microphone (for voice projects)

Check your Python installation:
```bash
python --version
# Should show: Python 3.7.x or higher
```

---

## 📥 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Eshanmaaye/python-sandbox.git
cd python-sandbox
```

### Step 2: Set Up Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

For **Sunday Voice Command Assistant**:
```bash
cd sunday-vca
pip install -r requirements.txt
```

---

## 🎮 Running Your First Project

### Sunday VCA (Voice Assistant)

```bash
cd sunday-vca
python Sunday_VCA_v3.py
```

**First time? Say:**
- "What is the time?"
- "Tell me a joke"
- "Search Wikipedia for Python programming"
- "Commands" (to see all available commands)

**Stop the assistant:**
- Say "sleep", "exit", or "goodbye"

---

## 🐛 Troubleshooting

### PyAudio Installation Issues

**Windows:**
```bash
# Download from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Choose the file matching your Python version
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

### Microphone Not Working

1. Check microphone is connected
2. Grant microphone permissions to Terminal/Command Prompt
3. Test with: `python -m speech_recognition`

### Import Errors

```bash
# Make sure you're in the virtual environment
# Reinstall requirements
pip install -r requirements.txt --upgrade
```

---

## 📁 Project Structure

```
python-sandbox/
├── sunday-vca/              # Voice Command Assistant
│   ├── Sunday_VCA_v3.py     ← Main file
│   ├── requirements.txt     ← Dependencies
│   └── CHANGELOG.md
├── basics/                  # Beginner scripts
├── experiments/             # Learning experiments
├── README.md
└── CONTRIBUTING.md
```

---

## 🎯 What to Try Next

### Beginner Projects
1. `basics/hello_world.py` - Start here
2. `basics/calculator.py` - Simple calculator
3. `basics/guess_number.py` - Number guessing game

### Intermediate Projects
1. Sunday VCA - Voice automation (you're here!)
2. File organizer - Coming soon
3. Web scraper - Coming soon

---

## 💡 Learning Tips

1. **Read the code** - Every file has detailed comments
2. **Break things** - It's the best way to learn!
3. **Check the changelog** - See how projects evolved
4. **Ask questions** - Open an issue if stuck

---

## 🆘 Need Help?

- 📖 [Read the full README](README.md)
- 🐛 [Report a bug](https://github.com/Eshanmaaye/python-sandbox/issues)
- 💬 [Ask a question](https://github.com/Eshanmaaye/python-sandbox/discussions)
- 📧 Email: [your.email@example.com]

---

## 🎉 You're All Set!

```python
print("Happy coding! 🐍")
```

Start with the Sunday VCA project, explore the basics folder, and most importantly - **have fun learning!**

Remember: Every expert was once a beginner. Keep coding! 🚀
