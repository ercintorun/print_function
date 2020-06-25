import time
timestr = time.strftime("%Y%m%d-%H%M%S")
OutputFile= "output"+str(timestr)+".txt"
OF = open(OutputFile, 'w')

def printing(text):
    print (str(text))
    if outputFile:
        OF.write(text + "\n")
