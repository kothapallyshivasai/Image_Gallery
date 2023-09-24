from django.shortcuts import render, redirect
from .models import Image
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.paginator import Paginator
from PIL import Image as PILImage

# Create your views here.
@never_cache
def home_page(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.is_authenticated:
            return redirect("/gallery/user_home")
 
    except Exception as e:
        pass

    else:
        images = Image.objects.filter(visible = True)[:12]

        for i in images:
            if not i.username_visible:
                i.username = "Anonymous"

        return render(request, "index.html", {"objects": images})


@login_required
@never_cache
def user_home(request):

    user = request.user
    if user.is_superuser:
        return redirect("/admin")

    images = Image.objects.all()

    for i in images:
        if not i.username_visible:
            i.username = "Anonymous"

    paginator = Paginator(images, 16)
    page_number = request.GET.get('page', 1)
    images = paginator.get_page(page_number)
    total_pages = images.paginator.num_pages
    
    return render(request, 'user/index.html', {'objects': images,
            'totalPageList': [(n + 1) for n in range(total_pages)]})



@login_required
@never_cache
def upload_image(request):

    user = request.user
    if user.is_superuser:
        return redirect("/admin")

    return render(request, 'user/upload_image.html', {})


@login_required
@never_cache
def validate_upload_image(request):
    if request.method == 'POST':

        image_object = Image()
        image_object.image = request.FILES.get('image')
        image_object.user = request.user
        image_object.caption = request.POST.get('caption')
        image_object.visible = request.POST.get('visible') == "on"
        image_object.username_visible = request.POST.get('username_visible') == "on"
        image_object.save()

        return redirect('/gallery/profile/')  

    return redirect('/gallery/upload/')



@login_required
@never_cache
def profile(request):
    return render(request, "user/profile.html", {})



@never_cache
def login(request):
    if request.method == "GET":
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.is_authenticated:
            return redirect("/gallery/user_home")

        return render(request, 'login.html', {})

    elif request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))

        if user is not None:
            auth_login(request, user)  
            return redirect("/gallery/user_home")
        else:
            return render(request, 'login.html', {'error_message': True})


@never_cache
def register(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.is_authenticated:
            return redirect("/gallery/user_home")
 
    except Exception as e:
        pass
    
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("/gallery/register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already in use.")
            return redirect("/gallery/register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address is already registered.")
            return redirect("/gallery/register")

        User.objects.create_user(username=username, email=email, password=password)
        authenticated_user = authenticate(request, username=username, password=password)
        
        auth_login(request, authenticated_user)  
        return redirect("/gallery/user_home")
    else:
        return render(request, 'register.html', {})