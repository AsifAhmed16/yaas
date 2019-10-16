from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta


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
                        form.seller = User.objects.get(id=request.session['id'])
                        form.status = Auction_Status.objects.get(status="Active")
                        form.deadline = datetime.now() + timedelta(days=3)
                        form.created_date = datetime.now()
                        form.save()
                        messages.success(request, 'Auction Added')
                        return redirect('account:index')
                    else:
                        print(form.errors)
                        context = {
                            'data': userdata,
                            'form': form
                        }
                        messages.error(request, 'Sorry...Something went wrong.')
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
