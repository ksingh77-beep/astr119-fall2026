import requests
import time
url = input('Enter a URL to poke: ')
t_start=time.time()
response = requests.get(url)
t_end=time.time()
nbytes = len(response.content)
d=t_end-t_start
rate=nbytes/(1e6*d)
print(f"{nbytes} bytes read from {url}")
print(f"Download took {d:.2f}s and rate {rate:.2f} MB/s")