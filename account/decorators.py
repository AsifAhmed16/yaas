from django.shortcuts import render
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import resolve
from .models import User, Privileged


def access_permission_required(view_func):
    def _decorator(request, *args, **kwargs):
        # #check if the user has proper permission to access this function
        myfunc, myargs, mykwargs = resolve(request.get_full_path())
        view_function = myfunc.__name__
        user = request.session['id']
        if user is None:
            return render(request, 'account/login.html')
        user_profile = User.objects.get(id=user)
        role_id = user_profile.user_role_id
        access = Privileged.objects.filter(userrole_id=role_id, moduleurl__url=view_function)
        if not access.exists():
            return redirect('account:register')
        response = view_func(request, *args, **kwargs)
        # maybe do something after the view_func call
        return response
    return wraps(view_func)(_decorator)


def login_required(session_key, fail_redirect_to):
    def _session_required(view_func):
        @wraps(view_func)
        def __session_required(request, *args, **kwargs):
            try:
                session = request.session.get(session_key)
                if session is None:
                    raise ValueError('Login Session is Expired Please Login Again!')
            except KeyError as e:
                messages.error(request, 'Login Session is Expired Please Login Again!')
                return redirect(fail_redirect_to)
            except ValueError as e:
                messages.error(request, 'Login Session is Expired Please Login Again!')
                return redirect(fail_redirect_to)
            else:
                return view_func(request, *args, **kwargs)
        return __session_required
    return _session_required
