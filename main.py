import pyttsx3
import argparse

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-t", "--text", help="Command line input of text")

# Read arguments from command line
args = parser.parse_args()

text_to_read = "Hi there! I'll read text for you."
if args.text:
    text_to_read = args.text

# initialize the reading engine
reader = pyttsx3.init()

# read the given text
reader.say(text_to_read)

# Execution of reading process
reader.runAndWait()

# Finish the reading process
reader.stop()
