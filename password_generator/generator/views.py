from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'qwertyuiop'})


def password(request):
    lower_case_characters_list = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        lower_case_characters_list.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        lower_case_characters_list.extend(list('!@#$%^&*()'))

    if request.GET.get('number'):
        lower_case_characters_list.extend(list('0123456789'))

    length_of_password = int(request.GET.get('length', 12))
    the_password = ''

    # print(lower_case_characters_list)

    for x in range(length_of_password):
        the_password += random.choice(lower_case_characters_list)

    return render(request, 'generator/password.html', {'password': the_password})
