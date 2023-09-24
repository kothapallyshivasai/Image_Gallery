from django.shortcuts import render, redirect

def redirection(request):
    return redirect('/gallery/home')