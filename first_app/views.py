from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        <h1>This is contact</h1>
                        <a href="/first_app/about">About</a>
                        ''')


def about(request):
    return HttpResponse("This is about")