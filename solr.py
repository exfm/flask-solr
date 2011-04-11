from flask import _request_ctx_stack
import pysolr


class Solr(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        self.app = app
        self.app.config.setdefault('SOLR_URL', 'http://localhost:8983/solr')
        self.app.after_request(self.after_request)
        self.app.before_request(self.before_request)

    def connect(self):
        return pysolr.Solr(self.app.config['SOLR_URL'])

    def before_request(self):
        ctx = _request_ctx_stack.top
        ctx.solr = self.connect()

    def after_request(self, response):
        ctx = _request_ctx_stack.top
        del ctx.solr
        return response

    @property
    def connection(self):
        ctx = _request_ctx_stack.top
        if ctx is not None:
            return ctx.solr
