<div align="center">

# 🐍 Python Sandbox

### *My Journey from Python Beginner to Builder*

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Learning-success?style=for-the-badge)](https://github.com/Eshanmaaye/python-sandbox)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge)](CONTRIBUTING.md)

*Learning Python one project at a time | From basics to automation | Built with curiosity 🚀*

[View Projects](#-featured-projects) • [Getting Started](#-getting-started) • [Roadmap](#-learning-roadmap) • [Connect](#-lets-connect)

</div>

---

## 👋 Welcome!

Hey there! I'm **Eshan**, and this is my **Python Sandbox** - a collection of projects, experiments, and learning milestones as I explore the world of Python programming. 

This isn't just a code dump - it's a **documented journey** from writing my first "Hello World" to building functional automation tools. Whether you're a fellow learner or an experienced developer, feel free to explore, learn, or even contribute!

### 🎯 What Makes This Repo Special?

- ✨ **Real Projects, Not Just Tutorials** - Working code that solves actual problems
- 📝 **Beginner-Friendly** - Detailed comments and explanations
- 🔄 **Iterative Learning** - Watch projects evolve from v1 to v2 to v3
- 🐛 **Mistakes Included** - Learn from my bugs and fixes
- 💬 **Open Collaboration** - Feedback and suggestions welcome!

---

## 🚀 Featured Projects

### 🎙️ Sunday Voice Command Assistant (VCA)

> A voice-activated automation system that brings hands-free control to your computer

**What it does:**
- 🗣️ Responds to voice commands in natural language
- 🔍 Searches Wikipedia and Google
- 🎵 Plays YouTube videos and local media
- 😂 Tells jokes when you need a laugh
- ⏰ Sets alarms with custom music
- 🧮 Performs voice-activated calculations
- 📱 Opens applications (Notepad, Calculator, etc.)
- 🆘 Provides emergency contact information

**Tech Stack:**
```python
pyttsx3          # Text-to-speech
SpeechRecognition # Voice input
pywhatkit        # YouTube automation
wikipedia        # Information retrieval
pyjokes          # Random jokes
```

**Quick Start:**
```bash
cd sunday-vca
pip install -r requirements.txt
python Sunday_VCA_v3.py
```

**Evolution:**
- `v1.0` - Basic voice recognition with hardcoded responses
- `v2.0` - Added Wikipedia, YouTube, and Google search
- `v3.0` - Bug fixes, better error handling, new features ✨

> 💡 **Learning Note:** This is *not* AI/Machine Learning - it's rule-based automation using speech recognition. A great way to understand the difference!

[📂 View Project](./sunday-vca) | [📖 Read Changelog](./sunday-vca/CHANGELOG.md)

---

### 📁 Other Projects

| Project | Description | Status | Key Learning |
|---------|-------------|--------|--------------|
| 🎮 **Mini Games** | Simple text-based games | 🔄 In Progress | Loops, conditionals, user input |
| 📊 **Data Scripts** | CSV/Excel automation | 📋 Planned | File handling, pandas |
| 🌐 **Web Scraper** | Extract data from websites | 📋 Planned | BeautifulSoup, requests |
| 🖼️ **Image Tools** | Batch image processing | 💡 Idea | PIL/Pillow library |

---

## 📚 Learning Roadmap

### ✅ Completed

- [x] Python basics (variables, data types, operators)
- [x] Control flow (if/else, loops)
- [x] Functions and modules
- [x] File operations (read/write)
- [x] Exception handling
- [x] Working with external libraries (pip)
- [x] Speech recognition integration
- [x] Text-to-speech systems

### 🔄 Currently Learning

- [ ] Object-Oriented Programming (OOP)
- [ ] Data structures (lists, dictionaries, sets)
- [ ] Regular expressions (regex)
- [ ] Working with APIs
- [ ] Database basics (SQLite)

### 📋 Next Up

- [ ] Web scraping with BeautifulSoup
- [ ] GUI development with Tkinter
- [ ] Data analysis with Pandas
- [ ] Web development with Flask
- [ ] Building REST APIs
- [ ] Automation with Selenium

---

## 🛠️ Tech Stack & Tools

<div align="center">

### Languages & Libraries
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Tools & Platforms
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

</div>

---

## 🚦 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Microphone (for voice projects)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Eshanmaaye/python-sandbox.git
   cd python-sandbox
   ```

2. **Install project dependencies**
   ```bash
   # For Sunday VCA
   cd sunday-vca
   pip install -r requirements.txt
   ```

3. **Run a project**
   ```bash
   python Sunday_VCA_v3.py
   ```

### Project Structure

```
python-sandbox/
├── sunday-vca/              # Voice Command Assistant
│   ├── Sunday_VCA_v3.py
│   ├── requirements.txt
│   └── CHANGELOG.md
├── basics/                  # Fundamental Python scripts
│   ├── hello_world.py
│   ├── calculator.py
│   └── ...
├── experiments/             # Testing new concepts
│   └── ...
└── README.md               # You are here!
```

---

## 💡 Philosophy & Approach

### Learning by Doing

I believe the best way to learn programming is to **build things**. Each project here represents:

1. 🎯 **A problem I wanted to solve** - Real use cases, not just exercises
2. 🔨 **Hands-on implementation** - Writing code, making mistakes
3. 🐛 **Debugging and refining** - Learning from errors
4. 📖 **Documentation** - Explaining what I learned
5. 🔄 **Iteration** - Making it better over time

### Code Quality Journey

As a learner, my code isn't perfect - and that's okay! You'll see:

- ✅ **Version 1:** Gets it working (even if messy)
- ✅ **Version 2:** Makes it better (cleaner, more features)
- ✅ **Version 3:** Makes it right (proper error handling, best practices)

This progression is intentional - it shows the **real learning process**.

---

## 🤝 Contributing

I'm learning, and I'd love your help! Here's how you can contribute:

### 🐛 Found a Bug?
- Open an issue describing the problem
- Include steps to reproduce
- Suggest a fix if you can!

### 💡 Have a Suggestion?
- Share ideas for new features
- Recommend better approaches
- Suggest learning resources

### 🔧 Want to Improve Code?
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Add comments explaining what and why
5. Submit a pull request

### 📚 Teaching Moment?
If you're an experienced developer and spot something I could do better, **please let me know!** I'm here to learn.

---

## 🌟 Inspiration & Resources

### Learning Resources I'm Using

- 📺 [Python Tutorial by Corey Schafer](https://www.youtube.com/c/Coreyms)
- 📖 [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- 🎓 [Real Python Tutorials](https://realpython.com/)
- 💻 [Python Official Documentation](https://docs.python.org/3/)
- 🏆 [LeetCode](https://leetcode.com/) - For problem-solving practice

### Projects That Inspired Me

- Voice assistants like Alexa and Google Assistant
- Desktop automation tools
- Developer productivity scripts

---

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/Eshanmaaye/python-sandbox?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/Eshanmaaye/python-sandbox?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/Eshanmaaye/python-sandbox?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/Eshanmaaye/python-sandbox?style=social)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR:** Feel free to use this code for learning, modify it, and share it. Just don't claim you wrote it from scratch!

---

## 💬 Let's Connect!

I'm always excited to connect with fellow learners and developers!

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Eshanmaaye-181717?style=for-the-badge&logo=github)](https://github.com/Eshanmaaye)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)

**Got questions? Ideas? Just want to chat about Python?**

Open an issue, start a discussion, or reach out directly!

</div>

---

## 🎓 My Learning Journey in Numbers

```python
{
    "journey_started": "2024",
    "projects_completed": 3,
    "bugs_fixed": "Too many to count 😅",
    "lines_of_code": "Growing daily",
    "cups_of_coffee": "∞",
    "stackoverflow_visits": "Countless",
    "aha_moments": "Every single day",
    "passion_level": "100%"
}
```

---

## 🙏 Acknowledgments

- Thanks to the **Python community** for amazing documentation and tutorials
- Shoutout to **Stack Overflow** for saving me countless times
- Appreciation for all the **open-source libraries** that make Python awesome
- Gratitude to **everyone who's starred, forked, or contributed** to this repo!

---

<div align="center">

### ⭐ If you found this helpful, give it a star!

**"Every expert was once a beginner. Keep coding, keep learning!"** 🚀

Made with ❤️ and lots of ☕ by [Eshan](https://github.com/Eshanmaaye)

---

*Last Updated: February 2026*

</div>
