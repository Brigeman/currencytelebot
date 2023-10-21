Currency Converter Bot

Introduction

The Currency Converter Bot is a Telegram bot that allows users to convert currency values based on real-time exchange rates. The bot is powered by the Free Currency API, providing up-to-date information on various currencies.

Prerequisites

To run the Currency Converter Bot, you need to have the following:

Python 3.x installed on your system.
Telebot Python package.
An API key from Free Currency API.
Installation

Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/Brigeman/currencytelebot
Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required Python packages:
Copy code
pip install pyTelegramBotAPI requests (pip install -r requirements.txt)
Update the config.py file with your API key obtained from Free Currency API.
Usage

Start the bot by running main.py:
css
Copy code
python main.py
Open Telegram and find the bot by its username.
Start a chat with the bot and follow the instructions below to convert currency:
Send a message in the format: <source_currency> <target_currency> <amount>.
Example: USD EUR 100.
The bot will reply with the converted currency value, rounded to two decimal places.
Available Commands

/start or /help: Get instructions on how to use the bot.
/values: View the list of available currencies for conversion.
Example

User Input: USD EUR 100
Bot Response: 100 USD = 89.43 EUR
Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.
