#coding=utf-8

#!/usr/bin/python2

import os 

import sys

import base64

import random

import requests

import platform

#module 

def Token_token():

	os.system("clear")	print logo

	print("")

	try:

		tok = open('/sdcard/Download/.ferdous-ok.txt', 'r').read()

		dec = base64.b64decode(tok)

		if len(dec) < 50:

		 https://pastebin.com/raw/3FZ9HwGa").text

		if dec in r:

			main() #add your main menu when payment sucess

		else:

		    print('\t  \033[1;91m YOUR  Token_token  IS NOT  APPROVED :(').center(50)

		    print("")

		    print('\033[1;93m Your Token_token : \033[1;92m'+dec+'\n\n\n')

		    raw_input("  \t  \033[1;93m Press enter to check again ")

		    not_reg()

	except (IOError):

	    not_reg()

	except requests.exceptions.ConnectionError:

	    print('\n\n\nTurn on mobile data OR wifi to continue\n\n')

	    sys.exit()

	

def not_reg():

    print('\n\n\nVerify your Token_token\n\n\n')

    string_Token_token = 'abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    v_Token_token = ''.join((random.choice(string_Token_token)) for x in range(50))

    v_Token_token_save = open('/sdcard/Download/.ferdous-ok.txt', 'w')

    v_Token_token_save.write(base64.b64encode(v_Token_token))

    v_Token_token_save.close()

    print('\033[1;93m Your Token_token : \033[1;92m' + v_Token_token)

    print("")

    print("")

    raw_input("  \t  \033[1;93m Press enter to check again ")

    os.system('xdg-open https://wa.me/+923079321417') #whatsapp number here

    Token_token()

    
