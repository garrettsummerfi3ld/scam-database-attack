#!/usr/bin/python3

import requests
import logging
import random
import os

# Logging config
logging.basicConfig(level=logging.INFO,
					filemode='w',
					format=('%(asctime)s - %(levelname)s - ' +
					'%(funcName)s - %(message)s'),
					datefmt='%d-%m-%y %H:%M:%S')
logging.getLogger().addHandler(logging.StreamHandler())

# Generates random string
def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_lowercase+string.ascii_uppercase+string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

# Connection headers
headers = {
	'Host': 'skinamerica.fun',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Referer': 'https://skinamerica.fun/auth/',
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

logging.info('Spamming "skinamerica.fun" database...')
logging.debug('Headers used to attack the offending db:')
for h in headers:
	logging.debug(h)

logging.debug('Cookies used to attack the offending db:')
for c in cookies:
	logging.debug(c)


while True:

	username = randomString(random.randrange(12,20,1))
	password = randomString(random.randrange(12,20,1))

	# Connection parameters
	params = {
	'emailauth': '',
	'emailsteamid': '',
	'loginfriendlyname': '',
	'login': username,
	'domain': 'skinamerica.fun',
	'_csrf': 'k2hy76jh-JOGwlBDHExj2q0NpNa6AqKWX17o',
	'password': password,
	'captchagid': '-1',
	'captcha_text': ''
	}

	logging.debug('Params used to attack offending db:')
	for p in params:
		logging.debug(p)
	
	logging.info('Logging in with:\n- user     : {}\n- password : {}'.format(username, password))

	# Sending and receiving connection from server that is being attacked
	# This is defined as a HTTP responce code
	response = requests.post('https://skinamerica.fun/auth', headers=headers, cookies=cookies, params=params)
	
	logging.info('Response from server: {}'.format(response.status_code))