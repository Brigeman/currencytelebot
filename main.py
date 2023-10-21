import telebot
import config
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(config.TOKEN)
api_url = f'https://api.freecurrencyapi.com/v1/latest?apikey={config.API_KEY}' # hiding keys and tokens in the config.

@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    instructions = """
    Hi, I'm a currency conversion bot. To get the exchange rate, use the command in the following format:
    <name of the currency whose price you want to know> <name of the currency in which you want to know the price of the first currency> <quantity of the first currency>.
    For example: "USD EUR 100".
    To view the list of available currencies, use the /values command.
    """
    bot.send_message(message.chat.id, instructions)

@bot.message_handler(commands=['values'])
def send_available_currencies(message):
    available_currencies = """
    Available currencies:
    - USD (US Dollar)
    - EUR
    - RUB
    """
    bot.send_message(message.chat.id, available_currencies)

@bot.message_handler(content_types=['text'])
def convert_currency(message):
    try:
        text = message.text.split()
        if len(text) != 3:
            raise APIException("Invalid query format. Use the /help command for instructions.")

        base, quote, amount = [item.upper() for item in text]  # upper case sensitivity
        exchange_rate = CurrencyConverter.get_exchange_rate(api_url, base, quote, float(amount))
        result_message = f"{amount} {base} = {round(exchange_rate, 2)} {quote}" # round to the hundredths
        bot.send_message(message.chat.id, result_message)
    except APIException as e:
        bot.send_message(message.chat.id, f"Error: {e}")


if __name__ == '__main__':
    bot.polling(none_stop=True)
