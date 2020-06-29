import requests
from bs4 import BeautifulSoup
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do')