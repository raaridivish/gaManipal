from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from . models import Atm

# Create your views here.
def index(request):
    if request.method == "POST":
        branch_name = request.POST.get('branch_name')
        branch_code = request.POST.get('branch_code')
        front_view = request.FILES['front_view']
        back_view = request.FILES['back_view']
        top_view = request.FILES['top_view']
        atm = Atm(branch_name=branch_name, branch_code=branch_code, front_view=front_view, back_view=back_view, top_view=top_view)
        atm.save()
        return redirect('/')
    return render(request, 'add.html')

def list(request):
    atm_list = Atm.objects.all()
    context = {'atm_list': atm_list}
    return render(request, 'list.html', context)