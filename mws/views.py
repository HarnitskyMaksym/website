import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return render(request, 'mws\\index.html')

def update(request):
    if request.method == 'POST':
        repo = git.Repo('hmaksymwebsite.com.ua')
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse('Updated on HMAKSYM')
    
    else:
        return HttpResponse('Couldn\'t update the server')