
from django.contrib import admin
from django.urls import path,include
from companies import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home, name='home'),
    path('companies/', views.companies, name='companies'),
    path('softwarecompanies/', views.softwarecompanies, name='softwarecompanies'),
    path('recruitmentprocess/', views.recruitmentprocess, name='recruitmentprocess'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.login, name='login'),
    path('', views.index, name='index'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('accenture/', views.accenture, name='accenture' ),
    path('aws/', views.aws, name='aws' ),
    path('cisco/', views.cisco, name='cisco' ),
    path('cognizant/', views.cognizant, name='cognizant'),
    path('google/', views.google, name='google'),
    path('hcl/', views.hcl, name='hcl'),
    path('hp/', views.hp, name='hp'),
    path('ibm/', views.ibm, name='ibm'),
    path('infosys/', views.infosys, name='infosys'),
    path('microsoft/', views.microsoft, name='microsoft'),
    path('musigma/', views.musigma, name='musigma'),
    path('oracle/', views.oracle, name='oracle'),
    path('tcs/', views.tcs, name='tcs'),
    path('techmahindra/', views.techmahindra, name='techmahindra'),
    path('unysis/', views.unysis, name='unysis'),
    path('verizon/', views.verizon, name='verizon'),
    path('vmware/', views.vmware, name='vmware'),
    path('wipro/', views.wipro, name='wipro'),
    path('psu/',views.psu,name='psu'),
    path('power/',views.power,name='power'),
    path('e_commerece/',views.e_commerce, name='e_commerce'),
    path('auto/',views.auto, name='auto'),
    path('realstate/',views.realstate, name='realstate'),
    path('metal/', views.metal, name='metal'),
    path('telecommunication/',views.telecommunication, name='telecommunication'),
    path('airtel/', views.airtel ,name='airtel'),
    path('bsnl/', views.bsnl, name='bsnl'),
    path('ericsson/', views.ericsson, name='ericsson'),
    path('nokia/', views.nokia, name='nokia'),
    path('reliance/', views.reliance, name='reliance'),
    path('dlf/',views.dlf, name='dlf'),
    path('godrej/',views.godrej, name='godrej'),
    path('lnt/', views.lnt, name='lnt'),
    path('bpcl/',views.bpcl,name='bpcl'),
    path('hpcl/',views.hpcl,name='hpcl'),
    path('iocl/',views.iocl,name='iocl'),
    path('ongc/',views.ongc,name='ongc'),
    path('gail/',views.gail,name='gail'),
    path('relience/',views.Relience,name='Relience'),
    path('bajaj/',views.bajaj,name='bajaj'),
    path('hero/', views.hero, name='hero'),
    path('maruti/', views.maruti, name='maruti'),
    path('nissan/', views.nissan, name='nissan'),
    path('tata/', views.tata, name='tata'),
    path('mahindra/', views.mahindra, name='mahindra'),
    path('eicher/', views.eicher, name='eicher'),
    path('adani/', views.adani, name='adani'),
    path('ntpc/', views.ntpc, name='ntpc'),
    path('powergrid/', views.powergrid, name='powergrid'),
    path('reliencepower/', views.reliencepower, name='reliencepower'),
    path('tatapower/', views.tatapower, name='tatapower'),
    path('coalindia/', views.coalindia, name='coalindia'),
    path('tatasteel/', views.tatasteel, name='tatasteel'),
    path('vedanta/', views.vedanta, name='vedanta'),
    path('amazon/', views.amazon, name='amazon'),
    path('ebay/', views.ebay, name='ebay'),
    path('flipkart/', views.flipkart, name='flipkart'),
    path('contact/', include('contactus.urls')),
]

urlpatterns += staticfiles_urlpatterns()