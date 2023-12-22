import os
import subprocess
import speech_recognition as speech_r

######## BUILD SETUPS ########

# apps = ['chrome.exe', 'msedge.exe', 'EXCEL.exe']
# dir = ['Chrome', 'Microsoft', 'Microsoft Office']

# def path(file_name, dir_name, drive='C'):
#     PATH = ''
#     PATH_DIR = ''
#     for root, dir, files in os.walk('%s:/'%drive):
#         for f in files:
#             if f == file_name:
#                 PATH = os.path.join(root, f)
#         for d in dir:
#             if d == dir_name:
#                 PATH_DIR = os.path.join(root, d)
#     return PATH.replace('\\', '/'), PATH_DIR.replace('\\', '/')


# def read_setupLogs(file):
#     log = []
#     with open(file, 'r') as f:
#         for i in f.readlines():
#             log.append(i.replace('\n', ''))

#     locations = {i.split(':')[0]: i.split(':')[1] for i in log}
#     return locations
    

# print(read_setupLogs(path('setup_logs.txt', 'pyAssistant', 'A')[0]))
audioRecognizer = speech_r.Recognizer()
with speech_r.Microphone() as input:
    audioRecognizer.adjust_for_ambient_noise(input)
    audio = audioRecognizer.listen(input)
    print(audio)