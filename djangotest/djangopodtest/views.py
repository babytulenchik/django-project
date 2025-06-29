from django.http import HttpResponce

def startview(request):
    return HttpResponce("Добро пожаловать на мой сайт!")

def aboutview(request):
    return HttpResponce("Это страница 'О нас'. Мы занимаемся веб-разработкой на Django.")

def contacts(request):
    return HttpResponce("Email: example@mail.com")
    

def users(request, username):
    return HttpResponce(f"Привет, {username}!")

def articles(request, article_id):
    return HttpResponce(f"Статья №{article_id}")
