from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # التحقق من صحة البيانات قبل الحفظ
            user = form.save()
            login(request, user)
            return redirect('/index')  # استخدم المسار الصحيح
    return render(request, 'signup.html', {'form': form})



# def logout_view(request):
#       logout(request)
#       return redirect('signup')