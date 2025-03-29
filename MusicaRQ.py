import speech_recognition as sr
from youtube_search import YoutubeSearch

def ouvir_microfone():

    microfone = sr.Recognizer()
    
   
    with sr.Microphone() as source:
        
     
        microfone.adjust_for_ambient_noise(source)
        
        
        print("Diga alguma coisa: ")
        
     
        audio = microfone.listen(source)
        
    try:
        
        frase = microfone.recognize_google(audio)
        result = YoutubeSearch(frase,1).to_dict()
        result = 'http://youtube.com/'+result[0]['url_suffix']
        print("Você disse: " + frase)
        print(result)
   
    except sr.UnknownValueError:
        print("Não entendi")
        
    return frase

ouvir_microfone()