#coding=utf8
from django.shortcuts import render

# Create your views here.


def index(req):
    response = render(req, 'index.html')
    return response

def upfile(req):
    response = render(req,'upfile.html')
    return response