import tornado.httpclient

http_client = tornado.httpclient.HTTPClient()

words = ['i', 'am', 'fast']

for word in words:
  response = http_client.fetch("http://localhost:4567?sec=3&msg=%s" % (word))
  if response.error:
      print("Error:", response.error)
  else:
      print(response.body)
