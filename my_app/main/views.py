from django.shortcuts import render


# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'data', 'for', 'test'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football',
        }
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")
