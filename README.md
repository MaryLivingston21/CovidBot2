### Covid Bot
- Messages users the current covid risk level.  
- Messages #misc-boston the current covid risk level on Fridays
- Used crontab and task scheduler to automate my script
  - runs M-F at 7am

#### Setup
- pip3 install python3
- pip3 install slack_sdk

#### Setup before first run
- add SLACK_BOT_TOKEN, and SLACK_SIGNING_SECRET
- add data to main.py before load_object() methods are called
```
location_dict = {"Boston": ["Middlesex", "Massachusetts", "C4ZM85PE3"],
                 "Durham": ["Durham", "North%20Carolina", "C5XDHQT6V"],
                 "Tampa": ["Pinellas", "Florida", "C8XV8KK40"]}

user_ids = {"Boston": [], "Durham": [], "Tampa": []}

save_object(location_dict, "locationData.pickle")
save_object(user_ids, "userData.pickle")
```

#### Automate python file - Mac
- pip3 install pyinstaller
- cd CovidBot2
    - pyinstaller --onefile main.py
- crontab -e

#### References
- [chat.postMessage](https://api.slack.com/methods/chat.postMessage)
- [chat.scheduleMessage](https://api.slack.com/methods/chat.scheduleMessage)
- [slack api : bolt python documentation](https://github.com/slackapi/bolt-python/blob/main/README.md)
- [slackBot tutorial](https://github.com/slackapi/python-slack-sdk/tree/main/tutorial)
- [automate python scripts](https://towardsdatascience.com/how-to-easily-automate-your-python-scripts-on-mac-and-windows-459388c9cc94)

#### Database
- [cdc database](https://data.cdc.gov/resource/3nnm-4jni.json)