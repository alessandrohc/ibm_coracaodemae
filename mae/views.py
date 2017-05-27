from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#@login_required
def inicio(request):
    context = {}
    return render(request, 'mommy/index.html', context)

