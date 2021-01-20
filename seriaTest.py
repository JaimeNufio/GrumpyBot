from serial import Serial
# "COM11" is the port that your Arduino board is connected.set it to port that your are using        
ser = Serial("COM5", 9600)
while True:
    cc=str(ser.readline())
    print(cc[2:][:-5])   