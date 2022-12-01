# COLOR DATA PRACTICE

import json
from typing import Counter

# Load Color Data from JSON file
file = open("color-data.json", "r")
dataStr = file.read()
file.close()

color_data = json.loads(dataStr)

#1
def number1(anArray):
    for i in range(len(anArray)):
        print(anArray[i]["name"])    
        print(anArray[i]["family"])
    
#2  

def number2(anArray):
    for i in range(len(anArray)):
        brightness = anArray[i]["brightness"]
        if brightness >= 200:
            print(anArray[i]["brightness"])
            print(anArray[i]["name"])
            

#3

def number3(anArray):
    counter = 0
    for i in range(len(anArray)):
        family = anArray[i]["family"]
        if family == "Pink" or family == "Red":
            counter += 1
    print(counter)

# 4
def number4(anArray):
    counter = 0
    Userin = input("Put in Family\nr")
    print("For the family, " + Userin + ". These are the colors:")
    for i in range(len(anArray)):
        if Userin == anArray[i]["family"]:
            counter +=1 
            print(anArray[i]["name"])
    print(counter)    
        
        
#5
def number5(anArray):
   Userin = input("Please write your letter").upper()
   counter = 0 
   for i in range(len(anArray)):
    if anArray[i]["name"].startswith(Userin):
        counter += 1 
    print([anArray[i]["name"]])
    print(counter)

