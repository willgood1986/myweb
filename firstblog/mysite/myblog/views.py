from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(req):
    '''
       just return django.http.HttpResponse('Welcome')
     
    '''
     #return HttpResponse('<h3>Welcome to Django!</h3>')
    users = {'name': 'Tom', 'age':23, 'sex':'male'}
    book_list = {'python', 'java', 'php', 'web'}

    return render_to_response('index.html', {'title':'MyBlog', 'book_list': book_list, 'users': users})
