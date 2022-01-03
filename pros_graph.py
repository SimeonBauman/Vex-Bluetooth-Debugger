import serial
import timeit
from matplotlib import pyplot as plt
#i need to create a somthing to determin the best arangment x , y of the graphs
ser = serial.Serial("COM20", 9600)
print("test")
startTime = timeit.default_timer()
firstline = str(ser.readline())
plt.ion()
numsOfGraphs = 4
fig = plt.figure(figsize = (2.5*numsOfGraphs,numsOfGraphs))


x = []
y = []
doing = True

def calcTime():
    return timeit.default_timer() - startTime
    
def GetVals():
    lineStr = str(ser.readline())
    numOfHa = 0
    
    num = ""
    for i in range(len(lineStr)):
        if numOfHa == 1 and lineStr[i] != "#":
            num += lineStr[i]
        if(lineStr[i] == '#'):
            if numOfHa == 1:
                numOfHa = 2
            elif numOfHa == 0:
                numOfHa = 1
        if(numOfHa >= 2):
            break
        
    print(num)
    return float(num)

while True:
    
    for i in range(numsOfGraphs):
        y.append(GetVals())
        x.append(calcTime())
        plt.subplot(1,numsOfGraphs,i+1).clear()
        plt.subplot(1,numsOfGraphs,i+1)
        plt.plot(x,y)
        plt.draw()
        plt.pause(0.0001)
        
      
    
    