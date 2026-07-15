from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth import logout 
from django.shortcuts import redirect
from django.urls import reverse
from django.core.mail  import send_mail
from django.conf import settings
import random
from .models import OTPRecord
from django.contrib.auth import get_user_model
# Create your views here.



def is_admin(user):
    return user.is_authenticated and user.role == 'ADMIN'


def is_distributor(user):
    return user.is_authenticated and user.role == 'DISTRIBUTOR'

class CustomLoginView( LoginView ):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        user_role = str(getattr(self.request.user, 'role', '')).upper()
        
        if user_role == 'ADMIN':
            return reverse('admin_dashboard')
        elif user_role == 'DISTRIBUTOR':
            return reverse('distributor_dashboard')
        
        return reverse('login')
    

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

@login_required
@user_passes_test(is_distributor)
def distributor_dashboard(request):
    return render(request, 'accounts/distributor_dashboard.html')


def custom_logout(request):
    logout(request)
    return redirect('login')



User = get_user_model()
def password_reset_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)

            if not user.email:
                return HttpResponse("This user does not have an email address registered.", status=400)
            otp_code = str(random.randint(100000, 999999))
            OTPRecord.objects.create(user=user, otp=otp_code)

            send_mail(
                subject='Your Password Reset OTP',
                message=f'Hello {user.username}.\n\nYour OTP for password recovery is :{otp_code}\n\n This code will expire in 10 minutes.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
                fail_silently=False,
            )

            request.session['reset_username'] = username
            return redirect('verify_otp')
        except User.DoesNotExist:
            return HttpResponse("User not found.", status=404)
    
    return render(request, 'accounts/reset_request.html') 



def verify_otp(request):
    if request.method == 'POST':
        submitted_otp = request.POST.get('otp')
        username = request.session.get('reset_username')

        user = User.objects.get(username = username)

        latest_otp = OTPRecord.objects.filter(user=user).last()

        if latest_otp and latest_otp.otp == submitted_otp and latest_otp.is_valid():
            request.session['otp_verified'] = True
            return redirect('set_new_password')
        else:
            return HttpResponse("Invalid or expired otp")
        
    return render(request, 'accounts/verify_otp.html')


def set_new_password(request):
    if not request.session.get('otp_verified'):
        return redirect('login')
    
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        username = request.session.get('reset_username')

        user = User.objects.get(username=username)
        user.set_password(new_password)
        user.save()

        del request.session['reset_username']
        del request.session['otp_verified']
        return redirect('login')

    return render(request, 'accounts/set_new_password.html')