import requests

def getToken(user, password):
    credentials = {'username':user, 'password':password}
    r = requests.post('https://api.europace.de/login', data=credentials)
    if r.status_code/100==2:
        token=r.json()['access_token']
        loginSuccessful = True
    else:
        token=""
        loginSuccessful = False
    return token, loginSuccessful
