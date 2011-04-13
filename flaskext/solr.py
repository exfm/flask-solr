import pysolr


# json logic from pysolr, to expose pysolr.Solr constructor API in Flask-Solr.
try:
    # For Python < 2.6 or people using a newer version of simplejson
    import simplejson as json
except ImportError:
    # For Python >= 2.6
    import json


EXTENSION_KEY = 'solr'


class Solr(object):
    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def __getattr__(self, name):
        return getattr(self.connection, name)

    def init_app(self, app):
        self.app = app
        self.app.config.setdefault('SOLR_URL', 'http://localhost:8983/solr')
        self.app.config.setdefault('SOLR_DECODER', json.JSONDecoder())
        self.app.config.setdefault('SOLR_TIMEOUT', 60)
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions[EXTENSION_KEY] = self.connect()

    def connect(self):
        url = self.app.config['SOLR_URL']
        decoder = self.app.config['SOLR_DECODER']
        timeout = self.app.config['SOLR_TIMEOUT']
        return pysolr.Solr(url, decoder=decoder, timeout=timeout)

    def raise_init_error(self, message=None):
        msg = 'Flask-Solr instance not properly initialized'
        if message is not None:
            msg += ': ' + message
        raise RuntimeError(msg)

    @property
    def connection(self):
        if self.app is None:
            self.raise_init_error('no app given -- call init_app(app) first.')
        if not hasattr(self.app, 'extensions'):
            self.raise_init_error('app does not have extensions namespace.')
        if EXTENSION_KEY not in self.app.extensions:
            self.raise_init_error('not in app extensions dict.')
        return self.app.extensions[EXTENSION_KEY]
