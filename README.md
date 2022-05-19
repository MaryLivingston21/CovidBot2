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