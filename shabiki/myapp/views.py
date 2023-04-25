from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from . import forms;

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f'''
        <br>Path: {path}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>Address: {address}
        <br>User Agent: {user_agent}
        <br>Path info: {path_info}
        <br>Response header: {response.headers}
    '''
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def getuser(request, name, id):
    return HttpResponse("Name: {} <br> UserID: {}".format(name, id))

def getuserqryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {} <br> UserId: {}".format(name, id))

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name: {} <br> UserId: {}".format(name,id))

def getuserform(request):
    if request.method == "POST":
        form = forms.DemoForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/getuserform/')
    else:
        form = forms.DemoForm()
    
    return render(request, "form_example.html", {"form": form})
        
