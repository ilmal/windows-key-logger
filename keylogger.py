import keyboard

rk = keyboard.record(until="escape")

keyArr = []

for key in rk:
    newKey = str(key)
    if newKey.find("up") > -1:
        continue
    newKey = newKey.replace("KeyboardEvent(", "")
    newKey = newKey.replace(" down)", "")
    newKey = newKey.replace(" up)", "")
    # print(newKey)
    keyArr.append(newKey)


def openFileFunc(openFileIdx):
    try:
        fileName = "resultFile" + str(openFileIdx) + ".txt"
        f = open(fileName)
        f.close()
        #print("file Found: " + fileName)
        openFileFunc(openFileIdx + 1)
    except:
        print("File not found: " + fileName)
        f = open(fileName, "w")
        for key in keyArr:
            f.write(key + ", ")
        f.close


openFileFunc(1)
print("Program complete")
