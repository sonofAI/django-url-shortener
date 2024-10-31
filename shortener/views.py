from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import URLForm
from .models import ShortURL

# Create your views here.

def home(request):
    if 'POST' == request.method:
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = form.save()
            base_url = request.build_absolute_uri('/')
            return JsonResponse({'success': True, 'short_url': f'{base_url}{short_url.short_url}'})

    else:
        form = URLForm()

    return render(request, 'index.html', {'form': form})


def redirect_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_url=short_code)
    return redirect(short_url.full_url)