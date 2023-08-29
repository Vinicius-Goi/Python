import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer()
maquina = pyttsx3.init()

def exercuta_comando():
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if "Jarvis" in comando:
                comando = comando.replace('Jarvis', "")
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print("Microfone não está ok")

    return comando

def comando_voz_user():
    comando = exercuta_comando()
    if "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        maquina.say(f"Agora são {hora}")
        maquina.runAndWait()
    elif "procure por" in comando:
        procurar = comando.replace("procure por", "")
        wikipedia.set_lang('pt')
        result = wikipedia.summary(procurar,2)
        print(result)
        maquina.say(result)
        maquina.runAndWait()
    elif 'toque' in comando:
        musica = comando.replace("toque", "")
        resultado = pywhatkit.playonyt(musica)
        maquina.say(f"Tocando {musica}")
        maquina.runAndWait()

comando_voz_user()