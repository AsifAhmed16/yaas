from background_task import background
from logging import getLogger
from .models import Auction, Auction_Status

logger = getLogger(__name__)


@background(schedule=15)
def set_deadline(auction_id):
    Auction.objects.filter(id=auction_id).update(status_id=Auction_Status.objects.get(status="Due"))
    message = "Deadline Met"
    print(message)
    return message
