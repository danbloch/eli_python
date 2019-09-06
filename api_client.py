import requests

def getToken(user, password):
    credentials = {'username':user, 'password':password}
    return requests.post('https://api.europace.de/login', data=credentials)
