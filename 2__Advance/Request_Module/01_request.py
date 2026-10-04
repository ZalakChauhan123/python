import requests as req

# Make a GET request
r = req.get("https://www.codewithharry.com")
print(r.text)
print(r.status_code)
print(r.headers)
print(r.json())
