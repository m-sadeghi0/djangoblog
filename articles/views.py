from django.shortcuts import render
from . import models

# Create your views here.
def articleslist(request):
    articels=models.articlesclass.objects.all().order_by('date')
    args={'artic':articels}
    return render(request,'articles/list.html',args)
