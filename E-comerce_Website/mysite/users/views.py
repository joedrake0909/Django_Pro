from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from .forms import CreateUserForm
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str
from .token import account_activation_token
# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            # Email Verification Logic 
            subject = 'Verify your email to activate your account'
            message = render_to_string('users/email-verification.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            } )

            user.email_user(subject=subject,message=message)
            return redirect('email-verification-sent')


    return render(request, 'users/register.html', {'form': form})


def email_verification(request):
    pass

def email_verification_sent(request):
    return render(request, 'users/email-verification-sent.html')

def email_verification_success(request):
    pass

def email_verification_failed(request):
    pass
