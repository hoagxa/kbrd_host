import time
import serial
from pynput import keyboard


# Khai bao cong Serial
ser = serial.Serial(
	port = '/dev/ttyAMA0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1)
try:
    while True:
        def on_press(key):
            try:
                print('Alphanumerhhic key pressed: {0} '.format(key.char))
                ser.write((key.char).encode())
                ser.flush()
            except AttributeError:
                print('Special key pressed: {0}'.format(key))
                data = b''
                if key == keyboard.Key.tab :
                    print('Tab')
                    data = b'~' #126
                if key == keyboard.Key.shift :
                    print('Shift')
                    data = b'!' #33
                if key == keyboard.Key.ctrl :
                    print('Ctrl')
                    data = b'@' #64
                if key == keyboard.Key.page_down :
                    print('PgD')
                    data = b'#' #35
                if key == keyboard.Key.page_up :
                    print('PgU')
                    data = b'$' #36
                if key == keyboard.Key.right :
                    print('Right')
                    data = b'%' #37
                if key == keyboard.Key.left :
                    print('Left')
                    data = b'^' #94
                if key == keyboard.Key.up :
                    print('Up')
                    data = b'&' #38
                if key == keyboard.Key.down :
                    print('Down')
                    data = b'*' #42
                if key == keyboard.Key.space :
                    print('Space')
                    data = b'_' #95
                #print(data)
                ser.write(data)
                #ser.write((key.char).encode())
                ser.flush()

        #def on_release(key):
            #print('Key released: {0}'.format(key))


            # Collect events until released
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()
except KeyboardInterrupt:
	ser.close()