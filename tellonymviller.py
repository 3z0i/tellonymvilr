#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------
# Telegram : @realviller , @3z0i 
# Coded by vilr
# YouTube : https://youtube.com/channel/UC-z1ssGwq4Y2Rou5KNJMetA
# Instagram : https://instagram.com/3z0i?utm_medium=copy_link
# github : https://github.com/muntazir-halim
# ---------------------
import requests,random,time
ruks_ = '\033[1;36m'	
ruks__ = '\033[1;36m'
jruks = '\033[1;33m'
_ruks  = '\033[1;31m'
BGreen='\033[1;32m'
BRed ='\033[1;31m'
Number=0
class ruks:
	def __init__(self,tok,id,count):
		self.http = requests.Session()
		self.tim=time.asctime()
		self.tok = tok
		self.id = id
		self.count = count
		if self.count >10: print("="*30),print("Please write a number less than 10"),exit()
	def send_uesr(self):
		req = self.http.post(f'https://api.telegram.org/bot{self.tok}/sendMessage?chat_id={self.id}&text=⌯  HI New user!\n. — — — — —  — — — — — . \n⌯ ᴜѕᴇʀɴᴀᴍᴇ : @{self.us}\n⌯ {self.tim} \n. — — — — —  — — — — —\n• Tele : @realviler . insta: @3z0i .')
	def run(self):
		self.us = str("".join(random.choice( 'poiuytrewqasdfghjklmnbvcxz1234567890_')for i in range(self.count)))
		self.res=self.http.get(f"https://tellonym.me/{self.us}",headers={'Host': 'tellonym.me','sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'none',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document'}).status_code
		if self.res == 200:
			print(jruks+'['+BRed+f'{Number}'+jruks+'] Unavailable'+BRed+f'-[{self.us}]')
		elif self.res == 404:
			print(jruks+'['+BGreen+f'{Number}'+jruks+'] Available'+BGreen+f' [{self.us}]')
			self.send_uesr()
		else:
			print(jruks+'['+BGreen+f'{Number}'+jruks+'] erorr '+BGreen+f' [False]') 

print(f""" {jruks}
  _       _ _                             
 | |     | | |                            
 | |_ ___| | | ___  _ __  _   _ _ __ ___  
 | __/ _ \ | |/ _ \| '_ \| | | | '_ ` _ \ 
 | ||  __/ | | (_) | | | | |_| | | | | | |
  \__\___|_|_|\___/|_| |_|\__, |_| |_| |_|
                           __/ |          
                          |___/           

          {BRed}# {jruks}- {ruks_}code by viller{jruks} -{BRed} #
""")		

print("="*30)								
tok = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' TOKEN BOT ! -> ; '+BGreen)
id = input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' ID ! -> ; '+BGreen)
count = int(input(jruks+'['+_ruks+'+'+jruks+']'+ruks__+' Character count ! -> ; '+BRed))
print("="*30)
if __name__ == '__main__':
	while True:
	#	try:
		Number+=1	
		ruks(tok,id,count).run()
		#except:
#			pass