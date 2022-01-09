# sdsp-bot

An elections bot for SDSP discord server

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
* [Dashboard](#dashboard)

## Installation

1. Clone the repository on your computer.
  ```bash
  git clone https://github.com/TroyeKizzz/sdsp-bot.git
  ```
2. Install python@3.7 from [python.org](https://www.python.org/downloads/).
3. Run install.bat file.

## Usage 

1. Create a file called token.py with the following contents but enter your real token in the gap.
  ```python
  token = "xxxxxxxxxxxxxxxxxxxxxxxx.xxxxxx.xxxxxxxxxxxxxxxxxxxxxxxxxxx" 
  ```
2. Configure you bot in cache.py file.

  | variable | description |
  | --- | --- |
  | `admin_id` | The ID of the first discord user who administrates the election |
  | `admin_id2` | The ID of the second discord user who administrates the election |
  | `channel_id` | The ID of the discord channel in which the elections are held |
  | `CANDIDATES` | The number of candidates in the election |
  | `election_msg` | The message that is sent by the bot when the election starts |
  
3. Start the bot by executing the start.bat file.

## Dashboard

The dashboard is available at https://sdsp.herokuapp.com.
You can also see the code used for the dashboard in [this repository](https://github.com/TroyeKizzz/sdsp-website).
