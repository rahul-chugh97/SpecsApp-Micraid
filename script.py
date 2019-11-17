import os

cmd='./bin/flite -voice voices/cmu_indic_hin_ab.flitevox --setf duration_stretch=0.75 -f doc/aktu.txt xyzz.wav'
os.system(cmd)

print('Audio file created. xyzz.wav')

from playsound import playsound
playsound('xyzz.wav')