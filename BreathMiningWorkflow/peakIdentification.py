import os
import sys
from tkinter import Tk
import tkinter.filedialog as fd




def peaxCommandMaker(inputDir, outputDir, paramFile):
    for inputFile in sorted(os.listdir(inputDir)):
        if os.path.isfile(os.path.join(inputDir, inputFile)):
            if "lock" not in inputFile:
                # inputFile = inputFile.split("/")[-1]
                paramFile = paramFile.split("/")[-1]
                os.popen("chmod 775 " + paramFile) #allow file to be read/open
                cmd = "./peax "+ inputDir.replace(os.getcwd()+"/","")+"/" + inputFile + " " +  outputDir.replace(os.getcwd()+"/","") + "/" + inputFile +" ./-p " + paramFile + "/"
                print(cmd)
                f = os.popen(cmd)
                now = f.read()
                print ("Results from peak Identification:", now)




# Tk().withdraw()
# ipD = fd.askdirectory()
# opD = fd.askdirectory()
# paF = fd.askopenfilename()


if __name__ == "__main__":
    peaxCommandMaker(sys.argv[1], sys.argv[2],  sys.argv[3])

# peaxCommandMaker(ipD, opD, paF)
