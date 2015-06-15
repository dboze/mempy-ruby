import tornado.ioloop
import tornado.httpclient

ioloop = tornado.ioloop.IOLoop.instance()

def handle_request(response):
    if response.error:
        print("Error:", response.error)
    else:
        print(response.body)

http_client = tornado.httpclient.AsyncHTTPClient()

words = ['i', 'am', 'fast']

for word in words:
  http_client.fetch("http://localhost:4567?sec=3&msg=%s" % (word), handle_request)

ioloop.start()
