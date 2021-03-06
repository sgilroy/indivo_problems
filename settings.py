from django.conf import settings # top-level setttings

# UPDATE THESE SETTINGS:
INDIVO_SERVER_OAUTH = {
#    'consumer_key': 'problems@apps.indivo.org',
#    'consumer_secret': 'problems'
    'consumer_key': 'sampleweb@apps.indivo.org',
    'consumer_secret': 'yourwebapp'
}
INDIVO_SERVER_LOCATION = 'http://sandbox.indivohealth.org:8000'
INDIVO_UI_SERVER_BASE = 'http://sandbox.indivohealth.org'

APP_HOME = 'C:\\Users\\sgilroy\\Documents\\IndivoHackathon\\indivo_problems_standalone\\'
STATIC_HOME = APP_HOME+'/static'

# Django Settings: can safely ignore
SEND_MAIL = False # Whether to notify admins when something fails

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ( # Admins to notify when email routing fails
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'e7^o7-%74eov^a!&9=9&)()%&_4%!bv*@01&z+^z&36@nnj=7w'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    )

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    APP_HOME + "/templates"
    )

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'indivo_problems_standalone',
    )

# use file based sessions for now - fixme: security?
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = APP_HOME + "/sessions"
SESSION_COOKIE_NAME = "indivo_problems_sessionid"

