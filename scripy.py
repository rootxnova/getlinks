from bs4 import BeautifulSoup
from colored import fg, bg, attr
import requests
color1 = fg('#f1c40f')
color2 = fg('#d35400')
print(color2+'''
   _____   ______   _______   _        _____   _   _   _  __   _____ 
  / ____| |  ____| |__   __| | |      |_   _| | \ | | | |/ /  / ____|
 | |  __  | |__       | |    | |        | |   |  \| | | ' /  | (___  
 | | |_ | |  __|      | |    | |        | |   | . ` | |  <    \___ \ 
 | |__| | | |____     | |    | |____   _| |_  | |\  | | . \   ____) |
  \_____| |______|    |_|    |______| |_____| |_| \_| |_|\_\ |_____/ 
                                                                     

                - CODED BY ABDELRAHMAN ABOULDAHAB -

''')
url = input(color1+" - Enter Website Link To Extract Links : ")
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')
for link in soup.find_all('a'):
    a = link.get('href')
    with open('Links.txt',mode="a+") as f:
        f.write(a+'\n')

print('==========[ S A V E D ]==========')

close = input(' >>> Press Enter To Close Script <<< ')
