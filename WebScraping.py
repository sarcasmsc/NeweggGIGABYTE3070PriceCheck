from bs4 import BeautifulSoup
import re
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3070-gv-n3070gaming-oc-8gd/p/N82E16814932449"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text='$')
parent = prices[0].parent
strong = parent.find('strong')
weak = parent.find('sup')
gpuprice = strong.string + weak.string
gpu = 'GIGABYTE Gaming OC GeForce RTX 3070 8GB'

#tags = doc.find_all(text=re.compile('\$.*')) #couldn't figure out how to get this to work yet
#for tag in tags:
#    print(gpu + tag.strip())

print(gpu)
print('$' + gpuprice)