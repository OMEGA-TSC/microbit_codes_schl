from microbit import *
import music

cmdsstr = ['help', 'beep', 'println', 'sys', 'disp_write', 'stopwatch', 'hw']
flg_work = 0
indexofcmd = 0
pins = [pin0, pin1, pin2]
stopwatch_vars = [0, 0]
stopwatch_run = 0
default_machine_name = "microbit"
machine_name = default_machine_name
os_version = "0.2.0"
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
        print("invalid argument/s!")
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
            print("invalid argument/s!")
            print("usage: digital_write pin (0-2) value (0-1)")  
    except:
        print("invalid argument/s!")
        print("usage: digital_write pin (0-2) value (0-1)")
        
def sys(args, argslen):
    global machine_name
    sys_args = ['uptime', 'info', 'reboot', 'name']
    name_args = ['set', 'default']
    if argslen > 1 and args[1] == sys_args[0]:
        print(str(round(running_time()/1000, 1)) + " s")
    elif argslen > 1 and args[1] == sys_args[1]:
        print("m_os vesion: " + os_version)
    elif argslen > 1 and args[1] == sys_args[2]:
        print("rebooting...")
        reset()
    elif argslen > 1 and args[1] == sys_args[3]:
        if argslen > 3 and args[2] == name_args[0]:
            if len(args[2]) < 33:
                machine_name = args[3]
            else:
                print("name too long! max length of name is 32 characters")
        elif argslen > 2 and args[2] == name_args[1]:
            machine_name = default_machine_name
        else:
            print("invalid argument/s!")
            print("usage: sys name set <name> or sys name default")
    else:
        print("invalid argument/s!")
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
            print("invalid argument/s!")
            print("usage: disp_write <scroll/show> <text>")

def stopwatch(args, argslen):
    stopwatch_args = ['start', 'stop', 'show', 'reset']
    global stopwatch_run
    if argslen > 1 and args[1] == stopwatch_args[0]:
        if stopwatch_run == 0:
            stopwatch_run = 1
            stopwatch_vars[0] = running_time()
        else:
            print("cannot start stopwatch when running!")
    elif argslen > 1 and args[1] == stopwatch_args[1]:
        if stopwatch_run == 1:
            stopwatch_run = 0
            stopwatch_vars[1] = running_time()
        else:
            print("cannot stop stopwatch when not running!")
    elif argslen > 1 and args[1] == stopwatch_args[2]:
        if stopwatch_run == 1:
            time_ms = running_time() - stopwatch_vars[0]
            ms = time_ms % 1000
            sec = int((time_ms - ms) / 1000) % 60
            min = int(((time_ms -ms) / 1000) / 60) % 60
            print("elapsed time: " + str(min) + ":" + str(sec) + ":" + str(ms))
        else:
            time_ms = stopwatch_vars[1] - stopwatch_vars[0]
            ms = time_ms % 1000
            sec = int((time_ms - ms) / 1000) % 60
            min = int(((time_ms -ms) / 1000) / 60) % 60
            print("stopwatch time: " + str(min) + ":" + str(sec) + ":" + str(ms))
    elif argslen > 1 and args[1] == stopwatch_args[3]:
        if stopwatch_run == 0:
            stopwatch_vars[0] = 0
            stopwatch_vars[1] = 0
        else:
            print("cannot reset stopwatch when running!")
    else:
        print("invalid argument/s!")
        print("usage: stopwatch <argument>")
        print('available arguments for "stopwatch":')
        for arg in stopwatch_args:
            print(arg)
       
def hw(args, argslen):
    hw_args = ['digital']
    digital_args = ['write', 'read']
    if argslen > 3 and args[1] == hw_args[0]:
        if argslen > 4 and digital_args[0] == args[2]:
            try:
                pins[int(args[3])].write_digital(int(args[4]))
            except:
                print("invalid argument/s!")
                print("usage: hw digital write <pin> (0-2) <value> (0-1)")
        elif argslen > 3 and digital_args[1] == args[2]:
            try:
                print(pins[int(args[3])].read_digital())
            except:
                print("invalid argument/s!")
                print("usage: hw digital read <pin> (0-2)")
        else:
            print("invalid argument/s!")
            print("usage: digital write/read <argument/s>")
            print('available arguments for "digital":')
            for arg in hw_args:
                print(arg)     
    else:
        print("invalid argument/s!")
        print("usage: hw <argument>")
        print('available arguments for "hw":')
        for arg in hw_args:
            print(arg)

cmds = [help, beep, println, sys, disp_write, stopwatch, hw]
        
while True:
    cmd = input("@" + machine_name + ">")
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
