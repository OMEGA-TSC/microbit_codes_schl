from microbit import *
import music

cmdsstr = ['help', 'beep', 'println', 'digital_write', 'sys', 'disp_write']
flg_work = 0
indexofcmd = 0
pins = [pin0, pin1, pin2]

def help(args, argslen):
    if argslen == 1:
        print("available functions:")
        for funs in cmdsstr:
            print(funs)
          
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
        print("usage: beep *frequency (int) *duratioon (int)  (* = optional argument)")

def println(args, argslen):
    res = ''
    for i in range(1, argslen):
        res += str(args[i])
        res += " "
    print(res)
    
def digital_write(args, argslen):
    try:
        if argslen == 3:
            pins[int(args[1])].write_digital(int(args[2]))
        else:
            print("invalid input!")
            print("usage: digital_write pin (0-2) value (0-1)")  
    except:
        print("invalid input!")
        print("usage: digital_write pin (0-2) value (0-1)")
        
def sys(args, argslen):
    sys_args = ['uptime', 'info', 'reboot']
    if argslen > 1 and args[1] == 'uptime':
        print(str(round(running_time()/1000, 1)) + " s")
    elif argslen > 1 and args[1] == 'info':
        print("m_os vesion: 1.0")
    elif argslen > 1 and args[1] == 'reboot':
        print("rebooting...")
        reset()
    else:
        print("invalid input!")
        print("usage: sys <argument>")
        print('available arguments for "sys":')
        for arg in sys_args:
            print(arg)

def disp_write(args, argslen):
    res = ""
    if argslen > 2:
        if args[1] == 'scroll':
            for i in range(2,argslen):
                res += args[i]
                res += " "
            display.scroll(res)
        elif args[1] == 'show':
            for i in range(2,argslen):
                res += args[i]
                res += " "
            display.show(res)
        else:
            print("invalid input!")
            print("usage: disp_write <scroll/show> <text>")
                  
cmds = [help, beep, println, digital_write, sys, disp_write]
        
while True:
    cmd = input("@microbit>")
    args = cmd.split(" ")
    argslen = len(args)
    try:
        indexofcmd = cmdsstr.index(args[0])
        flg_work = 1
    except:
        print("command doesn't exist use help for more info")
    if flg_work == 1:
        cmds[indexofcmd](args, argslen)
        flg_work = 0   
