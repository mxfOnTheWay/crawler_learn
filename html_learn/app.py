import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('get111')
        u=self.get_argument('name')
        p = self.get_argument('pwd')
        if u=='abc' and p=='123':
            self.write('ok')
        else:
            self.write('gun')
        self.write("Hello, world")
    def post(self, *args, **kwargs):
        print('post123')
        self.write('post')

application = tornado.web.Application([
    (r"/index", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()