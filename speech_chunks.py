import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import os, glob, csv
import speech_recognition as sr
from pydub.playback import play
import pyaudio
import time
import sys
from pydub.silence import split_on_silence
import wave
from pydub import AudioSegment

pa = pyaudio.PyAudio()


def main(path):
        audio_file_name = path
        print('audio file name: ', audio_file_name)
        audio_file = sr.AudioFile(infile)
        print(audio_file, type(audio_file))
        audio = AudioSegment.from_wav(infile)
        fh = open(path  "recognized.txt", "w+") 
        n = len(audio)  
        counter = 1
        fh = open(path + "recognized.txt", "w+") 
        interval = 12 * 1000
        overlap = 1.5 * 1000
        start = 0
        end = 0
        flag = 0
        for i in range(0, 2 *(n+1), interval): 
            if i == 0: 
                start = 0
                end = interval 
            else: 
                start = end - overlap 
                end = start + interval  
            if end >= (n+1): 
                end = (n+1) 
                flag = 1
            chunk = audio[start:end] 
            filename = path  + 'chunk'+str(counter)+'.wav'
            print(filename)
            chunk.export(filename, format ="wav") 
            print("Processing chunk "+str(counter)+". Start = "
                        +str(start)+" end = "+str(end)) 
            counter = counter + 1
            AUDIO_FILE = filename 
            r = sr.Recognizer()    
            with sr.AudioFile(AUDIO_FILE) as source:
                r.adjust_for_ambient_noise(source, duration=0.01)
                audio_listened =r.record(source)  
            try:     
                rec = r.recognize_google(audio_listened) 
                fh.write(rec+" ") 
            except sr.UnknownValueError: 
                print("Could not understand audio") 
            except sr.RequestError as e: 
                print("Could not request results.") 
            if flag == 1: 
                fh.close() 
                break
    print("end")

if __name__ == '__main__':
    argumentList = sys.argv 
    main(sys.argv[1])
