# coding=utf8
from django.shortcuts import render,redirect

def index(req):

    response = render(req,'webui/t.html'
                          )
    return response