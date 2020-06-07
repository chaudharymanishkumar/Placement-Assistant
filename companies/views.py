from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from companies.forms import RegistrationForm, LoginForm
from django.shortcuts import render_to_response
from django.core.exceptions import ValidationError



# Create your views here.
def home(request):
	return render(request, 'companies/home.html')


def companies(request):
	return render(request,'companies/companies.html')


def softwarecompanies(request):
	return render(request, 'companies/softwareco.html')


def psu(request):
	return render(request, 'companies/psu.html')

def power(request):
	return render(request, 'companies/power.html')

def e_commerce(request):
	return render(request, 'companies/e_commerce.html')

def metal(request):
	return render(request, 'companies/metal.html')

def auto(request):
	return render(request, 'companies/auto.html')

def realstate(request):
	return render(request, 'companies/realstate.html')

def telecommunication(request):
	return render(request, 'companies/telecommunication.html')






def recruitmentprocess(request):
	return render(request,'companies/recruitmentpro.html')

'''context = {}
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, email=email, password=password)
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse	('home'))
		else:
			context['error'] = "Provide valid credentials"
			return render(request, 'companies/login.html', context)

	else:
		return render(request, 'companies/login.html', context)'''


def signup(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
                                     username=form.cleaned_data['username'],
                                     email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password1']
                                    )
			return redirect('home')
	else:
		form = RegistrationForm()

	return render(request, 'companies/signup.html', {'form': form})


def login(request):
	l = LoginForm(request.POST or None)
	if request.method == 'POST':
		print("hello in login")
		if l.is_valid():
			user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
			print("user is correct")
		# auth_login(request,user)
			if user:
				auth_login(request, user)
				return redirect('home')
	else:
		l = LoginForm()
	return render(request, 'companies/login.html', {'form': l})


def index(request):
	logout(request)
	return render(request, 'companies/index.html')




def accenture(request):
	return render(request, 'companies/software/accenture.html')

def google(request):
	return render(request, 'companies/software/goggle.html')

def aws(request):
	return render(request, 'companies/software/aws.html')

def hcl(request):
	return render(request, 'companies/software/hcl.html')

def cisco(request):
	return render(request, 'companies/software/cisco.html')

def cognizant(request):
	return render(request, 'companies/software/cognizant.html')

def hp(request):
	return render(request, 'companies/software/hp.html')

def microsoft(request):
	return render(request, 'companies/software/microsoft.html')

def ibm(request):
	return render(request, 'companies/software/ibm.html')

def musigma(request):
	return render(request, 'companies/software/musigma.html')

def oracle(request):
	return render(request, 'companies/software/oracle.html')

def infosys(request):
	return render(request, 'companies/software/infosys.html')

def unysis(request):
	return render(request, 'companies/software/unysis.html')

def verizon(request):
	return render(request, 'companies/software/verizon.html')

def wipro(request):
	return render(request, 'companies/software/wipro.html')

def vmware(request):
	return render(request, 'companies/software/vmware.html')

def techmahindra(request):
	return render(request, 'companies/software/techmahindra.html')

def tcs(request):
	return render(request, 'companies/software/tcs.html')


def dlf(request):
	return render(request, 'companies/realstate/dlf.html')

def godrej(request):
	return render(request, 'companies/realstate/godrej.html')

def lnt(request):
	return render(request, 'companies/realstate/lnt.html')



def airtel(request):
	return render(request, 'companies/telecommunication/airtel.html')

def bsnl(request):
	return render(request, 'companies/telecommunication/bsnl.html')

def ericsson(request):
	return render(request, 'companies/telecommunication/ericsson.html')

def nokia(request):
	return render(request, 'companies/telecommunication/nokia.html')

def reliance(request):
	return render(request,'companies/telecommunication/reliance.html')

def bpcl(request):
	return render(request, 'companies/psu/bpcl.html')

def hpcl(request):
	return render(request, 'companies/psu/hpcl.html')

def iocl(request):
	return render(request, 'companies/psu/iocl.html')

def ongc(request):
	return render(request, 'companies/psu/ongc.html')

def gail(request):
	return render(request, 'companies/psu/gail.html')

def Relience(request):
	return render(request, 'companies/psu/relience.html')

def bajaj(request):
	return render(request, 'companies/automobiles/bajaj.html')

def hero(request):
	return render(request, 'companies/automobiles/hero.html')

def maruti(request):
	return render(request, 'companies/automobiles/maruti.html')


def nissan(request):
	return render(request, 'companies/automobiles/nissan.html')


def tata(request):
	return render(request, 'companies/automobiles/tata.html')

def mahindra(request):
	return render(request, 'companies/automobiles/mahindra.html')


def eicher(request):
	return render(request, 'companies/automobiles/eicher.html')

def adani(request):
	return render(request, 'companies/power/adani.html')

def ntpc(request):
	return render(request, 'companies/power/ntpc.html')


def powergrid(request):
	return render(request, 'companies/power/powergrid.html')


def reliencepower(request):
	return render(request, 'companies/power/reliencepower.html')

def tatapower(request):
	return render(request, 'companies/power/tatapower.html')


def coalindia(request):
	return render(request, 'companies/metalandmining/coalindia.html')

def tatasteel(request):
	return render(request, 'companies/metalandmining/tatasteel.html')


def vedanta(request):
	return render(request, 'companies/metalandmining/vedanta.html')


def amazon(request):
	return render(request, 'companies/ecommerce/amazon.html')


def ebay(request):
	return render(request, 'companies/ecommerce/ebay.html')

def flipkart(request):
	return render(request, 'companies/ecommerce/flipkart.html')