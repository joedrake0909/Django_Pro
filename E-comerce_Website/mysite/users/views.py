from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateUserForm
from django.shortcuts import redirect

# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'users/register.html', {'form': form})