from .instatalk import Talk
from .instaauth import Auth
from .instaobject import Object

import sys
import os

class INSTAGRAM(Talk, Auth, Object):

	def __init__(self, username=None, password=None, **kwargs):
		"""
		:param username: Login username. Default: None
		:param password: Login password. Default: None
		:param kwargs: See below
		:Keyword Arguments:
			- **cookie**: Instagram cookie after username & password login. Default: None
			- **settings**: A dict of settings from a previous session. Default: {}
			- **on_login**: Callback after successful login. Default: None
		:return:
		"""
		self.cookie = kwargs.pop('cookie', None)
		self.settings = kwargs.pop('settings', True)
		self.on_login = kwargs.pop('on_login', None)
		Auth.__init__(self)
		if not (username and password):
			sys.exit("Please input your username & password")
		else:
			self.login(username, password)
		self.__initAll()

	def __initAll(self):

		self.profile = self.auth.current_user()['user']
		self.user_id = self.auth.authenticated_user_id

		Object.__init__(self)
		Talk.__init__(self)
