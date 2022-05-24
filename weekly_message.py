import urllib.request
import json


class WeeklyMessage:
    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel, location_data):
        self.channel = channel
        self.icon_emoji = ":mask:"
        self.city = location_data[0]
        self.location_data = location_data
        self.risk_level = self.get_risk_level()
        self.text = "weekly_covid_risk_level_message"
        self.username = "covidbot"

    def get_message_payload(self):
        return {
            "channel": self.channel,
            "icon_emoji": self.icon_emoji,
            "text": self.text,
            "username": self.username,
            "blocks": [
                *self._get_greeting_block(),
                *self._get_info_block(),
                self.DIVIDER_BLOCK,

            ],
        }

    def _get_greeting_block(self):
        text = (
            "Good Morning :wave: \n"
        )
        return self._get_section_block(text)

    def _get_info_block(self):
        text = (
            self.get_weekly_message()
        )
        return self._get_section_block(text)

    @staticmethod
    def _get_section_block(text):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": text}},
        ]

    def get_weekly_message(self):
        message = "The covid risk level in " + self.city + " is " + self.risk_level + ". :mask: \n"

        if self.risk_level == "High":
            return message + "Working in-person is optional next week.\n"

        return message + "Working in-person is required Tues, Wed, and Thurs next week.\n"

    def get_risk_level(self):
        with urllib.request.urlopen(
                "https://data.cdc.gov/resource/3nnm-4jni.json?$limit=1&$order=date_updated%20DESC&county="
                + self.location_data[1][0] + "%20County&state=" + self.location_data[1][1]) as url:
            data = json.loads(url.read().decode())
        return data[0]['covid_19_community_level']
