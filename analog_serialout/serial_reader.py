import serial
import time
import mouse

# setup serial line
ser = serial.Serial('COM3', 9600)
time.sleep(2)
disabled = False
while True:
    b = ser.readline()
    b = b.decode('UTF-8')
    print(b) #SWITCH|Y|X when oriented with wires below. Switch 1 = not pressed, Switch 0 = pressed. #x,y = 0 means bottom-left-most corner
    b = b.split("|")
    currMouse = mouse.get_position()
    if int(b[0]) == 0 and not disabled: # analog pressed
        mouse.click('left')
        disabled = True
    if int(b[0]) == 1:
        disabled = False
    y = (int(b[1]) - 514) // 50 # Center at 0
    x = -((int(b[2]) - 505) // 50) # Center at 0
    mouse.move(x,y,absolute=False)
ser.close()