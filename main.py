import logging
import os
import pickle

from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from daily_message import DailyMessage
from weekly_message import WeeklyMessage


os.environ['SLACK_BOT_TOKEN'] = ''
os.environ['SLACK_SIGNING_SECRET'] = ''

client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
logger = logging.getLogger(__name__)


def save_object(obj, filename):
    try:
        with open(filename, "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        logger.error("Error during pickling object (Possibly unsupported):", ex)


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        logger.error("Error during unpickling object (Possibly unsupported):", ex)


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    location_dict = load_object("locationData.pickle")
    user_ids = load_object("userData.pickle")

    print(user_ids)

    if datetime.now().strftime("%a") == "Fri":
        for location in location_dict.items():
            try:
                message_builder = WeeklyMessage(location[1][2], location)
                weekly_message = message_builder.get_message_payload()
                result = client.chat_postMessage(**weekly_message)

                logger.info(result)
            except SlackApiError as e:
                logger.error("Error posting weekly message: {}".format(e))

    for city in user_ids.items():
        for user in city[1]:
            try:
                location = (city[0], location_dict[city[0]])
                message_builder = DailyMessage(user, location)
                daily_message = message_builder.get_message_payload()
                result = client.chat_postMessage(**daily_message)

                logger.info(result)
            except SlackApiError as e:
                logger.error("Error posting daily message: {}".format(e))
