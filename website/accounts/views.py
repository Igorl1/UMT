from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def RegistrationView(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/sign_up.html', context)

def HomeView(request):
    """
    Home page view that handles both authenticated and anonymous users.
    
    - If user is logged in: redirect to their media tracker
    - If user is anonymous: show landing page
    """
    if request.user.is_authenticated:
        # User is logged in, redirect to their tracker
        return redirect('/tracker/')
    else:
        # User is not logged in, show home page
        return render(request, 'accounts/home.html')

def LogoutConfirmView(request):
    """
    Show logout confirmation page and handle logout POST request.
    """
    if request.method == 'POST':
        # User confirmed logout
        logout(request)
        return redirect('home')
    else:
        # Show logout confirmation page
        return render(request, 'registration/logout.html')

def DeleteAccountView(request):
    """
    Show account deletion confirmation page and handle account deletion POST request.
    Prevents deletion of admin accounts for security.
    """
    user = request.user
    
    if user.is_superuser:
        context = {
            'error_message': 'Administrator accounts cannot be deleted.',
            'user': user
        }
        return render(request, 'registration/delete_acc.html', context)
    
    if request.method == 'POST':
        # User confirmed
        if user.is_superuser:
            return redirect('home')

        # Regular account
        logout(request)  # Log out
        user.delete()    # Then delete
        return redirect('home')
    else:
        # Show account deletion confirmation page
        context = {'user': user}
        return render(request, 'registration/delete_acc.html', context)