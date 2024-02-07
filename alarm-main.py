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
set = 0
while True:
   # data = radio.receive()
    #if data:
     #   data = dec.bin(data)
      #  if data == "1":
      #      music.pitch(5000)
    
    if button_a.is_pressed():
        set_x, set_y, set_z = accelerometer.get_values()
        set = 1
    if accelerometer.get_x() > set_x + 20 or accelerometer.get_x() < set_x + 20 and set == 1:
        encdata = "1"
        encdata = enc.bin(encdata)
        radio.send(encdata)
    else :
        encdata = "0"
        encdata = enc.bin(encdata)
        radio.send(encdata)
        print(accelerometer.get_values())
        
        
    
    
    
    
    
            