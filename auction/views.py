from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
from .tasks import set_deadline
from django.core.mail import send_mail
import socket


def auction_add(request):
    try:
        if 'logged_in' in request.session:
            if request.session['logged_in'] is True:
                form = AuctionTempForm
                userdata = {
                    'id': request.session['id'],
                    'logged_in': request.session['logged_in'],
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
                        messages.success(request, 'A request mail has been sent...Please check your Email')
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


def auction_confirm(request, id):
    try:
        temp = Auction_Temp.objects.get(pk=id)
    except Exception as e:
        messages.error(request, 'Sorry...Link is no more valid.')
        return redirect('account:index')
    user = User.objects.get(pk=temp.seller.id)
    request.session['logged_in'] = True
    request.session['username'] = user.username
    request.session['id'] = user.pk
    form = AuctionTempForm(instance=temp)
    userdata = {
        'id': request.session['id'],
        'logged_in': request.session['logged_in'],
    }
    context = {
        'data': userdata,
        'form': form,
    }
    if request.method == 'POST':
        form = AuctionForm(request.POST or None, instance=temp)
        if form.is_valid():
            Auction.objects.create(title=request.POST['title'],
                                   description=request.POST['description'],
                                   seller=User.objects.get(id=request.session['id']),
                                   min_price=request.POST['min_price'],
                                   status=Auction_Status.objects.get(status="Active"),
                                   deadline=datetime.now() + timedelta(days=3),
                                   created_date=datetime.now())
            auction = Auction.objects.latest('id')
            _post_tasks(request, auction.id)
            temp.delete()
        messages.success(request, 'Auction Added Successfully.')
        return redirect('account:index')
    return render(request, 'auction/auction_add.html', context)


def mail_notification(request, id, temp_auc):
    employeeobject = User.objects.get(id=id)
    mailbody = "Dear " + employeeobject.username + "," + '\n' + '\n' \
               + "Please go to the link below and confirm auction you made. " + '\n' + '\n' + \
               "Link: " + "http://127.0.0.1:8000/auctionauction/create/" + str(temp_auc) + "" + '\n' + '\n'
    email = employeeobject.email
    mailbody = mailbody + '\n' + "Thanks." + '\n' + "YAAS Team."
    if is_connected():
        send_mail("New Auction", mailbody, "YAAS Admin", [email])
    else:
        messages.error(request, 'Network Error. Check your internet connection.')
    return


# python3 manage.py process_tasks
def _post_tasks(request, auction_id):
    result = set_deadline(int(auction_id))
    return result


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
