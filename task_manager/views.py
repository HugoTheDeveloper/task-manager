from django.shortcuts import render


def hello_world(request):
    return render(request, 'start_page.html', context={'who': 'world'})
