import logging
import os

from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from daily_message import DailyMessage
from weekly_message import WeeklyMessage

os.environ['SLACK_BOT_TOKEN'] = ''
client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
logger = logging.getLogger(__name__)
user_ids = {"U02AUH5TLHF": "Boston"}
# , "U028412LLKT": "Boston", "U012HHZRUJD": "Boston", "U97PAM3N0": "Boston", }
location_dict = {"Boston": ["Middlesex", "Massachusetts", "C4ZM85PE3"]}  # ,
#  "Durham": ["Durham", "North%20Carolina", "C5XDHQT6V"],
# "Tampa": ["Pinellas", "Florida", "C8XV8KK40"]}

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    if datetime.now().strftime("%a") == "Fri":
        for location in location_dict.items():
            try:
                message_builder = WeeklyMessage(location[1][2], location)
                weekly_message = message_builder.get_message_payload()
                # result = client.chat_postMessage(**weekly_message)

                # logger.info(result)
            except SlackApiError as e:
                logger.error("Error posting weekly message: {}".format(e))

    for user in user_ids.items():
        location = (user[1], location_dict.get(user[1]))
        try:
            message_builder = DailyMessage(user[0], location)
            daily_message = message_builder.get_message_payload()
            result = client.chat_postMessage(**daily_message)

            logger.info(result)
        except SlackApiError as e:
            logger.error("Error posting daily message: {}".format(e))
