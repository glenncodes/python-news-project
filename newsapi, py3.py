#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__credits__ = "glenncodes, seals, and newsapi.org"


import requests
import datetime
import time
from ftplib import FTP
import ctypes



counterr = 0
counter = 0

#your api key from newsapi.org
apikey = 'APIKEY'

#infinite loop
while counter == 0:
    nowww = datetime.datetime.today().strftime('%Y-%m-%d %I:%M:%S %p')
    ctypes.windll.kernel32.SetConsoleTitleW(f"Refreshed {counterr} Times") #setting title, personal thing
    try:
        def NYT():
            mainurl = f'https://newsapi.org/v2/top-headlines?sources=the-new-york-times&apiKey={apikey}'

            open_nyt_page = requests.get(mainurl).json()

            article = open_nyt_page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])

            temp = []
            toomp = []

            for i in range(len(results)):
                print("NYT", i + 1, "|", results[i])
                temp.append("NYT " + str(i + 1) + " | " + results[i] + '<pre>') #pre is used for line breaks
                toomp.append("NYT " + str(i + 1) + " | " + results[i] + '\n')
            with open('NYTArticles.html', 'w', encoding='utf-8') as output:
                output.write(f"New York Times Headlines | {nowww} EST" + '<pre>')
                output.writelines(temp)

        def Politico():

            main_url = f'https://newsapi.org/v2/top-headlines?sources=politico&apiKey={apikey}'

            open_politico_page = requests.get(main_url).json()
            article = open_politico_page["articles"]

            temp = []
            toomp = []
            results = []

            for ar in article:
                results.append(ar["title"])

            for i in range(len(results)):
                print("POL", i + 1, "|", results[i])
                temp.append("PL " + str(i + 1) + " | " + results[i] + '<pre>')#add to temp list, because directly placing to file caused issues
                toomp.append("PL " + str(i + 1) + " | " + results[i] + '\n')
            with open('PoliticoArticles.html', 'w', encoding='utf-8') as output:
                output.write(f"Politico Headlines | {nowww} EST" + '<pre>')
                output.writelines(temp)

        def BR():
            main_url = f'https://newsapi.org/v2/top-headlines?sources=bleacher-report&apiKey={apikey}'
            open_br_page = requests.get(main_url).json()
            article = open_br_page["articles"]
            temp = []
            toomp = []
            results = []

            for ar in article:
                results.append(ar["title"])

            for i in range(len(results)):
                print("BR", i + 1, "|", results[i])
                temp.append("BR " + str(i + 1) + " | " + results[i] + '<pre>')
                toomp.append("BR " + str(i + 1) + " | " + results[i] + '\n')
            with open('BleacherReportArticles.html', 'w', encoding='utf-8') as output:
                output.write(f"Bleacher Report Headlines | {nowww} EST" + '<pre>')
                output.writelines(temp)

        def Business():
            main_url = f'https://newsapi.org/v2/top-headlines?sources=business-insider&apiKey={apikey}'
            open_bi_page = requests.get(main_url).json()
            article = open_bi_page["articles"]
            temp = []
            toomp = []
            results = []

            for ar in article:
                results.append((ar["title"]))

            for i in range(len(results)):
                print("BI", i + 1, "|", results[i])
                temp.append("BI " + str(i + 1) + " | " + results[i] + '<pre>')
                toomp.append("BI " + str(i + 1) + " | " + results[i] + '\n')
            with open('BusinessInsiderArticles.html', 'w', encoding='utf-8') as output:
                output.write(f"Business Insider Headlines | {nowww} EST" + '<pre>')
                output.writelines(temp)

        def CryptoCoin():

            main_url = f'https://newsapi.org/v2/top-headlines?sources=crypto-coins-news&apiKey={apikey}'
            open_cc_page = requests.get(main_url).json()
            article = open_cc_page["articles"]
            temp = []
            toomp = []
            results = []

            for ar in article:
                results.append((ar["title"]))

            for i in range(len(results)):
                print("CC", i + 1, "|", results[i])
                temp.append("CC " + str(i + 1) + " | " + results[i] + '<pre>')
                toomp.append("CC " + str(i + 1) + " | " + results[i] + '\n')
            with open('CryptoCoinsNewsArticles.html', 'w', encoding='utf-8') as output:
                output.write(f"Crypto Coins News Headlines | {nowww} EST" + '<pre>')
                output.writelines(temp)
        print("New York Times Headlines | ", nowww, "EST")
        print("\n")
        NYT()
        time.sleep(15)
        print("\n")
        print("Politico Headlines | ", nowww, "EST")
        print("\n")
        Politico()
        time.sleep(15)
        print("\n")
        print("Bleacher Report Headlines | ", nowww, "EST")
        print("\n")
        BR()
        time.sleep(15)
        print("\n")
        print("Business Insider Headlines | ", nowww, "EST")
        print("\n")
        Business()
        time.sleep(15)
        print("\n")
        print("Crypto Coins News Headlines | ", nowww, "EST")
        print("\n")
        CryptoCoin()
        time.sleep(3)
        counterr += 1
        print("\n")

        ftp = FTP()
        ftp.set_debuglevel(2)
        ftp.connect('your server', port)
        ftp.login('username', 'password')
        ftp.cwd('directory to place in')
        fp = open("NYTArticles.html", 'rb')
        ftp.storbinary('STOR NYTArticles.html', fp)
        fp = open("BusinessInsiderArticles.html", 'rb')
        ftp.storbinary('STOR BusinessInsiderArticles.html', fp)
        fp = open("BleacherReportArticles.html", 'rb')
        ftp.storbinary('STOR BleacherReportArticles.html', fp)
        fp = open("PoliticoArticles.html", 'rb')
        ftp.storbinary('STOR PoliticoArticles.html', fp)
        fp = open("CryptoCoinsNewsArticles.html", 'rb')
        ftp.storbinary('STOR CryptoCoinsNewsArticles.html', fp)
        fp.close()
        ftp.quit()

        ctypes.windll.kernel32.SetConsoleTitleW(f"Refreshed {counterr} Times")

        time.sleep(900)




    except Exception as e:
        print(e, " Error Control ")


### First projects, messy code, thanks to newsapi