from background_task import background
from logging import getLogger
from .models import Auction, Auction_Status, Bid
from account.models import User
from django.core.mail import send_mail

logger = getLogger(__name__)
# python3 manage.py process_tasks


# @background(schedule=15)
@background(schedule=259200)
def set_deadline(auction_id):
    Auction.objects.filter(id=auction_id).update(status_id=Auction_Status.objects.get(status="Due").id)
    message = "Deadline Met"
    print(message)
    return message


@background(schedule=266400)
def resolve_auction(auction_id):
    Auction.objects.filter(id=auction_id).update(status_id=Auction_Status.objects.get(status="Adjudicated").id)
    resolve_mail_notification(auction_id)
    message = "Auction Adjudicated"
    print(message)
    return message


def resolve_mail_notification(res_auc):
    auc_obj = Auction.objects.get(id=res_auc)
    bid_objs = Bid.objects.filter(auction_id=auc_obj.id)
    max_bid = bid_objs.order_by('-bid_price')[0]
    s_mailbody = "Dear " + auc_obj.seller.username + "," + '\n' + '\n' \
                 + "The Auction Created By You as Stated Below Has Been Resolved." + '\n' + '\n' \
                 + "Auction Details :::: Title - " + auc_obj.title + " Price - " + str(auc_obj.min_price) + " Max Bid Price - " + str(max_bid.bid_price) + " Bid Winner - " + str(max_bid.bidder.username) + '\n' + '\n'
    s_email = auc_obj.seller.email
    s_mailbody = s_mailbody + '\n' + "Thanks." + '\n' + "YAAS Team."

    send_mail("New Auction", s_mailbody, "YAAS Admin", [s_email])
    email_list = []
    for each in bid_objs:
        b_email = each.bidder.email
        email_list.append(b_email)
    email_list = list(set(email_list))
    for each in email_list:
        usr = User.objects.get(email=each)
        b_mailbody = "Dear " + usr.username + "," + '\n' + '\n' + "A bid you made has been Resolved.." + '\n' + '\n' \
                     + " Max Bid Price - " + str(max_bid.bid_price) + " Bid Winner - " + str(max_bid.bidder.username) + '\n' + '\n'
        b_mailbody = b_mailbody + '\n' + "Thanks." + '\n' + "YAAS Team."
        send_mail("New Auction", b_mailbody, "YAAS Admin", [each])
    return
