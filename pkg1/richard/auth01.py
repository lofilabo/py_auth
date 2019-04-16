import pprint

import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client_id = r'903166010095-itita8nbn6g3l39um4uvhotje13bp9no.apps.googleusercontent.com'
client_secret = r'XE-YCrH_hYtKXtK5jZ3mic-U'
redirect_uri = 'http://p4nd4.net/oauth2_incm'
import requests
from requests_oauthlib import OAuth2Session
scope = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
authorization_url, state = oauth.authorization_url('https://accounts.google.com/o/oauth2/auth', access_type="offline", prompt="select_account")
print (state)
print (authorization_url)

authorization_response = input('Enter the full callback URL')
token = oauth.fetch_token('https://accounts.google.com/o/oauth2/token', authorization_response=authorization_response, client_secret=client_secret)

pprint.pprint(token)

#token = oauth.fetch_token('https://accounts.google.com/o/oauth2/token',authorization_response=authorization_response,client_secret=client_secret)
r = oauth.get('https://www.googleapis.com/oauth2/v1/userinfo')
pprint.pprint(r)