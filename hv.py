from microbit import *
import random as rn

hvezdy = [[0,0],[0,0],[0,0],[0,0],[0,0]]
exist = [0,0,0,0,0]

def gen_str():
    hv = rn.randint(0,4)
    if exist[hv] == 0:
        hvezdy[hv][0] = rn.randint(0,4)
        hvezdy[hv][1] = rn.randint(0,4)
        exist[hv] = 1
        
    for i in range(0,5):
        while hvezdy[hv] == hvezdy[i]:
            hvezdy[hv][0] = rn.randint(0,4)
            hvezdy[hv][1] = rn.randint(0,4)
            if hvezdy[hv] != hvezdy[i]:
                break
            
    else:
        gen_str()

def render():
    display.clear()
    for strs in range(0,5):
        if exist[strs] == 1:
            display.set_pixel(hvezdy[strs][0],hvezdy[strs][1],9)

while True:
    if button_a.was_pressed():
        for x in range(0, 5):
            gen_str()
        render()
    if button_b.was_pressed():
        for poz in range(0,5):
            hvezdy[poz][1] += 1
            if hvezdy[poz][1] == 5:
                exist[poz] = 0
                hvezdy[poz] = [0,0]
        render()       
