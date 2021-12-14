import serial
ser = serial.Serial("COM20", 9600)
print("test")

firstline = str(ser.readline())
numofP = 0
startTimeStr = ""
for i in range(len(firstline)):
    if numofP == 1:
        if(firstline[i] == '#'):
            break
        startTimeStr += firstline[i]
    if(firstline[i] == '#'):
        numofP+=1
    if numofP >= 2:
        break
print(startTimeStr) 
startTime = float(startTimeStr)/1000

def calcTime():
    time = ""
    numofP=0
    line = str(ser.readline())
    for i in range(len(line)):
        if numofP == 1:
            if(line[i] == '#'):
                break
            time += line[i]
        if(line[i] == '#'):
            numofP+=1
        if numofP >= 2:
            break
    time = float(time)/1000
    time = time-startTime
    return time

while True:
    
    print(calcTime())