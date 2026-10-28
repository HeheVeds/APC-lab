from django.shortcuts import render
import re

def login(request):
    msg = ""

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if re.match(r'^[a-zA-Z0-9_]{3,15}$', username) and re.match(r'^[A-Za-z0-9@#$]{8,}$', password):
            msg = "Login Successful!"
        else:
            msg = "Invalid Username or Password"

    return render(request, 'login.html', {'msg': msg})