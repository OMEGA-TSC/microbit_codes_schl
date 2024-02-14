from microbit import *
import radio
import music
import simplecipher
enc = simplecipher.encrypt()
dec = simplecipher.decrypt()
pohyb = 0
radio.config(channel=69, group=69, length=64)
radio.on()
set_x, set_y, set_z = 0, 0, 0
set, alarm, beep = 0, 0, 0
lastT = 0
delayT = 500
data = ""
for x in range(5):
    for y in range(5):
        display.set_pixel(x, y, 9)
display.off()
while True:
    data = radio.receive()
    if data:
        data = dec.bin(data)
        if data == "alarm":
            alarm = 1
        elif data == "reset":
            alarm = 0
            set = 0
            alarm = 0
            music.stop()
            display.off()
            
    if alarm == 1 and running_time() >= (lastT + delayT):
        if beep == 0:
            music.pitch(2500)
            display.on()
            beep = 1
        else:
            music.stop()
            display.off()
            beep = 0
        lastT = running_time()
        
    if button_a.is_pressed():
        set_x, set_y, set_z = accelerometer.get_values()
        set = 1
        
    if button_b.is_pressed():
        set = 0
        alarm = 0
        music.stop()
        display.off()

    if pin_logo.is_touched():
        radio.send(enc.bin("reset"))
        
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
            
        print(encdata)
