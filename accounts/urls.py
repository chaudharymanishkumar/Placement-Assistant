from django.conf.urls.defaults import *
from registration.backends.default.urls import *
from accounts.forms import UserRegistrationForm

urlpatterns += patterns('',

    #customize user registration form
    url(r'^register/$', 'registration.views.register',
        {
            'backend': 'accounts.regbackend.Backend',
            'form_class' : UserRegistrationForm
        },
        name='registration_register'
    ),

) 