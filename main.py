import re
import requests

start_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

response = requests.get(start_url)
if response.status_code == 200:
    patt = re.compile(r'<a href="([^"]+)"')
    for parsed_url in patt.finditer(response.content.decode('utf-8')):
        print(parsed_url.groups()[0])
