from microbit import *
import radio
import music
import simplecipher
enc = simplecipher.encrypt()
dec = simplecipher.decrypt()
radio.config(channel=21, group=123, length=64)
radio.on()
set_x, set_y, set_z = 0, 0, 0
set, alarm, beep = 0, 0, 0
lastT, lastTled = 0, 0
delayT, delayTled = 500, 2
data = ""
dir = 1
pwm = 0
while True:
    data = radio.receive()
    if data:
        data = dec.bin(data)
        if data == "alarm":
            alarm = 1
            pin1.write_analog(0)
        elif data == "reset":
            alarm = 0
            set = 0
            alarm = 0
            music.stop()
            pin0.write_digital(0)
            
    if alarm == 1 and running_time() >= (lastT + delayT):
        if beep == 0:
            music.pitch(2500)
            pin0.write_digital(1)
            beep = 1
        else:
            music.stop()
            pin0.write_digital(0)
            beep = 0
        lastT = running_time()
    if alarm == 0 and running_time() >= (lastTled + delayTled):
        if dir == 1:
            pin1.write_analog(pwm)
            pwm += 1
            if pwm == 1023:
                dir = 0
        else:
            pin1.write_analog(pwm)
            pwm -=1
            if pwm == 0:
                dir = 1
        lastTled = running_time()
            
    if button_a.is_pressed():
        sleep(1000)
        set_x, set_y, set_z = accelerometer.get_values()
        set = 1
        
    if button_b.is_pressed():
        set = 0
        alarm = 0
        music.stop()
        pin0.write_digital(0)

    if pin_logo.is_touched():
        radio.send(enc.bin("reset"))
        sleep(500)
        
    if set == 1:
        if (accelerometer.get_x() > (set_x + 50))  or (accelerometer.get_x() < (set_x - 50)):
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
            
        elif (accelerometer.get_y() > (set_y + 50))  or (accelerometer.get_y() < (set_y - 50)):
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
            
        elif (accelerometer.get_z() > (set_z + 50))  or (accelerometer.get_z() < (set_z - 50)):
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        elif microphone.sound_level() > 170:
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        else :
            encdata = "ok"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        print(encdata)from microbit import *
import radio
import music
import simplecipher
enc = simplecipher.encrypt()
dec = simplecipher.decrypt()
radio.config(channel=21, group=123, length=64)
radio.on()
set_x, set_y, set_z = 0, 0, 0
set, alarm, beep = 0, 0, 0
lastT, lastTled = 0, 0
delayT, delayTled = 500, 2
data = ""
dir = 1
pwm = 0
while True:
    data = radio.receive()
    if data:
        data = dec.bin(data)
        if data == "alarm":
            alarm = 1
            pin1.write_analog(0)
        elif data == "reset":
            alarm = 0
            set = 0
            alarm = 0
            music.stop()
            pin0.write_digital(0)
            
    if alarm == 1 and running_time() >= (lastT + delayT):
        if beep == 0:
            music.pitch(2500)
            pin0.write_digital(1)
            beep = 1
        else:
            music.stop()
            pin0.write_digital(0)
            beep = 0
        lastT = running_time()
    if alarm == 0 and running_time() >= (lastTled + delayTled):
        if dir == 1:
            pin1.write_analog(pwm)
            pwm += 1
            if pwm == 1023:
                dir = 0
        else:
            pin1.write_analog(pwm)
            pwm -=1
            if pwm == 0:
                dir = 1
        lastTled = running_time()
            
    if button_a.is_pressed():
        sleep(1000)
        set_x, set_y, set_z = accelerometer.get_values()
        set = 1
        
    if button_b.is_pressed():
        set = 0
        alarm = 0
        music.stop()
        pin0.write_digital(0)

    if pin_logo.is_touched():
        radio.send(enc.bin("reset"))
        sleep(500)
        
    if set == 1:
        if (accelerometer.get_x() > (set_x + 50))  or (accelerometer.get_x() < (set_x - 50)):
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
            
        elif (accelerometer.get_y() > (set_y + 50))  or (accelerometer.get_y() < (set_y - 50)):
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
            
        elif (accelerometer.get_z() > (set_z + 50))  or (accelerometer.get_z() < (set_z - 50)):
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        elif microphone.sound_level() > 170:
            encdata = "alarm"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        else :
            encdata = "ok"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        print(encdata)
