import requests
import random
import string

r = ''
while r != '404':
    r = requests.get('https://recarga.nequi.com.co/manifest.json')
    #print(r.status_code)
    letters = string.ascii_lowercase
    print(''.join(random.choice(letters) for i in range(10)))
print('service available!!!')