import urllib.request as ur
import json

# json_url = 'http://py4e-data.dr-chuck.net/comments_66573.json'

url = input("Enter location: ")
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
obj = json.loads(data)

sum = 0
number = 0

for comment in obj["comments"]:
    sum += int(comment["count"])
    number += 1

print('Count:', number)
print('Sum:', sum)
