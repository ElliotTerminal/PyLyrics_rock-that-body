import sys
from time import sleep
from rich import print
from playsound import playsound  # For MP3 playback
import threading  # To run audio and lyrics simultaneously

def printlyrics():
    lines = [
        ("I wanna da-", 0.3),  # Faster delay for this line
        ("I wanna dance in the lights", 1.9),
        ("I wanna ro-", 0.3),
        ("I wanna rock your body", 2),
        ("I wanna go", 0.3),
        ("I wanna go for a ride", 1.9),
        ("Hop in the music and", 0.4),
        ("Rock your body", 1.2),
        ("Rock that body", 0.3),
        ("come on, come on", 0.2),  # Reduced delay
        ("Rock that body", 0.2),
        ("Rock your body", 0.2),  # Reduced delay
        ("Rock that body", 0.3),
        ("come on, come on", 0.2),  # Reduced delay
        ("ROCK", 0.2),
        ("THAT", 0.2),
        ("BODY", 0.4)
    ]

    for line, delay in lines:
        for char in line:
            print(char, end="", flush=True)  
            sleep(0.05)  # Small delay between characters
        print()  # Move to the next line after printing all characters
        sleep(delay)  # Custom delay after the entire line

if __name__ == "__main__":
    # Path to your MP3 file
    # if added manually, name the audio file with 'the_name_you_gave.mp3' for the compiler to identify the audio name
    mp3_path = "audio.mp3"

    audio_thread = threading.Thread(target=playsound, args=(mp3_path,))
    audio_thread.start()

    # Run the lyrics display
    printlyrics()

    audio_thread.join()
