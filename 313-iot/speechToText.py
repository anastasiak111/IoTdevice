# Importerer libraries/pakker
import speech_recognition as sr
import pyttsx3
import keyboard
import threading

#funksjon som kan calles fra Index.py
def speechToText():
    r = sr.Recognizer()
    # Used to signal the thread to stop
    stop_flag = threading.Event()  

    # Function to record text from microphone
    def record_text():
        # Keep listening until the stop flag is set
        while not stop_flag.is_set():  
            try:
                with sr.Microphone() as mic:
                    r.adjust_for_ambient_noise(mic, duration=0.2)
                    userAudio = r.listen(mic)
                    requestText = r.recognize_google(userAudio, language="EN-gb")
                    
                    input_text(requestText)

                    print("Wrote text")

            except sr.RequestError as e:
                print("Could not request result; {0}".format(e))

            except sr.UnknownValueError:
                print("Cannot understand you, speak clearly. :)")

    # Function to clear input.txt
    def clear_text():
        f = open("input.txt", "w") 
        f.close()

        return  
    
    # Function that makes and empties the input.txt file
    def input_text(text):
        f = open("input.txt", "a") # Lager en input-fil
        f.write(text) # Skriver tekst
        f.write("\n") # Ny linje
        f.close()

        return

    # Clear input.txt at the start
    clear_text()

    # Start the recording thread
    recording_thread = threading.Thread(target=record_text)
    recording_thread.start()

    # Main loop to detect keystroke
    while True:
        # Stop when "q" is pressed
        if keyboard.is_pressed("q"):  
            print("Exiting...")
            # Signal the recording thread to stop
            stop_flag.set()  
            # Wait for the recording thread to finish
            recording_thread.join()  
            break