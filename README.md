# 🐍 Python Sandbox

<div align="center">

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Voice Assistant](https://img.shields.io/badge/AI-Voice%20Assistant-orange.svg)

**A collection of Python projects showcasing voice AI, games, and data structures**

[Projects](#-projects) • [Getting Started](#-getting-started) • [Features](#-features) • [Contributing](#-contributing)

</div>

---

## 📖 About

Python Sandbox is a curated collection of practical Python applications demonstrating various programming concepts, from AI-powered voice assistants to interactive games and fundamental data structures. This repository serves as both a learning resource and a showcase of Python's versatility.

## ✨ Features

- 🎤 **Sunday VCA** - Advanced voice command assistant with speech recognition
- 🎮 **Interactive Games** - Classic Hangman game with ASCII art
- 📚 **Data Structures** - Clean implementation of Stack operations
- 🔧 **Well-Documented Code** - Clear comments and structured programming
- 🚀 **Ready to Run** - Minimal setup required to get started

## 🎯 Projects

### 1. 🎙️ Sunday Voice Command Assistant (VCA)

An intelligent voice-controlled assistant that can perform various tasks through speech commands.

**Key Features:**
- 🗣️ Natural speech recognition and text-to-speech
- 🔍 Wikipedia search integration
- 🌐 Google and YouTube search
- ⏰ Alarm system with custom music
- 🎬 Media file playback
- 🧮 Voice-activated calculator
- 😄 Joke telling capability
- 🚨 Emergency contact information
- 💻 System control (open apps, get system info)

**Available Commands:**
- `wikipedia [topic]` - Search Wikipedia
- `play video` - Play videos from your library
- `what is the time/date` - Get current time/date
- `alarm` - Set an alarm
- `google [search]` - Search Google
- `youtube [search]` - Play YouTube videos
- `joke` - Hear a random joke
- `calculation` - Perform calculations
- `open notepad/calculator` - Open applications
- `help` - Emergency contact numbers
- `exit/sleep/quit` - Stop the assistant

### 2. 🎮 Hangman Game

A classic word-guessing game with multiple categories and ASCII art visualization.

**Game Features:**
- 🎲 Three categories: Fruits, Animals, and Things
- 🎨 ASCII art hangman visualization
- ✅ Input validation and duplicate detection
- 🏆 Win/lose conditions with visual feedback
- 📊 Progressive difficulty with life system

**How to Play:**
1. Choose a category (Fruits, Animals, or Things)
2. Guess letters one at a time
3. Try to complete the word before running out of lives
4. You have 5 incorrect guesses before game over!

### 3. 📚 Stack Implementation

A clean and educational implementation of the Stack data structure with all fundamental operations.

**Features:**
- ➕ **Push** - Add elements to the stack
- ➖ **Pop** - Remove and return top element
- 👁️ **Peek** - View top element without removing
- 📋 **Display** - Visualize entire stack
- ✔️ **isEmpty** - Check if stack is empty
- 🛡️ **Underflow Protection** - Error handling for empty stack operations

**Operations Menu:**
```
1. Push    - Add item to stack
2. Pop     - Remove top item
3. Peek    - View top item
4. Display - Show all items
5. Exit    - Close program
```

## 🚀 Getting Started

### Prerequisites

Before running these projects, ensure you have Python 3.8+ installed and the required dependencies.

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Eshanmaaye/python-sandbox.git
cd python-sandbox
```

2. **Install dependencies**

For the Voice Assistant:
```bash
pip install pyttsx3 SpeechRecognition wikipedia-api pyjokes google pywhatkit pyaudio
```

For the other projects (no additional dependencies required):
```bash
# Games.py and Stack.py use only Python standard library
python Games.py
python Stack.py
```

### Quick Start

#### Running Sunday VCA:
```bash
python Sunday_VCA.py
```

Make sure your microphone is connected and working!

#### Playing Hangman:
```bash
python Games.py
```

#### Using Stack Implementation:
```bash
python Stack.py
```

## 💻 Usage Examples

### Sunday VCA Example Session

```python
# The assistant greets you based on time of day
"Good morning boss, I am Sunday. How are you boss?"

# You can ask questions
User: "What is the time?"
Sunday: "The time is 10:30 AM"

# Search Wikipedia
User: "Wikipedia Python programming"
Sunday: "According to Wikipedia, Python is..."

# Set an alarm
User: "Set an alarm"
Sunday: "Setting an alarm. Please enter the time below"
# Enter hour and minutes when prompted
```

### Hangman Game Flow

```
H A N G M A N

Topics:
1. FRUITS
2. ANIMALS
3. THINGS

Enter a choice: 1

The length of your word is:  _ _ _ _ _

Guess a letter: A
CORRECT CHOICE!!!
A _ _ _ _
```

### Stack Operations Example

```python
STACK OPERATIONS
1. Push
2. Pop
3. Peek
4. Display stack
5. Exit

Enter your choice: 1
Enter item: 42
# Item pushed successfully

Enter your choice: 4
42 <--- top
```

## 🛠️ Technical Details

### Sunday_VCA.py
- **Libraries Used:** pyttsx3, speech_recognition, wikipedia, webbrowser, pyjokes, pywhatkit
- **Features:** Speech-to-text, text-to-speech, web automation, alarm system
- **Version:** 3.0 (with bug fixes and new features)

### Games.py
- **Type:** Interactive command-line game
- **Difficulty:** Beginner-friendly
- **Categories:** 3 (each with 5 words)

### Stack.py
- **Implementation:** List-based stack
- **Operations:** Push, Pop, Peek, Display, isEmpty
- **Error Handling:** Underflow detection

## 📁 Project Structure

```
python-sandbox/
│
├── Sunday_VCA.py          # Voice Command Assistant
├── Games.py               # Hangman Game
├── Stack.py               # Stack Data Structure
├── README.md              # This file
└── requirements.txt       # Project dependencies (if created)
```

## 🔧 Configuration

### Sunday VCA Customization

You can customize the voice assistant by modifying these settings in `Sunday_VCA.py`:

```python
# Change voice (0 for male, 1 for female on most systems)
engine.setProperty('voice', voices[0].id)

# Adjust speech rate (default: 180)
engine.setProperty('rate', 180)

# Set your video directory
videodir = "C:\\Eshan\\Movies"

# Set your music directory for alarms
Musicdir = "C:\\Eshan\\New"
```

### Adding New Words to Hangman

Edit the word lists in `Games.py`:

```python
L1 = ['APPLE','BANANA','ORANGE','GRAPE','MANGO']  # Fruits
L2 = ['LION','TIGER','ELEPHANT','DEER','BEAR']    # Animals
L3 = ['MOBILE','COMPUTER','TABLE','BAG','MAT']    # Things
```

## 🎓 Learning Outcomes

By exploring this repository, you'll learn:

- **Voice AI Integration** - How to build voice-controlled applications
- **Speech Recognition** - Converting speech to text using Google's API
- **Text-to-Speech** - Using pyttsx3 for audio output
- **Web Automation** - Opening URLs and controlling web browsers
- **Data Structures** - Implementing stack with proper error handling
- **Game Development** - Creating interactive command-line games
- **Error Handling** - Managing exceptions and edge cases
- **User Input Validation** - Ensuring robust user interactions

## 🐛 Troubleshooting

### Sunday VCA Issues

**Microphone not working:**
- Check microphone permissions
- Ensure PyAudio is properly installed
- Try adjusting `r.pause_threshold` in the code

**Speech not recognized:**
- Speak clearly and at moderate pace
- Check internet connection (Google Speech API requires it)
- Reduce background noise

**Import errors:**
```bash
pip install --upgrade pyttsx3 SpeechRecognition pyaudio
```

### Windows-specific PyAudio Installation
```bash
pip install pipwin
pipwin install pyaudio
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add more voice commands to Sunday VCA
- Create new game modes for Hangman
- Implement other data structures (Queue, Tree, etc.)
- Add GUI interfaces to existing projects
- Improve error handling and user experience
- Add unit tests

## 📋 Requirements

```
pyttsx3==2.90
SpeechRecognition==3.10.0
wikipedia==1.4.0
pyjokes==0.6.0
pywhatkit==5.4
pyaudio==0.2.13
```

## 📄 License

This project is licensed under the MIT License - feel free to use it for learning and personal projects!

## 👤 Author

**Eshan Maaye**

- GitHub: [@Eshanmaaye](https://github.com/Eshanmaaye)

## 🌟 Acknowledgments

- Thanks to the Python community for excellent libraries
- Google Speech Recognition API for voice processing
- All open-source contributors who make projects like this possible

## 🎯 Future Enhancements

- [ ] Add GUI interface for Sunday VCA
- [ ] Implement more games (Tic-Tac-Toe, Snake, etc.)
- [ ] Add more data structures (Queue, LinkedList, Tree)
- [ ] Create web-based version of projects
- [ ] Add machine learning capabilities to voice assistant
- [ ] Implement database integration
- [ ] Add testing suite

## 📊 Project Stats

- **Lines of Code:** ~600+
- **Projects:** 3
- **Languages:** Python
- **Dependencies:** 6 external libraries

## 💡 Tips

- **For Sunday VCA:** Speak clearly and wait for the "Listening..." prompt
- **For Hangman:** Start with common letters like E, A, R, S, T
- **For Stack:** Try pushing multiple items before displaying to see the LIFO structure

## 📬 Contact & Support

Have questions or suggestions?
- Open an issue on GitHub
- Submit a pull request
- Star ⭐ the repository if you found it helpful!

---

<div align="center">

**Happy Coding! 🚀**

Made with ❤️ and Python by Eshan Maaye

*"Code is like humor. When you have to explain it, it's bad." – Cory House*

</div>
