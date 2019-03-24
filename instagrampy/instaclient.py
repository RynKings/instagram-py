from .instatalk import Talk
from .instaauth import Auth
from .instaobject import Object

class INSTAGRAM(Talk, Auth, Object):

	def __init__(self, username, password):
		Auth.__init__(self)
		self.login(username, password)
		self.__initAll()

	def __initAll(self):

		self.profile = self.auth.current_user()['user']
		self.user_id     = self.auth.authenticated_user_id

		Object.__init__(self)
		Talk.__init__(self)