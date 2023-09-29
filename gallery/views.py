from django.shortcuts import render, redirect
from .models import Image, Likes, Comments
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.paginator import Paginator
from PIL import Image as PILImage
from django.db.models import Count

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
        images = Image.objects.annotate(total_likes_count=Count('likes')).filter(visible=True).order_by('-total_likes_count')[:12]

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

    images = Image.objects.all().order_by('-id')

    for i in images:
        if not i.username_visible:
            i.username = "Anonymous"

    user_likes = Likes.objects.filter(user=request.user).values_list('image_id', flat=True)


    paginator = Paginator(images, 16)
    page_number = request.GET.get('page', 1)
    images = paginator.get_page(page_number)
    total_pages = images.paginator.num_pages

    login_param = request.GET.get('login', None)
    if login_param == '1':
        success = True
    else:
        success = False

    login_param = request.GET.get('registration', None)
    if login_param == '1':
        registration = True
    else:
        registration = False
    

    
    return render(request, 'user/index.html', {'objects': images,
            'totalPageList': [(n + 1) for n in range(total_pages)],
            'user_likes': user_likes, "success": success, "registration": registration})


@login_required
@never_cache
def upload_image(request):

    user = request.user
    if user.is_superuser:
        return redirect("/admin")
    
    change = request.GET.get("change", None)

    if change != None:
        change = True
    else:
        change = False

    fail = request.GET.get('fail', None)

    if fail != None:
        fail = True
    else:
        fail = False

    return render(request, 'user/upload_image.html', {'change': change, 'fail': fail})


@login_required
@never_cache
def validate_upload_image(request):

    user = request.user
    if user.is_superuser:
        return redirect("/admin")

    if request.method == 'POST':
        image_file = request.FILES.get('image')

        try:
            image = PILImage.open(image_file)
            valid_formats = ('JPEG', 'JPG', 'PNG', 'GIF')
            if image.format not in valid_formats:
                return redirect("/gallery/upload_image?fail=1")
        except Exception as e:
            return redirect("/gallery/upload_image?fail=1")

        user = request.user
        caption = request.POST.get('caption')
        visible = request.POST.get('visible') == "on"
        username_visible = request.POST.get('username_visible') == "on"

        image_object = Image(
            image=image_file,
            user=user,
            caption=caption,
            visible=visible,
            username_visible=username_visible
        )

        image_object.save()

        return redirect("/gallery/upload_image?change=1")

    return redirect('/gallery/upload_image')



@login_required
@never_cache
def profile(request):

    if request.user.is_superuser: return redirect("/admin")
    images = Image.objects.filter(user=request.user).order_by('-id')
    total_likes = Likes.objects.all()
    total_comments = Comments.objects.all()
    image = request.GET.get("image", None)
    if image != None:
        image_saved = True
    else:
        image_saved = False



    image_deleted = request.GET.get("image_deleted", None)
    if image_deleted != None:
        image_deleted = True
    else:
        image_deleted = False


    image_not_deleted = request.GET.get("image_not_deleted", None)
    if image_not_deleted != None:
        image_not_deleted = True
    else:
        image_not_deleted = False



    changes = request.GET.get("changes", None)

    if changes != None:
        change = True

    else:
        change = False

    image_count = images.count
    paginator = Paginator(images, 6)
    page_number = request.GET.get('page', 1)
    images = paginator.get_page(page_number)
    total_pages = images.paginator.num_pages
    return render(request, "user/profile.html", {'objects': images, "image_deleted": image_deleted, "image_not_deleted": image_not_deleted
                                                  , "image_saved": image_saved, "change": change, 'total_likes': total_likes, "total_comments": total_comments, 'image_count': image_count, 'totalPageList': [(n + 1) for n in range(total_pages)]})

@login_required
@never_cache
def save_profile(request):

    if request.user.is_superuser: return redirect("/admin")

    if request.method == "POST":
        
        updated_user = request.user
        updated_user.first_name = request.POST.get('firstname')
        updated_user.last_name = request.POST.get('lastname')
        flag = request.POST.get('password')
        if flag != updated_user.password:
            updated_user.set_password(request.POST.get('password'))
        try:
            updated_user.save()
            return redirect("/gallery/profile?changes=1")
        except Exception as e:
            return redirect("/gallery/profile")
    
    return redirect("/gallery/profile")

@login_required
@never_cache
def update_image(request, id):
    if request.user.is_superuser: return redirect("/admin")

    if request.method == "POST":
        
        try:
            image = Image.objects.get(pk=id)
            image.caption = request.POST.get(f"caption{image.id}")
            image.visible = request.POST.get(f'visible{image.id}') == "on"
            image.username_visible = request.POST.get(f'username_visible{image.id}') == "on"
            image.save()
            return redirect("/gallery/profile?image=1")
        except Exception as e:
            return redirect("/gallery/profile")
            

    return redirect("/gallery/profile")

@login_required
@never_cache
def image_like(request, image_id):
    if request.user.is_superuser: return redirect("/admin")

    already_liked = Likes.objects.filter(user=request.user, image_id=image_id).exists()

    if not already_liked:
        likes = Likes()
        likes.user = request.user
        likes.image_id = Image.objects.get(pk=image_id)
        likes.save()

    return redirect("/gallery/user_home")


@login_required
@never_cache
def remove_like(request, image_id):
    if request.user.is_superuser: return redirect("/admin")

    try:
        likes = Likes.objects.get(user=request.user, image_id=image_id)
        likes.delete()
    except Exception as e:
        pass

    return redirect("/gallery/user_home")


@login_required
@never_cache
def remove_like_profile(request, like_id):
    if request.user.is_superuser: return redirect("/admin")

    try:
        likes = Likes.objects.get(id=like_id)
        if request.user.id == likes.user.id:
            likes.delete()
    except Exception as e:
        print(e)
    return redirect("profile")
    

@login_required
@never_cache
def add_comment(request, image_id):
    if request.user.is_superuser: return redirect("/admin")

    if request.method == "POST":
        comment = request.POST.get(f'comment{image_id}')
        comment_object = Comments()
        try:
            comment_object.image_id = Image.objects.get(pk=image_id)
            comment_object.user = request.user
            comment_object.comment = comment
            comment_object.save()
        except Exception as e:
            print(e)
        return redirect("/gallery/user_home")        

    return redirect("/gallery/user_home")


@login_required
@never_cache
def remove_comment_profile(request, comment_id):
    if request.user.is_superuser: return redirect("/admin")

    try:
        comment = Comments.objects.get(id=comment_id)
        if request.user.id == comment.image_id.user.id:
            comment.delete()
        else:
            print("Nhk")
    except Exception as e:
        print(e)

    return redirect("profile")


@login_required
@never_cache
def delete_image(request, id):
    if request.user.is_superuser: return redirect("/admin")

    if request.method == "POST":
        
        try:
            image = Image.objects.get(user=request.user, pk=id)
            image.image.delete(save=True)
            image.delete()
            return redirect("/gallery/profile?image_deleted=1")

        except Exception as e:
            print(e)
            return redirect("/gallery/profile?image_not_deleted=1")

    return redirect("/gallery/profile")



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
            return redirect("/gallery/user_home?login=1")
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
        return redirect("/gallery/user_home?registration=1")
    else:
        return render(request, 'register.html', {})