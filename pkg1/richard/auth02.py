import pprint
import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import LegacyApplicationClient
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client_id = 'f0fb5849ce315747d57c'
client_secret = '68b9badb5bcbf6f18cf18bbd7ca283e03704d5bc'
username = 'lofilabo'
password = 'hyper71130'

"""
client_id = '903166010095-itita8nbn6g3l39um4uvhotje13bp9no.apps.googleusercontent.com'
client_secret = 'XE-YCrH_hYtKXtK5jZ3mic-U'
username = 'richardlofi@gmail.com'
password = 'your_password'
"""
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'


client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, client_id=client_id,
        client_secret=client_secret)