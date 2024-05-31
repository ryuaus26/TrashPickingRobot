import speech_recognition as sr
import google.generativeai as genai

# Configure the API key
GOOGLE_API_KEY = "AIzaSyBzgOrW5BHN6Npxb6wha6Cm1Of8QhVpci8"
genai.configure(api_key=GOOGLE_API_KEY)

# Create the Gemini text generation model
gemini_model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

# Initialize the speech recognizer
r = sr.Recognizer()

# Open the default microphone
mic = sr.Microphone()

while True:
    print("Say something...")

    # Capture audio from the microphone
    with mic as source:
        audio = r.listen(source)

    try:
        # Use the Google Speech Recognition engine to transcribe the audio
        text = r.recognize_google(audio)
        print("You said:", text)

        # Generate text using Gemini model with the transcribed text as input
        gemini_response = gemini_model.generate_content([text])
        print("Gemini response:", gemini_response)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    if input("Press Enter to continue or 'q' to quit: ").lower() == 'q':
        break