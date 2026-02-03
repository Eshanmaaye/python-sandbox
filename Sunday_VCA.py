# Sunday Voice Command Assistant (VCA) - Version 3.0
# Upgraded with bug fixes and new features

import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia 
import webbrowser 
import os
import pyjokes
from googlesearch import search
import pywhatkit as pwt
import pyaudio
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Adjust speech rate for better clarity
engine.setProperty('rate', 180)

# Speak function
def speak(audio):
    """Convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Greet the user based on time of day"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning boss, I am Sunday. How are you boss?")
    elif 12 <= hour < 17:
        speak('Good afternoon boss, I am Sunday. How are you?')
    else:
        speak("Good evening boss. I am Sunday. How are you?")

def command():
    """Listen to user voice command and convert to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1.5
        r.dynamic_energy_threshold = True
        
        try:
            r.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            print(f"Noise adjustment error: {e}")
        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("No speech detected. Listening again...")
            return "None"
    
    try:
        print("Processing your command...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Speech recognition service error: {e}")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"

def get_voice_input(prompt="Speak now..."):
    """Get voice input from user"""
    speak(prompt)
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print(prompt)
        try:
            r.adjust_for_ambient_noise(source, duration=0.8)
        except Exception:
            pass
        
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand.")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

def play_media_file(directory, file_type="file"):
    """Play a media file from specified directory"""
    if os.path.exists(directory):
        try:
            files = os.listdir(directory)
            if files:
                print(f"Found {file_type}s: {files}")
                os.startfile(os.path.join(directory, files[0]))
                return True
            else:
                speak(f"No {file_type}s found in the directory")
                return False
        except Exception as e:
            print(f"Error playing {file_type}: {e}")
            speak(f"Error playing {file_type}")
            return False
    else:
        speak(f"{file_type.capitalize()} directory not found")
        return False

def show_help():
    """Display available commands"""
    print("\n" + "="*60)
    print("SUNDAY VCA - Available Commands:")
    print("="*60)
    commands = {
        "wikipedia [topic]": "Search Wikipedia for information",
        "play video": "Play video from your video folder",
        "fine": "Casual conversation response",
        "what is the time": "Tell current time",
        "what is the date": "Tell current date",
        "alarm": "Set an alarm with music",
        "google [search]": "Search Google and open top result",
        "youtube [search]": "Search and play on YouTube",
        "joke": "Tell a random joke",
        "help": "Show emergency contact numbers",
        "hurt": "Get first-aid suggestions",
        "calculation": "Perform math calculations",
        "open notepad": "Open Notepad application",
        "open calculator": "Open Calculator application",
        "system info": "Get system information",
        "exit/quit/sleep": "Stop the assistant"
    }
    for cmd, desc in commands.items():
        print(f"  • {cmd:20} - {desc}")
    print("="*60 + "\n")

# Main execution
if __name__ == "__main__":
    wishme()
    speak("How may I help you today?")
    
    while True:
        query = command().lower()
        
        if query == "none":
            continue
        
        # Wikipedia search
        if "wikipedia" in query:
            speak("Searching in Wikipedia")
            query = query.replace("wikipedia", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Multiple results found. Please be more specific.")
                print(f"Options: {e.options[:5]}")
            except wikipedia.exceptions.PageError:
                speak("No Wikipedia page found for that topic.")
            except Exception as e:
                print(f"Wikipedia error: {e}")
                speak("Error searching Wikipedia")
        
        # Play video
        elif 'play video' in query:
            speak("Playing video")
            videodir = "C:\\Eshan\\Movies"
            play_media_file(videodir, "video")
        
        # Casual conversation
        elif "fine" in query or "good" in query:
            speak("Me too fine!")
            speak("I am a voice command assistant.")
            speak("What can I do for you?")
        
        # Tell time
        elif "time" in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%I:%M %p")
            speak(f"The time is {current_time}")
            print(f"Current time: {current_time}")
        
        # Tell date
        elif "date" in query:
            now = datetime.datetime.now()
            current_date = now.strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
            print(f"Current date: {current_date}")
        
        # Set alarm
        elif "alarm" in query:
            speak("Setting an alarm. Please enter the time below")
            try:
                alarmHour = int(input("Enter hour (0-23): "))
                alarmMin = int(input("Enter minutes (0-59): "))
                
                if not (0 <= alarmHour <= 23 and 0 <= alarmMin <= 59):
                    speak("Invalid time entered")
                    continue
                
                speak(f"Alarm set for {alarmHour}:{alarmMin:02d}")
                print(f"Waiting for {alarmHour}:{alarmMin:02d}...")
                
                while True:
                    now = datetime.datetime.now()
                    if now.hour == alarmHour and now.minute == alarmMin:
                        speak("Alarm! Time's up!")
                        print("Playing alarm music...")
                        Musicdir = "C:\\Eshan\\New"
                        play_media_file(Musicdir, "music")
                        break
                    time.sleep(30)  # Check every 30 seconds instead of constantly
                    
            except ValueError:
                speak("Invalid input. Please enter numbers only.")
            except KeyboardInterrupt:
                speak("Alarm cancelled")
        
        # Google search
        elif "google" in query:
            search_query = get_voice_input("What would you like to search on Google?")
            if search_query:
                try:
                    speak("Searching Google")
                    for url in search(search_query, tld="com", num=1, stop=1, pause=2):
                        webbrowser.open(url)
                        speak("Here are the results")
                        break
                except Exception as e:
                    print(f"Google search error: {e}")
                    speak("Error performing Google search")
        
        # YouTube search
        elif "youtube" in query:
            search_query = get_voice_input("What would you like to search on YouTube?")
            if search_query:
                try:
                    speak("Searching YouTube")
                    pwt.playonyt(search_query)
                except Exception as e:
                    print(f"YouTube error: {e}")
                    speak("Error playing on YouTube")
        
        # Tell a joke
        elif "joke" in query:
            speak("Okay, I'll tell you a joke")
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        
        # Emergency help
        elif "help" in query and "emergency" not in query:
            speak("Oh no! Are you in danger?")
            speak("Here are emergency phone numbers in your region")
            print("\n" + "="*40)
            print("EMERGENCY NUMBERS (India)")
            print("="*40)
            print("Police: 100")
            print("Ambulance: 108")
            print("Fire: 101")
            print("Emergency: 112")
            print("="*40 + "\n")
        
        # First aid for injury
        elif "hurt" in query or "injured" in query:
            speak("Oh no! I feel very sad about that")
            speak("Please seek a first aid kit or ask someone to help you")
            speak("If it's serious, call ambulance at 108")
        
        # Calculator
        elif "calculation" in query or "calculate" in query:
            expression = get_voice_input("Please say the calculation. Say 'plus' for +, 'minus' for -, 'multiply' or 'into' for *, 'divided by' for /")
            if expression:
                try:
                    # Replace words with operators
                    expression = expression.replace("plus", "+").replace("minus", "-")
                    expression = expression.replace("into", "*").replace("multiply", "*").replace("multiplied by", "*")
                    expression = expression.replace("divided by", "/").replace("divide", "/")
                    expression = expression.replace("x", "*").replace("X", "*")
                    
                    # Remove extra words
                    expression = expression.replace("what is", "").replace("equals", "").strip()
                    
                    result = eval(expression)
                    speak(f"The answer is {result}")
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Calculation error: {e}")
                    speak("I couldn't process that calculation. Please try again.")
        
        # Open Notepad
        elif "open notepad" in query:
            speak("Opening Notepad")
            os.system("notepad.exe")
        
        # Open Calculator
        elif "open calculator" in query:
            speak("Opening Calculator")
            os.system("calc.exe")
        
        # System information
        elif "system info" in query or "system information" in query:
            speak("Gathering system information")
            import platform
            print("\n" + "="*40)
            print("SYSTEM INFORMATION")
            print("="*40)
            print(f"System: {platform.system()}")
            print(f"Release: {platform.release()}")
            print(f"Version: {platform.version()}")
            print(f"Machine: {platform.machine()}")
            print(f"Processor: {platform.processor()}")
            print("="*40 + "\n")
            speak("System information displayed")
        
        # Show available commands
        elif "commands" in query or "what can you do" in query:
            speak("Here are the commands I can respond to")
            show_help()
        
        # Exit commands
        elif any(word in query for word in ['sleep', 'exit', 'quit', 'bye', 'goodbye']):
            speak("Okay, as your wish boss. Goodbye!")
            break
        
        # Unknown command
        else:
            speak("I cannot recognize what you're saying")
            speak("Say 'commands' to see what I can do")
            show_help()
