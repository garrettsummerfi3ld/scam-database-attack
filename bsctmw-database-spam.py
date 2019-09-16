#!python3
import requests
import random
import string

def randomString(stringLength=10):
	"""Generate a random string of fixed length """
	letters = string.ascii_lowercase+string.ascii_uppercase+string.digits
	return ''.join(random.choice(letters) for i in range(stringLength))

cookies = {
#	'__ddg_': '856806E1D761B35E7BE4173938CABFA9052143F6',
#	'_csrf': 'tAgle4ZPqH5PysmmkuZtYtDZ',
#	'XSRF-TOKEN': 'J2vg9DJs-jEQX97cQKqq-3VqUvX95KKp6h64',
#	'connect.sid': 's%3Aheppfz0bgX8TALAmhlM5gVfFuToKzYd5.zcvVtjQKgHehDXUb9fTSYATM1Ocafaer9luITzifKgE',
#	'item': '{name:Karambit | Crimson Web,quality:Minimal Wear,img:https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf2PLacDBA5ciJnJm0gPL2IITdn2xZ_Pp9i_vG8MKj2Qbl_EdlZziiddOXdAY2YAvT-wW2xrjugJG_tcvNyyBn6SEm4XuMgVXp1n8qZn5H/360fx360f}',
#	'img': 'https://steamcommunity-a.akamaihd.net/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpovbSsLQJf2PLacDBA5ciJnJm0gPL2IITdn2xZ_Pp9i_vG8MKj2Qbl_EdlZziiddOXdAY2YAvT-wW2xrjugJG_tcvNyyBn6SEm4XuMgVXp1n8qZn5H/360fx360f',
#	'name': 'Karambit | Crimson Web (Minimal Wear)',
	'human': 'yes',
}

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

print('Spamming "bsctmw.com" database...')
print('Headers used to attack the offending db:\n{}'.format(headers))
print('Cookies used to attack the offending db:\n{}'.format(cookies))

while True:

	username = randomString(random.randrange(12,20,1))
	password = randomString(random.randrange(12,20,1))

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
	
	print('Params used to attack offending db:\n{}' .format(params))

	print('Logging in with:\n- user     : {}\n- password : {}'.format(username, password))

	response = requests.post('https://bsctmw.com/uncheck2', headers=headers, cookies=cookies, params=params)
	
	print('Response from server: {}'.format(response.status_code))