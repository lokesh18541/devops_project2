# 1. Update your database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/data/db.sqlite3', 
    }
}

# 2. Add 'students' to your INSTALLED_APPS array
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'students', 
]

ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'student_services.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'