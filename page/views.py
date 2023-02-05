from django.shortcuts import render

# Create your views here.
def home_view(request):
    context=dict()
    return render(request, 'page/home_page.html', context)