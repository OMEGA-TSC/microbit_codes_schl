from microbit import *
import radio
radio.config(channel=55, group=123)
radio.on()
strdata = []
id = 0
hlas = 0
while True:
    data = radio.receive()
    if data:
        strdata = data.split(":")
        id = strdata[0]
        hlas = strdata[1]
    
