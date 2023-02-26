from django.shortcuts import render, redirect
from django.contrib import messages  #to display flash messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required





def register(request):  
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #collect the form
        if form.is_valid(): #check whether it is valid or not
            #saves the user to our database
            form.save()
            
            username = form.cleaned_data.get('username')
#update the base html template to actually display the message
            messages.success(request, f'Your account has been created. You are now able to login!')#show a flash message
#after the form has been submitted and the user has been created, just redirect back to the original page
            
            return redirect('login')
    else:
        form = UserRegisterForm() 
    #python classes that get converted into HTML
     #form that will be passed to the template
    return render(request, 'users/register.html', {'form':form})


#decorators -> adds functionality to our existing function
#required the user to be logged in order to access the profile page
@login_required
def profile_view(request):
    return render(request, 'users/profile.html')












