import django

PROJECT_APPS = [
    'file_manager_mptt', 
    'testapp'
]

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth'
 ] 

INSTALLED_APPS.extend(PROJECT_APPS)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
)

DATABASE_ENGINE = 'sqlite3'
SECRET_KEY = 'nokey'
MIDDLEWARE_CLASSES = ()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

if django.VERSION < (1, 9):
    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return 'notmigrations'

    MIGRATION_MODULES = DisableMigrations()
else:
    MIGRATION_MODULES = {
    'auth': None,
    'contenttypes': None,
}


ANONYMOUS_USER_ID = 0
