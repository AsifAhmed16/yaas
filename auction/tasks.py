from background_task import background
from logging import getLogger

logger = getLogger(__name__)


@background(schedule=15)
def demo_task(message):
    print(message)
    return message
