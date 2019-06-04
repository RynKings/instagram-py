import os, sys, json, codecs
from datetime import datetime
try:
	from instagram_private_api import Client, ClientError
except ImportError:
	python = sys.executable
	os.system(f'{python} -m pip install git+https://git@github.com/ping/instagram_private_api.git --upgrade --force-reinstall')
	os.execl(python, python, *sys.argv)

def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable') 

def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object

def onlogin_callback(api, new_settings_file):
    cache_settings = api.settings
    with open(new_settings_file, 'w') as outfile:
        json.dump(cache_settings, outfile, default=to_json, indent=4)
        print('SAVED: {0!s}'.format(new_settings_file))

class Auth(object):
	isLogin = False

	def __init__(self):
		return

	def __loadSession(self, cl):
		self.auth = cl
		self.isLogin = True

	def login(self, username, password):
		if self.settings:
			if 'settings_session.json' not in os.listdir():
				self.cl = Client(username, password, cookie=self.cookie, on_login=lambda x: onlogin_callback(x, 'settings_session.json'))
				print("[%s] [%s] : Save settings_session.json success" % (str(datetime.now()), self.cl.current_user()['user']['full_name']))
			else:
				self.cl = Client(username, password, cookie=json.load(open('settings_session.json'), object_hook=from_json).get('cookie'), settings=json.load(open('settings_session.json'), object_hook=from_json))
				print("[%s] [%s] : Load settings_session.json success" % (str(datetime.now()), self.cl.current_user()['user']['full_name']))
		else:
			self.cl = Client(username, password, cookie=self.cookie)
		self.token = self.cl.csrftoken
		self.userAgent = self.cl.user_agent
		self.cookie = self.cl.cookie_jar
		self.__loadSession(self.cl)
