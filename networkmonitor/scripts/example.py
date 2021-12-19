#!/usr/bin/python3

import subprocess
import time

arg1 = "192.168.1.117"
arg2 = "root"

results = []
for i in range(0, 60, 5):
    subprocess.call(f"./getScript.bash {arg1} {arg2}", shell=True)
    f = open("./output.txt","r")
    list = f.read().split(" ")
   
    results.append(int(list[3]))
    results.append(int(list[7]))
    results.append(int(list[11]))
    if len(results) > 3:
        lenResult = len(results)
        deltaIn = abs(results[lenResult -3 ] - results[lenResult - 6])
        deltaOut = abs(results[lenResult -2 ] - results[lenResult - 5])
        results.pop(0)
        results.pop(1)
        results.pop(2)

        print("Gelen :")
        print((deltaIn * 8 * 100) / (i * lenResult -1 ))
        print("Giden")
        print((deltaOut * 8 * 100) / (i * lenResult -1))
        print("Half")
        print(((deltaIn + deltaOut) * 8 * 100) / (i * lenResult - 1))
        print("Full")
        print((max(deltaIn, deltaOut) * 8 * 100) / (i * lenResult - 1))
        print("\n\n")
    time.sleep(5)

