# import librairie

import requests
import hashlib

# craft url
# ?url=https://facebook.com&h=a023cfbf5f1c39bdf8407f28b60cd134
base = 'http://challenge01.root-me.org/web-serveur/ch52/'
site_param = input('Veuillez entrer l\'url du site que vous voulez requeter : ')
encoded_site_hash = hashlib.md5(site_param.encode()).hexdigest()


url = base + '?url=' + site_param + '&h=' + encoded_site_hash

# requests the url

response = requests.get(url)
print('RESPONSE CODE : ', response.status_code)
print()
print(response.text)