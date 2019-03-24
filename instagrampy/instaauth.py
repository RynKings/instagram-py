try:
	from instagram_private_api import Client, ClientError
except ImportError:
	python = sys.executable
	os.system(f'{python} install git+https://git@github.com/ping/instagram_private_api.git --upgrade --force-reinstall')
	os.execl(python, python, *sys.argv)

class Auth(object):
	isLogin = False

	def __init__(self):
		return

	def __loadSession(self, cl):
		self.auth = cl
		self.isLogin = True

	def login(self, username, password):
		self.cl = Client(username, password)
		self.token = self.cl.csrftoken
		self.userAgent = self.cl.user_agent
		self.cookie = self.cl.cookie_jar
		self.__loadSession(self.cl)
