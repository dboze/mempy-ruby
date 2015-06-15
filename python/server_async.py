import tornado.ioloop
import tornado.web
from tornado import gen

class NapHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        args = self.request.arguments
        yield gen.sleep(float(args["sec"][0]))
        self.write(args["msg"][0])

application = tornado.web.Application([
    (r"/", NapHandler),
])

if __name__ == "__main__":
    application.listen(4567)
    tornado.ioloop.IOLoop.current().start()
