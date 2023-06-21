import os
import shutil
# open text
with open('top50.txt', 'r') as f:
    lines = f.readlines()
# remove \n
lines = [line.strip() for line in lines]
# remove empty lines
lines = [line for line in lines if line != '']

mid_dir=r"W:\datasets\D2MIDI\D2MIDI_V1\new\30S\16000HZ_cleaned/"
output_dir=r"./assets/wav/"
wav_dir=r"W:\datasets\D2MIDI\D2MIDI_V1\new\30S\audio/"

# cp files
for line in lines:
    print(line)
    try:
        shutil.copy(os.path.join(wav_dir,line+".wav"),output_dir)
    except:
        print("error")
        continue
