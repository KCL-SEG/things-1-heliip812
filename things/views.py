from django.shortcuts import render


def render_html(request):
    return render(request, 'things.html')
# Create your views here.
