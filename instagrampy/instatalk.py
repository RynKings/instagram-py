import requests, json
from bs4 import BeautifulSoup

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to INSTAGRAM')
    return checkLogin

class Talk(object):
	isLogin = False

	def __init__(self):
		self.isLogin = True

	"""
	user
	"""

	@loggedIn
	def getUserInfo(self, username):
		return self.auth.username_info(username)

	@loggedIn
	def getUserId(self, username):
		return self.auth.username_info(username)['user']['pk']

	@loggedIn
	def getName(self, username):
		return self.auth.username_info(username)['user']['full_name']

	@loggedIn
	def getProfilePicture(self, username):
		return self.auth.username_info(username)['user']['profile_pic_url']

	@loggedIn
	def getFollowers(self, username):
		user_id    = self.getUserId(username)
		rank_token = self.getRankToken()
		return self.auth.user_followers(user_id, rank_token)

	@loggedIn
	def getFollowing(self, username):
		user_id    = self.getUserId(username)
		rank_token = self.getRankToken()
		return self.auth.user_following(user_id, rank_token)

	@loggedIn
	def getFollowersUsername(self, username):
		user_foll = self.getFollowers(username)
		username  = []
		for user in user_foll['users']:
			username.append(user['username'])
		return username

	@loggedIn
	def getFollowingUsername(self, username):
		user_foll = self.getFollowing(username)
		username  = []
		for user in user_foll['users']:
			username.append(user['username'])
		return username

	@loggedIn
	def getFollowersUserId(self, username):
		user_foll = self.getFollowers(username)
		user_id   = []
		for user in user_foll['users']:
			user_id.append(user['pk'])
		return user_id

	@loggedIn
	def getFollowingUserId(self, username):
		user_foll = self.getFollowing(username)
		user_id   = []
		for user in user_foll['users']:
			user_id.append(user['pk'])
		return user_id

	@loggedIn
	def editProfile(self, name, bio, link, email, phone_num, gender):
		#Email Required
		#Gender 1. Male 2. Female 3.Bencong
		return self.auth.edit_profile(name, bio, link, email, phone_num, gender)

	@loggedIn
	def cekUsername(self, username):
		return self.auth.check_username(username)

	"""
	Friend
	"""

	@loggedIn
	def followUser(self, username):
		user_id = self.getUserId(username)
		return self.auth.friendships_create(user_id)

	@loggedIn
	def unfollowUser(self, username):
		user_id = self.getUserId(username)
		return self.auth.friendships_destroy(user_id)

	@loggedIn
	def blockUser(self, username):
		user_id = self.getUserId(username)
		return self.auth.friendships_block(user_id)

	@loggedIn
	def unblockUser(self, username):
		user_id = self.getUserId(username)
		return self.auth.friendships_unblock(user_id)

	@loggedIn
	def unblockStorySeens(self, username):
		user_id = self.getUserId(username)
		return self.auth.unblock_friend_reel(user_id)

	@loggedIn
	def blockStorySeens(self, username):
		user_id = self.getUserId(username)

	@loggedIn
	def deleteFollowers(self, username):
		user_id = self.getUserId(username)
		return self.auth.remove_follower(user_id)

	"""
	settings
	"""

	@loggedIn
	def setToPublic(self):
		#Make Your Account to Public
		return self.auth.set_account_public()

	@loggedIn
	def setToPrivate(self):
		#Make Your Account to Private
		return self.auth.set_account_private()

	@loggedIn
	def deleteProfilePicture(self):
		#Delete Your Picture Profile
		return self.auth.remove_profile_picture()
