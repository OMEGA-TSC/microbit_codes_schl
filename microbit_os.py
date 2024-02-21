from microbit import *
import music

def beep(args, argslen):
    try:
        if argslen == 1:
            music.pitch(2500, 1000)
        elif argslen == 2:
            music.pitch(int(args[1]), 1000)
        elif argslen == 3:
            music.pitch(int(args[1]), int(args[2]))
    except:
        print("invalid input!")

cmdsstr = ['beep']
cmds = [beep]
        
while True:
    cmd = input("@microbit>")
    args = cmd.split(" ")
    argslen = len(args)
    for i in range(len(cmds)):
        if cmdsstr[i] == args[0]:
            cmds[i](args, argslen)
