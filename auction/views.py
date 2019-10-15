from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def auction_add(request):
    try:
        if 'logged_in' in request.session:
            if request.session['logged_in'] is True:
                form = AuctionForm
                userdata = {
                    'id': request.session['id'],
                    'logged_in': request.session['logged_in'],
                }
                context = {
                    'data': userdata,
                    'form': form,
                }
                if request.method == 'POST':
                    form = AuctionForm(request.POST, request.FILES or None)
                    if form.is_valid():
                        form = form.save(commit=False)
                        form.save()
                        messages.success(request, 'Auction Added')
                        return redirect('auction:auction_add')
                    else:
                        print(form.errors)
                        context = {
                            'data': userdata,
                            'form': form
                        }
                        return render(request, 'auction/auction_add.html', context)
                return render(request, 'auction/auction_add.html', context)
            else:
                messages.error(request, 'Please login before creating an auction.')
                return redirect('account:login')
        else:
            messages.error(request, 'Please login before creating an auction.')
            return redirect('account:login')
    except Exception as ex:
        print(ex)
        messages.error(request, str(ex))
        return redirect('account:login')
