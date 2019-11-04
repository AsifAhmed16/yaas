from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from auction.views import mail_notification, bid_mail_notification, uniqueBidder, maxPrice
from auction.forms import *
from auction.models import *
import random


def store_language_list(request):
    display = Auction.objects.filter(status_id=1)
    context = dict()
    context['display'] = display
    if 'language' in request.session:
        userdata = {
            'language': request.session['language'],
        }
    else:
        request.session['language'] = "Eng"
        userdata = {
            'language': "Eng",
        }
    context['data'] = userdata
    if request.method == 'POST':
        display = display.filter(title__icontains=request.POST['Search'])
        context['display'] = display
        if request.POST['language']:
            request.session['language'] = request.POST['language']
            userdata = {
                'language': request.POST['language'],
            }
            context['data'] = userdata
            if 'logged_in' in request.session:
                if request.session['logged_in'] is True:
                    userdata = {
                        'username': request.session['username'],
                        'logged_in': request.session['logged_in'],
                        'language': request.session['language'],
                    }
                    context['data'] = userdata
                return redirect('account:index')
    if 'logged_in' in request.session:
        if request.session['logged_in'] is True:
            userdata = {
                'username': request.session['username'],
                'logged_in': request.session['logged_in'],
                'language': request.session['language'],
            }
            context['data'] = userdata
            return render(request, 'account/home.html', context)
    return render(request, 'account/home.html', context)


def auction_add(request):
    try:
        if 'logged_in' in request.session:
            if request.session['logged_in'] is True:
                form = AuctionTempForm
                userdata = {
                    'id': request.session['id'],
                    'username': request.session['username'],
                    'logged_in': request.session['logged_in'],
                    'language': request.session['language'],
                }
                context = {
                    'data': userdata,
                    'form': form,
                }
                if request.method == 'POST':
                    form = AuctionTempForm(request.POST, request.FILES or None)
                    if form.is_valid():
                        form = form.save(commit=False)
                        form.seller = User.objects.get(id=request.session['id'])
                        form.save()
                        temp = Auction_Temp.objects.latest('id')
                        mail_notification(request, request.session['id'], temp.id)
                        if request.session['language'] == "Eng":
                            messages.success(request, 'A request mail has been sent...Please check your Email')
                        else:
                            messages.success(request, 'Pyyntöviesti on lähetetty...Ole hyvä ja tarkista sähköpostisi.')
                        return redirect('account:index')
                    else:
                        print(form.errors)
                        context = {
                            'data': userdata,
                            'form': form
                        }
                        if request.session['language'] == "Eng":
                            messages.error(request, 'Sorry !!! Something Went Wrong.')
                        else:
                            messages.error(request, 'Anteeksi !!! Jotain Meni Pieleen.')
                        return render(request, 'auction/auction_add.html', context)
                return render(request, 'auction/auction_add.html', context)
            else:
                if request.session['language'] == "Eng":
                    messages.error(request, 'Please login before creating an auction.')
                else:
                    messages.error(request, 'Ole hyvä ja kirjaudu sisään ennen huutokaupan luomista')
                return redirect('account:login')
        else:
            if request.session['language'] == "Eng":
                messages.error(request, 'Please login before creating an auction.')
            else:
                messages.error(request, 'Ole hyvä ja kirjaudu sisään ennen huutokaupan luomista')
            return redirect('account:login')
    except Exception as ex:
        print(ex)
        messages.error(request, str(ex))
        return redirect('account:login')
