from microbit import *
import radio
import music
import simplecipher
enc = simplecipher.encrypt()
dec = simplecipher.decrypt()
pohyb = 0
radio.config(channel=69, group=69)
radio.on()
set_x, set_y, set_z = 0, 0, 0
set, alarm, beep = 0, 0, 0
lastT = 0
delayT = 500
while True:
    data = radio.receive()
    if data:
        data = dec.bin(data)
        if data == "alarm":
            alarm = 1
    if alarm == 1 and running_time() >= (lastT + delayT):
        if beep == 0:
            music.pitch(5000)
            beep = 1
        else:
            music.stop()
            beep = 0
    if button_a.is_pressed():
        set_x, set_y, set_z = accelerometer.get_values()
        set = 1
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
        else :
            encdata = "ok"
            encdata = enc.bin(encdata)
            radio.send(encdata)
        #print(encdata)
