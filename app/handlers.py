from django.shortcuts import render


def not_found_handler(request, *args, **kwargs):
    return render(request, 'errors/404.html', status=404)

def server_error_handler(request, *args, **kwargs):
    return render(request, 'errors/500.html', status=500)
