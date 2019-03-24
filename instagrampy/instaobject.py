# -*- coding: utf-8 -*-
from datetime import datetime
import json, time, ntpath

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.other('You want to call the function, you must login to INSTAGRAM')
    return checkLogin
    
class Object(object):

    def __init__(self):
        if self.isLogin == True:
            self.log("[%s] : Login success" % self.profile['full_name'])

    def log(self, text):
        print("[%s] %s" % (str(datetime.now()), text))

    @loggedIn
    def getRankToken(self):
        return self.auth.generate_uuid()

    @loggedIn
    def searchUser(self, query):
        result = []
        search = self.auth.search_users(query)
        for user in search['users']:
            result.append({'username': user['username'], 'full_name': user['full_name'], 'user_id': user['pk'], 'private': user['is_private']})
        result = {'num_res': search['num_results'], 'result': result}
        return result

    @loggedIn
    def postPhoto(self, path, size, caption='', disableComment=False):
    	return self.auth.post_photo(path, size, caption=caption, disable_comment=disableComment)
    	#Not Finish

    @loggedIn
    def likePost(self, url='', media_id='', code=''):
        if url:
            code = re.search(r'instagram.com/p/(.*?)/', url + '/').group(1)
            url = requests.get(f'https://www.instagram.com/p/{code}/')
            soup = BeautifulSoup(url.text, 'lxml')
            a = soup.find('body')
            b = a.find('script')
            c = b.text.strip().replace('window._sharedData =', '').replace(';', '')
            d = json.loads(c)
            f = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']['id']
            r = self.auth.post_like(f)
        if media_id:
            r = self.auth.post_like(media_id)
        if code:
            url = requests.get(f'https://www.instagram.com/p/{code}/')
            soup = BeautifulSoup(url.text, 'lxml')
            a = soup.find('body')
            b = a.find('script')
            c = b.text.strip().replace('window._sharedData =', '').replace(';', '')
            d = json.loads(c)
            f = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']['id']
            r = self.auth.post_like(f)
        return r

    @loggedIn
    def commentPost(self, text, url='', media_id='', code=''):
        if url:
            code = re.search(r'instagram.com/p/(.*?)/', url + '/').group(1)
            url = requests.get(f'https://www.instagram.com/p/{code}/')
            soup = BeautifulSoup(url.text, 'lxml')
            a = soup.find('body')
            b = a.find('script')
            c = b.text.strip().replace('window._sharedData =', '').replace(';', '')
            d = json.loads(c)
            f = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']['id']
            r = self.auth.post_comment(f, text)
        if media_id:
            r = self.auth.post_comment(media_id, text)
        if code:
            url = requests.get(f'https://www.instagram.com/p/{code}/')
            soup = BeautifulSoup(url.text, 'lxml')
            a = soup.find('body')
            b = a.find('script')
            c = b.text.strip().replace('window._sharedData =', '').replace(';', '')
            d = json.loads(c)
            f = d['entry_data']['PostPage'][0]['graphql']['shortcode_media']['id']
            r = self.auth.post_comment(f, text)
        return r

    @loggedIn
    def spamLike(self, username):
        feed = self.auth.username_feed(username)
        for media in feed['items']:
            self.auth.post_like(media['pk'])
            print(f'success like {media["pk"]}')
        print(f"liked {len(feed['items'])} items")