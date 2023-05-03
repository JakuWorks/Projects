import urllib.request
from time import sleep

print('---------- START ----------')

print(urllib.request.urlopen('https://www.example.com').read())

print('---------- END ----------')