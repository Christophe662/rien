from django.shortcuts import render


def mycv_view(request):
    #return HttpResponse ('Contacter nous')
     return render(request,'my_cv/list.html')
