import logging
import os
import urllib.request, json

from datetime import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError



# # WebClient instantiates a client that can call API methods
# # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN'))
logger = logging.getLogger(__name__)
# ID of the channel you want to send the message to
user_ids = {"U02AUH5TLHF": "Boston", "U028412LLKT": "Boston", "U012HHZRUJD": "Boston", "U97PAM3N0": "Boston", }
location_dict = {"Boston": ["Middlesex", "Massachusetts", "C4ZM85PE3"],
                 "Durham": ["Durham", "North%20Carolina", "C5XDHQT6V"],
                "Tampa": ["Pinellas", "Florida", "C8XV8KK40"]}


def get_risk_level(location):
    with urllib.request.urlopen(
            "https://data.cdc.gov/resource/3nnm-4jni.json?$limit=1&$order=date_updated%20DESC&county="
            + location[1][0] + "%20County&state=" + location[1][1]) as url:
        data = json.loads(url.read().decode())

    return data[0]['covid_19_community_level']


def get_daily_message(location):
    risk_level = get_risk_level(location)
    day_of_week = datetime.now().strftime("%A")
    month = datetime.now().strftime("%B")
    day = datetime.now().strftime("%d")

    message = "Good Morning :wave: \nToday is " + day_of_week + " " + month + " " + day + \
              ". \nThe covid risk level in " + location[0] + " is " + risk_level + \
              ". :mask: \n"

    if day_of_week == ("Monday" or "Friday") or risk_level == "High":
        return message + "Working in-person is optional today.\n"

    return message + "Working in-person is required today.\n"


def get_weekly_message(location):
    risk_level = get_risk_level(location)

    message = "Good Morning :wave: \nThe covid risk level in " + location[0] + \
              " is " + risk_level + ". :mask: \n"

    if risk_level == "High":
        return message + "Working in-person is optional next week.\n"

    return message + "Working in-person is required Tues, Wed, and Thurs, next week.\n"


if __name__ == '__main__':
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    if datetime.now().strftime("%a") == "Fri":
        for location in location_dict.items():
            try:
                result = client.chat_postMessage(channel=location[1][2],
                                                 text=get_weekly_message(location))
                logger.info(result)
            except SlackApiError as e:
                logger.error("Error posting message: {}".format(e))

    for user in user_ids.items():
        location = (user[1], location_dict.get(user[1]))
        try:
            result = client.chat_postMessage(channel=user[0],
                                             text=get_daily_message(location))
            logger.info(result)
        except SlackApiError as e:
            logger.error("Error posting message: {}".format(e))
