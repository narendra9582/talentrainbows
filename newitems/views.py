from django.shortcuts import render

def newitems(request):
    return render(request,'new_items.html')
