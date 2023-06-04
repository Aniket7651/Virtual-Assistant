import pyttsx3
import webbrowser
import os, subprocess
import speech_recognition as speak
import datetime
import wikipedia
import re, urllib.parse, urllib.request

def YTsearch(search):
    return webbrowser.open('youtube.com/results?search_query=%s' %search.replace(' ', '+'))

query = []
answer = []
Q_A_file = os.path.abspath('virtual assistant/talking.txt')
with open(Q_A_file) as answers:
    lines = answers.readlines()
    for line in lines:
        splite = line.split('-')
        query.append(splite[0])
        answer.append(splite[1])
dict_form = {query[i]: answer[i] for i in range(len(query))}

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 148)

try:
    recogniz = speak.Recognizer()
    with speak.Microphone(device_index=1) as input:
        audio = recogniz.listen(input, phrase_time_limit=4)
        recogniz.adjust_for_ambient_noise(input)
        sentence = recogniz.recognize_google(audio)
        print(sentence)
except speak.UnknownValueError:
    engine.say('oops, speech time out')
    engine.runAndWait()
        
if 'Ani' in sentence:
    acceptableSpeech = sentence.replace('Ani', '')

    if acceptableSpeech in dict_form:
        engine.say(dict_form[acceptableSpeech])
        engine.runAndWait()

    elif 'Chrome' in acceptableSpeech:
        engine.say('sure, launching chrome browser')
        engine.runAndWait()
        subprocess.call("C:/Program Files/Google/Chrome/Application/chrome.exe")

    elif 'browser' in acceptableSpeech:
        if 'search' in acceptableSpeech:
            searchingFor = acceptableSpeech.split('search')
            engine.say(f'browser searching {searchingFor[-1]}, please wait for a second')
            engine.runAndWait()
            webbrowser.open('www.bing.com/search?q=%s' %searchingFor[-1])
        else:
            subprocess.call('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe')
            engine.say('there is the microsoft edge for acceptable browser')
            engine.runAndWait()

    elif 'YouTube' in acceptableSpeech:
        if 'search' in acceptableSpeech:
            searchingFor = acceptableSpeech.split('search')
            engine.say(f"I'm searching {searchingFor[-1]} on you tube, please wait")
            engine.runAndWait()
            YTsearch(searchingFor[-1])
        else:
            engine.say('of course, launching you tube')
            engine.runAndWait()
            webbrowser.open('youtube.com')

    elif 'time' in acceptableSpeech:
        engine.say('now, the time is %s' %datetime.datetime.now().strftime('%I %M %p'))
        print(datetime.datetime.now().strftime('%I:%M %p'))
        engine.runAndWait()

    elif 'Excel' in acceptableSpeech:
        engine.say('yeh, microsoft excel opend')
        engine.runAndWait()
        subprocess.call("C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe")

    elif 'play' in acceptableSpeech:
        if 'song' in acceptableSpeech:
            searchingFor = acceptableSpeech.split('song')
            song = f'{searchingFor[-1]}+song'
            engine.say(wikipedia.summary(song, 1))
            engine.runAndWait()
            query_s = urllib.parse.urlencode({'search_query': song})
            Url = urllib.request.urlopen('https://youtube.com/results?'+query_s)
            search_results = re.findall(r"watch\?v=(\S{11})", Url.read().decode())
            # print(search_results)
            clip = 'youtube.com/watch?v='+'{}'.format(search_results[0])
            webbrowser.open(clip)

        else:
            searchingFor = acceptableSpeech.split('play')
            song = f'{searchingFor[-1]}+movie'
            engine.say(wikipedia.summary(song, 1))
            engine.runAndWait()
            query_s = urllib.parse.urlencode({'search_query': song})
            Url = urllib.request.urlopen('https://youtube.com/results?'+query_s)
            search_results = re.findall(r"watch\?v=(\S{11})", Url.read().decode())
            # print(search_results)
            clip = 'youtube.com/watch?v='+'{}'.format(search_results[0])
            webbrowser.open(clip)


    elif 'what' or 'where' or 'when' or 'whome' or 'who' in acceptableSpeech:
        try:
            engine.say(wikipedia.summary(acceptableSpeech, 2))
            engine.runAndWait()
        except wikipedia.exceptions.PageError:
            engine.say('I have no idea about this')
            engine.runAndWait()

    else:
        engine.say("what do you mean, I couldn't understand you")
        engine.runAndWait()

print('accepted')