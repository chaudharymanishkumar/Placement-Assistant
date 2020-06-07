import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&!0+#su4zhnex#o(&(xs09$8z-5e!hahkd04wmw)x-7sknrrk7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'tests.apps.TestsConfig',
    'companies.apps.CompaniesConfig',
    'accounts.apps.AccountsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'contactus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'placementassistent.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['companies/templates', 'software_companies/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',         #new for social auth
                'social_django.context_processors.login_redirect',   #new for social login
            ],
        },
    },
]

WSGI_APPLICATION = 'placementassistent.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#Adding database named placementassistentdb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'placementassistentdb',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,"static"),
    ) 


LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',

    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '439281664367-069hlsk0t97blcaactc3app164b1gu0s.apps.googleusercontent.com'    #app key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WO62QSqBuaBUyRdX2y7r5Fxu'                                                  #app secret key
SOCIAL_AUTH_FACEBOOK_KEY = '1070857146434643'                       #app id
SOCIAL_AUTH_FACEBOOK_SECRET = '6be232e07676506e8ed965f6bbc118c2'     #app secret key

SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '786ehdif25dk32'
SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'PsqYmyUesN87hebT'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'