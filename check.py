import os
from dotenv import load_dotenv
load_dotenv()

def auth(pwd):
    if pwd == os.environ.get('API_KEY'):
        return True
    return False
