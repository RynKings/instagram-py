from instagrampy import *
import sys

username = ''
password = ''

cl = INSTAGRAM(username, password)
profile = cl.profile
print(profile)