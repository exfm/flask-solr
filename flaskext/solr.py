import pysolr

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
        self._connection = None
        self.app = app
        self.app.config.setdefault('SOLR_URL', 'http://localhost:8983/solr')
        self.app.config.setdefault('SOLR_TIMEOUT', 5)
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions[EXTENSION_KEY] = self

    def get_connection(self):
        if not self._connection:
            url = self.app.config['SOLR_URL']
            timeout = self.app.config['SOLR_TIMEOUT']
            self._connection = pysolr.Solr(url, timeout=timeout)
        return self._connection
