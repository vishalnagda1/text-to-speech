import pyttsx3

# initialize the reading engine
reader = pyttsx3.init()

# Sample text to read
reader.say("Hi there! I'll read text for you.")

# Execution of reading process
reader.runAndWait()

# Finish the reading process
reader.stop()
