import numpy as np
from PIL import Image
import random
import copy
"""
Wiederverwendbare Funktionen
"""
def readFile(path):
    f = open(path)
    content = None
    with open(path) as f:
        content = f.read()
        f.close()
    return content

def writeFile(path, content):
    with open(path, "w") as f:
        f.write(content)
        f.close()

def modifyFile(path):
    content = readFile(path)
    newContent = "".join(map(lambda c: chr(ord(c) + 1), content))
    writeFile(path, newContent)
    print("The new content has been written to the same file.")

def connect(path1, path2):
    content1 = readFile(path1)
    content2 = readFile(path2)
    mergedContent = content1 + "\n" + content2
    writeFile("./data/aufgabenblatt_4_a18.txt", mergedContent)

def countColors(path):
    img = Image.open(path, 'r')
    img.load()
    data = np.asarray( img, dtype="int32" )
    dataMostFrequented = {}
    for row in data:
        for pixel in row:
            key = tuple(pixel)
            if not key in dataMostFrequented:
                dataMostFrequented[key] = 1
            else:
                dataMostFrequented[key] += 1
    return data, dataMostFrequented

def saveImageFromArray(path, data):
    img = Image.fromarray(np.uint8(data))
    img.save(path)
    print(f"New image saved to {path}")

def createFromTopColors(data, dataMostFrequented, topCount):
    print(f"Bitte warten... Bild wird erstellt (Top {topCount})")
    sortedData = sorted(dataMostFrequented, key=dataMostFrequented.get, reverse=True)
    fastSearchData = set(sortedData[:topCount])
    for x in range(len(data)):
        for y in range(len(data[x])):
            curPixel = tuple(data[x][y])
            if curPixel not in fastSearchData:
                randomPixel = sortedData[random.randint(0, topCount - 1)]
                data[x][y] = np.asarray(randomPixel)
    saveImageFromArray(f"./data/aufgabenblatt_4_a19_top_{topCount}.jpg", data)

def mergeImages(data1, data2, path):
    print("Merging images, please wait...")
    newData = copy.deepcopy(data1)
    for x in range(len(newData)):
        for y in range(len(newData[x])):
            if x % 2 == 0:
                newData[x][y] = np.asarray(data2[x][y])
    saveImageFromArray(path, newData)
"""
Aufgaben Funktionen
"""
def aufgabe16():
    print("----- Aufgabe 16 ------")
    content = readFile("./data/aufgabenblatt_4_a16.txt")
    print(content)
    print("")

def aufgabe17():
    print("----- Aufgabe 17 ------")
    modifyFile("./data/aufgabenblatt_4_a17.txt")
    print("")

def aufgabe18():
    print("----- Aufgabe 18 ------")
    path1 = "./data/aufgabenblatt_4_a16.txt"
    path2 = "./data/aufgabenblatt_4_a17.txt"
    connect(path1, path2)
    print(f"File {path1} has been merged together with file {path2}")
    print(f"Merged file: ./data/aufgabenblatt_4_a18.txt")
    print("")

def aufgabe19():
    print("----- Aufgabe 19 ------")
    data, dataMostFrequented = countColors("./data/tom_and_jerry.jpg")
    createFromTopColors(copy.deepcopy(data), dataMostFrequented, 10)
    # Aus reiner Interesse wurde der Top Count erhöht, um zu schauen ob das Bild ähnlich wie das Originalbild ist.
    # Gemäss Kombinatorik, existieren 255x255x255 mögliche Farbkombinationen also 255^3 = 16'581'375 RGB Farben
    createFromTopColors(copy.deepcopy(data), dataMostFrequented, 100)
    createFromTopColors(copy.deepcopy(data), dataMostFrequented, 1000)
    createFromTopColors(copy.deepcopy(data), dataMostFrequented, 5000)
    print("")

def aufgabe20():
    print("----- Aufgabe 20 ------")
    nyan_cat, _ = countColors("./data/nyan_cat.jpg")
    spongebob_fish, _ = countColors("./data/spongebob_fish.jpg")
    tom_and_jerry, _ = countColors("./data/tom_and_jerry.jpg")
    mergeImages(nyan_cat, spongebob_fish, "./data/aufgabenblatt_4_a20_bsp1.jpg")
    mergeImages(nyan_cat, tom_and_jerry, "./data/aufgabenblatt_4_a20_bsp2.jpg")
    mergeImages(tom_and_jerry, spongebob_fish, "./data/aufgabenblatt_4_a20_bsp3.jpg")
    print("")

if __name__ == "__main__":
    aufgabe16()
    aufgabe17()
    aufgabe18()
    aufgabe19()
    aufgabe20()
