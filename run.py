"""Load Packages"""
from logging import Filter
from dotenv import load_dotenv
import os
from telegram.ext import *
from telegram.ext import commandhandler
from pyresponse import bot_response
import pyresponse

"""Load Envrionment variable"""
load_dotenv(os.path.join('.env'))

print("pyBot Started")

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi, I am pyBot. What can I do for you?")

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Help")

def handle_message(update, context):
    """handle the user message."""
    msg = str(update.message.text).lower()
    response = bot_response(msg)

    update.message.reply_text(response)

def error(update, context):
    """Print errors caused by Updates."""
    print(f"Update {update} caused error {context.error}")

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(os.getenv('APIKEY'), use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - print the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # handle all kind of errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()







    