from pynput import mouse
import time 

count = 0
maxCount = 100
increment = 3

def on_scroll(x, y, dx, dy):
    global count, maxCount
    count = count+increment if count < maxCount else maxCount


listener = mouse.Listener(
   # on_move=on_move,
   # on_click=on_click,
    on_scroll=on_scroll)

listener.start()

def display(x,y):
    percent = x/y if x/y < 1 else 1
    length = 40
    progress = (int)(length*percent)
    print("[{}{}]".format(progress*"|",(length-progress)*"-"))


while True:
    time.sleep(.5)
    display(count,maxCount)
    count = count-1 if count-1>0 else 0 