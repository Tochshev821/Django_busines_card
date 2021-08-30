from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница!!',
        'values': ['some','Hello','123'],
        'obj': {
            'car': 'bmw',
            'age': 21,
            'hobby': 'wrestling'
        }
    }
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')
