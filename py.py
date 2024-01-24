from microbit import *
import audio
def frames_from_file(sfile, frame):
    # 32 is length of AudioFrame
    while(sfile.readinto(frame, 32) > 0):
        yield frame
def play_file(filename):
    frame = audio.AudioFrame()
    with open(filename, "rb") as snd_file:
        audio.play(frames_from_file(snd_file, frame), wait=True)
        audio.stop()   
while True:
    play_file("haah.wav")
    sleep(5000)
    open(filename,"rb")
