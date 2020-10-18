from django.shortcuts import redirect
from django.http import HttpResponse

def writer_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_authenticated:
                try:
                    group = request.user.groups.all()[0].name
                except:
                    group = None
                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Nie masz uprawnień do wyświetlenia tej strony')
        return wrapper_func
    return decorator