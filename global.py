#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:46:47 2020

@author: edoardottt
"""

import requests
import time
import os
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

url = "https://worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")

for x in range(0, 5):
    b = "Fetching data" + "." * x
    print(b, end="\r")
    time.sleep(0.5)

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())

feat1 = data[0].text.strip()
feat1 = feat1.replace(",", "")
print(feat1)

feat2 = data[1].text.strip()
feat2 = feat2.replace(",", "")
print(feat2)

feat3 = data[2].text.strip()
feat3 = feat3.replace(",", "")
print(feat3)


x = [int(el) for el in [feat1, feat2, feat3]]
plt.bar(["Total Cases", "Total Deaths", "Total Recovered"], x)
plt.yticks(
    np.arange(0, max(x) + 1, int(0.2 * max(x))),
    np.arange(0, max(x) + 1, int(0.2 * max(x))),
)

if not os.path.exists("GLOBAL-compared-to-yesterday"):
    os.makedirs("GLOBAL-compared-to-yesterday")

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d-%m-%Y")

title = "GLOBAL-compared-to-yesterday-" + d1 + ".png"

plt.savefig("GLOBAL-compared-to-yesterday/" + title)
plt.show()
