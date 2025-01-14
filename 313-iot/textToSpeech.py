import pyttsx3
import asyncio

def textToSpeech():
    with open('output.txt', 'r') as o:  # Using 'with' to handle file closing automatically
        content = o.read()  # Read the entire file content into a string
    engine = pyttsx3.init()
    engine.say(content)  # Pass the text content to engine.say()
    engine.runAndWait()  # Run the speech engine to speak the text

# Call the function
#textToSpeech()