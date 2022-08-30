import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser

engine =  pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Speak an audio
def speakLoud(audio):
    engine.say(audio)
    engine.runAndWait()
    
# Wish by time 
def wishMe():
    
    hour =  int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speakLoud("Good Morning Sir")
    elif hour>=12 and hour<18:
        speakLoud("Good Afternoon Sir")
    else:
        speakLoud("Good Evening Sir")
    speakLoud("I am Jarvis, How may I help you")

# hear voice 
def hearVoice():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
        speakLoud("Listening")
        print("Listening...")
        r.pause_threshold = 1
        audio =  r.listen(source)
        
    try:
        print("Recognizing...")
        query =  r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speakLoud("Sorry Sir I didn't get that")
        print("Say that again please...")
        return "None"
    return query
        
    
# Main function

if __name__ == "__main__":
    wishMe()
    while 1:
        query =  hearVoice().lower()
        
        if 'wikipedia' in query :
            speakLoud("Searching Wikipedia...")
            query =  query.replace("wikipedia","")
            result =  wikipedia.summary(query, sentences=2)
            speakLoud("According to wikipedia ")
            speakLoud(result)
        if 'open youtube' in query:
            speakLoud("Opening youtube")
            webbrowser.open("youtube.com")
        if 'time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speakLoud(strTime)
print(voices)