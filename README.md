# right-now
right-now is a simple script that runs on command line and helps you track what you have been doing throughout the day.

1. Prerequisites
   python3 / python2

2. Installation

    # Clone this Repo

    # add alias to your bash_profile/bash_rc/zshrc

       alias rnw='python3 <path to the clone>/right-now/main.py'  

    # Install Libraries

       pip3 install -r requirements.txt
    
     
    # generate slack token at https://api.slack.com/legacy/custom-integrations/legacy-tokens
    
3. Usage
   Start an Activity:
       ``` rnw add "Planning the Day" ```
   Check All Events For Today:
       ``` rnw show ```
   Check Time Taken For Each Event:
       ``` rnw report ```
   Undo your last activity
       ``` rnw undo ```

4. toDos
     Better Slack handling
     Make this Easily installable
