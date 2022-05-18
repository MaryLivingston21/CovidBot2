import logging
import os
import urllib.request, json

from datetime import date
from datetime import datetime
from datetime import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# # WebClient instantiates a client that can call API methods
# # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)
# ID of the channel you want to send the message to
channel_id = "U02AUH5TLHF"


def get_message():
    with urllib.request.urlopen(
            "https://data.cdc.gov/resource/3nnm-4jni.json?$limit=1&$order=date_updated%20DESC&county=Middlesex"
            "%20County&state=Massachusetts") as url:
        data = json.loads(url.read().decode())

    risk_level = data[0]['covid_19_community_level']
    day_of_week = datetime.now().strftime("%A")
    month = datetime.now().strftime("%B")
    day = datetime.now().strftime("%d")

    message = "Good Morning :wave: \nToday is " + \
              day_of_week + " " + month + " " + day + ". \nThe covid risk level in Middlesex, MA is " + \
              risk_level + " today. :mask: \n"

    if day_of_week == ("Monday" or "Friday") or risk_level == "High":
        message = message + "Working in-person is optional."

    return message


if datetime.now().hour < 7:
    today = date.today()
    scheduled_time = time(hour=7)
    schedule_timestamp = datetime.combine(today, scheduled_time).strftime('%s')
    try:
        result = client.chat_scheduleMessage(channel=channel_id, text=get_message(),
                                             post_at=schedule_timestamp)
        logger.info(result)
    except SlackApiError as e:
        logger.error("Error scheduling message: {}".format(e))
else:
    try:
        result = client.chat_postMessage(channel=channel_id, text=get_message())
        logger.info(result)
    except SlackApiError as e:
        logger.error("Error scheduling message: {}".format(e))
