# PulseCheckAPI


## Overview

PulseCheckAPI is a Python-based API monitoring tool that checks the availability of a specified API and sends notifications via Telegram if the API is down. The script is designed to be deployed on Heroku ([https://heroku.com]()).

## Features

* Monitors API availability
* Sends Telegram notifications if the API is down
* Logs API status

## Deployable on Heroku

* Prerequisites
* Python 3.x
* Heroku account
* Telegram Bot Token
* Git

## Installation

### Local Setup

Clone the repository

`git clone https://github.com/Ingvarsvensen/PulseCheckAPI.git`

Navigate to the project directory

`cd PulseCheckAPI`

### Install the required packages

`pip install -r requirements.txt`

Create a .env file and add your environment variables

`TELEGRAM_TOKEN=your_telegram_token_here`<br>
`CHAT_ID=your_chat_id_here`<br>
`API_LINK=your_api_link_here`

Run the script

`python main.py`

## Heroku Deployment

Login to Heroku

`heroku login`

Create a new Heroku app

`heroku create PulseCheckAPI`

Add a Procfile and requirements.txt to your project if not already present.

Commit your changes

`git add .`<br>
`git commit -m "Prepare for Heroku deployment"`

Push to Heroku

`git push heroku master`

Set environment variables on Heroku

`heroku config:set TELEGRAM_TOKEN=your_telegram_token_here`<br>
`heroku config:set CHAT_ID=your_chat_id_here`<br>
`heroku config:set API_LINK=your_api_link_here`

Scale your worker

`heroku ps:scale worker=1`

## Usage

Once deployed, the script will automatically check the API at regular intervals. If the API is down, a Telegram message will be sent to the specified chat ID.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
