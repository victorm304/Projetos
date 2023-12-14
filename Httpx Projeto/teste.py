import httpx

r = httpx.post('https://httpbin.org/post', data={'key': 'value'})

print(r.url)
