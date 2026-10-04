import requests as rq

Payload = {"key1":"value1", "key2":"value2", "key3":["value3", "value4", "value5"]}
r = rq.get("https://httpbin.org/get", Payload)

print(r.url)