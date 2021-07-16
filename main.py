import requests
import time
from keep_alive import keep_alive
import setup

keep_alive()
while True:
  for bot_url in setup.bot_urls:
    requests.head(bot_url, allow_redirects=True)
    print('Pinged: ' + bot_url)
  time.sleep(setup.timeout*60)

 