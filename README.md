### Covid Bot
- Messages me the current covid risk level every weekday at 7am
- Used crontab and task scheduler to automate my scripts

#### Setup
- pip3 install python3
- cd CovidBot2
    - python3 -m venv env/
    - source env/bin/activate
- pip3 install slack_sdk

#### Automate python file - Mac
- pip3 install pyinstaller
- cd CovidBot2
    - pyinstaller --onefile main.py
- crontab -e

#### References
- [chat.postMessage](https://api.slack.com/methods/chat.postMessage)
- [chat.scheduleMessage](https://api.slack.com/methods/chat.scheduleMessage)
- [slackBot tutorial](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial)
- [automate python scripts](https://towardsdatascience.com/how-to-easily-automate-your-python-scripts-on-mac-and-windows-459388c9cc94)

#### Database
- [cdc database](https://data.cdc.gov/resource/3nnm-4jni.json)


##### Misc data
location_dict = {"Boston": ["Middlesex", "Massachusetts", "C4ZM85PE3"],
                 "Durham": ["Durham", "North%20Carolina", "C5XDHQT6V"],
                 "Tampa": ["Pinellas", "Florida", "C8XV8KK40"]}

user_ids = {"Boston": [], "Durham": [], "Tampa": []}

user_ids = {"Boston": ["U02AUH5TLHF", "U028412LLKT", "U012HHZRUJD", "U97PAM3N0"],
            "Durham": [], "Tampa": []}