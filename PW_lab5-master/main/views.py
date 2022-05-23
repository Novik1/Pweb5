from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import News, Category


# Create your views here.
def home(request):
    first_news = News.objects.first()
    three_news = News.objects.all()[1:3]
    categories = Category.objects.all()

    return render(request, 'home.html',{
        'first_news': first_news,
        'three_news': three_news,
        'categories': categories,
    })


def all_news(request):
    all_news = News.objects.all()
    return render(request,'all-news.html',{
        'all_news': all_news
    })

def create_news(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.POST['image']
        detail = request.POST['detail']
        category = request.POST['category']
        cat = Category.objects.get(title = category)
        cat_id = cat.id
        privacy = request.POST['privacy']
        if privacy == "true" or "True":
            privacy_bool = 1

        News.objects.create(
            title = title,
            image = image,
            detail = detail,
            category_id = cat_id,
            privacy = privacy_bool
        )
        messages.success(request, 'Saved')
    return render(request,'create_news.html')

def edit(request, id):
    news = News.objects.get(pk = id)
    if request.method == 'POST':
        title = request.POST['title']
        image = request.POST['image']
        detail = request.POST['detail']
        category = request.POST['category']
        cat = Category.objects.get(title = category)
        cat_id = cat.id
        privacy = request.POST['privacy']
        if privacy == "true" or "True":
            privacy_bool = 1

        news.title = title
        news.image = image
        news.detail = detail
        news.category_id = cat_id
        news.privacy = privacy_bool
        news.save()


        messages.success(request, 'Saved')

    return render(request,'edit_news.html',{
        'news': news
    })

def detail(request, id):
    news = News.objects.get(pk = id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        Comment.objects.create(
            news = news,
            name = name,
            email = email,
            comment = comment
        )
        messages.success(request, 'Comment submitted but in moderation mode')

    category = Category.objects.get(id = news.category.id)
    rel_news = News.objects.filter(category = category).exclude(id = id)
    return render(request,'detail.html',{
        'news': news,
        'related_news': rel_news
    })


#User Registration
def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been successfully registered')
    return render(request, 'registration/register.html',{
        'form': form
    })
