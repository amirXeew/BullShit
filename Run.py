import os 
import time 
import colorama
import sys 
import requests
import string
import random
#################### Colors ###################
colorama.init()
lRED = colorama.Fore.LIGHTRED_EX
lBLUE = colorama .Fore.LIGHTBLUE_EX 
lYeLLOW = colorama.Fore.LIGHTYELLOW_EX 
lGREEN = colorama.Fore.LIGHTGREEN_EX
lCYAN = colorama.Fore.LIGHTCYAN_EX
lMAGRNTA = colorama.Fore.LIGHTMAGENTA_EX
red = colorama.Fore.RED
blue = colorama.Fore.BLUE
yellow = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN
green = colorama.Fore.GREEN 
white = colorama.Fore.WHITE
rest = colorama.Fore.RESET
color_TEXT = [lBLUE,lRED,lYeLLOW,lGREEN,lCYAN,lMAGRNTA,red,blue,yellow,cyan,green]
#################### Print slow ###################
def print_slow(text):
    for letter in text:
        colors = random.choice(color_TEXT) 
        sys.stdout.write(f'{colors}{letter}')
        sys.stdout.flush()
        time.sleep(0.1)
########                         
def print_slow_in(text):
    for letter in text:
        sys.stdout.write(f'{letter}')
        sys.stdout.flush()
        time.sleep(0.1)
    result = input() 
    return result
def print_colors(text):
    for letter in text:
        colors = random.choice(color_TEXT)
        sys.stdout.write(f'{colors}{letter}')

##################### bannetr ######################
def banners(): 
    try: os.system('cls')
    except: os.system('clear')
    time.sleep(0.2)
    print(f'''{red}
 ▄▄▄▄    █    ██  ██▓     ██▓      ██████  ██░ ██  ██▓▄▄▄█████▓
▓█████▄  ██  ▓██▒▓██▒    ▓██▒    ▒██    ▒ ▓██░ ██▒▓██▒▓  ██▒ ▓▒{yellow}{rest}Created by me :){yellow}
▒██▒ ▄██▓██  ▒██░▒██░    ▒██░    ░ ▓██▄   ▒██▀▀██░▒██▒▒ ▓██░ ▒░ {rest} Version 1.0 {yellow}
▒██░█▀  ▓▓█  ░██░▒██░    ▒██░      ▒   ██▒░▓█ ░██ ░██░░ ▓██▓ ░ {green}
░▓█  ▀█▓▒▒█████▓ ░██████▒░██████▒▒██████▒▒░▓█▒░██▓░██░  ▒██▒ ░ 
░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░▓  ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓    ▒ ░░   {cyan}
▒░▒   ░ ░░▒░ ░ ░ ░ ░ ▒  ░░ ░ ▒  ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░    ░    
 ░    ░  ░░░ ░ ░   ░ ░     ░ ░   ░  ░  ░   ░  ░░ ░ ▒ ░  ░      {blue}
 ░         ░         ░  ░    ░  ░      ░   ░  ░  ░ ░           
      ░                                                        
''')
    time.sleep(0.3)

    print(red+f'    Git{white}hub:',end='')
    time.sleep(0.2)                                 
    print_slow('https://github.com/amirXeew \n\n\n') 
    time.sleep(0.3)
    print(f"{red}[{green}1{red}]{white}Create Random Account    {red}[{green}2{red}]{white}Create Private Account\n")
    time.sleep(0.1)
    print_colors("****************************************************\n\n\n")
    time.sleep(0.4)
    print(f'''{red}┌─{white}[{yellow}!{white}]{white} Select An Option
{red}└──╼{rest}''',end=' ')
######################### data ##########################
url = "https://spclient.wg.spotify.com/signup/public/v1/account"
headers = {
  'authority': 'spclient.wg.spotify.com',
  'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'content-type': 'application/x-www-form-urlencoded',
  'accept': '*/*',
  'origin': 'https://www.spotify.com',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.spotify.com/',
  'accept-language': 'en-US,en;q=0.9'
}
addEmails = ['gmail.com', 'yahoo.com', 'hotmail.com', 'hotmail.co.uk', 'hotmail.fr', 'outlook.com', 'icloud.com', 'mail.com', 'live.com', 'yahoo.it', 'yahoo.ca', 'yahoo.in', 'live.se', 'orange.fr', 'msn.com', 'mail.ru', 'mac.com']

###################### Information #######################
def ran_char(letter):
       return ''.join(random.choice(string.ascii_letters) for words in range(letter))
a = True
banners()
Option = input()
##########################################################
if Option == "1" :
    a = False
    Count = eval(input(f"{red}[{green}!{red}]{white} Amount to create:╼ "))
    def Email():
        return '%s@%s' % (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(7, 10))), random.choice(addEmails))
    def Password():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(8, 12)))
    def Username():
        return ran_char(12)+"AmirXeew"
    def Day():
        return random.randint(1, 28)
    def Month():
        return random.randint(1, 12)
    def Year():
        return random.randint(1970,2002)
    def Gender():
        return random.choice(["male","female"])

elif Option == "2" :
    Count = 1
    email = input("Enter your email :")
    password = input("Enter your password :")
    username = input("Enter your user name :")
    day = eval(input ("Enter a day :"))
    month = eval(input("Enter a month :"))
    year = eval(input("Enter a year :"))
    gender = input("Enter a Gender (male) (female) :")

#########################################################
num = 0 
File_Path=input(f"  {red}[{green}!{red}] {white}Enter Your Proxies Path :")
while num != Count:
    if a == False :
        email = Email()
        password = Password()
        username = Username()
        day = Day()
        month = Month()
        year = Year()
        gender = Gender()
    data = 'creation_point=lite_7e7cf598605d47caba394c628e2735a2&password_repeat=%s&platform=Android-ARM&iagree=true&password=%s&gender=%s&key=a2d4b979dc624757b4fb47de483f3505&birth_day=%s&birth_month=%s&email=%s&birth_year=%s' % (password, password, gender,day,month, email,year)
    with open(File_Path, 'r') as f:
        for linesa in f.read().splitlines():
            try:
                create = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account', data = data, headers = headers, proxies = {'https': 'HTTP://%s' % (linesa)}, timeout = 5)
                print(f"{red}[{white}AmirXeew{red}]{blue}Email:{email}:{cyan}{password}{white}|Username:{yellow}{username}{white}|{green}{year}/{month}/{day}{rest}")
                with open("Account.txt","a") as s:
                    s.write(f"{email}:{password}|{username}|{year}/{month}/{day}\n")
                num+=1
                break
            except : pass
input("Finished ... . ",)
