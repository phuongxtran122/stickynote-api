import os

def auth(pwd):
    if pwd == os.environ.get('API_KEY'):
        return True
    return False
