import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client_id = 'f0fb5849ce315747d57c'
client_secret = '68b9badb5bcbf6f18cf18bbd7ca283e03704d5bc'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

from requests_oauthlib import OAuth2Session
github = OAuth2Session(client_id)
authorization_url, state = github.authorization_url(authorization_base_url)
print ('Please go here and authorize,', authorization_url)
redirect_response = input('Paste the full redirect URL here:')
github.fetch_token(token_url, client_secret=client_secret,
        authorization_response=redirect_response)
r = github.get('https://api.github.com/user')
print (r.content)