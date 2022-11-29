import os,shutil
import time
import requests
import threading
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from cryptography.fernet import Fernet
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def get_creds():
#Getting Login
    cred filename = ‘CredFile,ini
wey file = "key. key"
eye
with open(key_ file, 'r!) as key_in:
vey = key/in.zeed() encode ()
f = Fernet (key)
wich open(cred filename, ‘x') as cred tn:
Lines = cred_in.readdines()
config = ()
for Line in Lines:
tuples = line.retrip('\n') .split('=',2)
Af tuples(0) in ('Username','Password'):
contig{tuples{0)) = tuples(?)
passwd = f.decrypt (contig( "Password! J encede()) «decode ()
recur passwd
det run()s
#scarcing Webdstver
disco = *https://discccp7 quidewell .com: 43"
chrone_options = Options()
‘chrone_options.add_argunent (*--incognito")
‘chrone_options.add_argunent (*--vebview-disable-safebrowsing-support")
‘chrone_options.add_argunent ("--disable-dev-shm-usage")
‘chrone_options.add_argunent (*--no-sandbox")
‘chrone_options.add_argunent (*--renote-debugging-port=9222")
driver = webdriver.Chrone executable path = 'C:\\Users\\32ok\\Desktop\ \devel
driver get (disco)
‘Here it will find various links to navigate. Eventually it will
find all models that do not have a "needs review" stacus and export chen
vo j
