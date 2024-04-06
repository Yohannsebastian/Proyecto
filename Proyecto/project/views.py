from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'{username} creado')
    else: 
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'Proyecto/regitro.html')