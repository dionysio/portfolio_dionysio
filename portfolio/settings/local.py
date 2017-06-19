from .settings import *

BASE_URL = 'localhost:8002'

DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = THUMBNAIL_DEBUG = SQL_DEBUG = DEBUG
DEBUG_TOOLBAR = True
if DEBUG_TOOLBAR:
    INSTALLED_APPS += ['debug_toolbar', ]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

from debug_toolbar.middleware import show_toolbar

def custom_show_toolbar(request, excluded_urls = ['/admin']):
    return show_toolbar(request) and not any(request.path.startswith(url) for url in excluded_urls)
#SHOW_TOOLBAR_CALLBACK = custom_show_toolbar

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

INTERNAL_IPS = ['127.0.0.1', '::1']
ALLOWED_HOSTS.extend(INTERNAL_IPS)
MEDIA_DIRS = os.path.join(BASE_DIR, "../public/media")
STATIC_ROOT = '/tmp/static/'


STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
