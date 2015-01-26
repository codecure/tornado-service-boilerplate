#!/usr/bin/env python
# coding: utf-8

from tornado import web, httpserver, ioloop
from service import configuration
from service import __project_name__, __app_version__

DEFAULT_PORT = 8383
conf = configuration.load_configuration()
app_port = conf['app'].get('port', DEFAULT_PORT)


class Application(web.Application):
    def __init__(self):
        self.conf = conf

        handlers = (
            # (r'/', MainHandler),
        )
        super(Application, self).__init__(handlers=handlers)

if __name__ == "__main__":
    http_server = httpserver.HTTPServer(Application())
    http_server.listen(app_port)
    print '%s (build %s) started on %s port' % (__project_name__,
                                                __app_version__, app_port)
    ioloop.IOLoop.instance().start()