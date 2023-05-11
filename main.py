import os
import json
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()  # load environment variables from .env file

# get bot token from environment variables
bot_token = os.getenv('BOT_TOKEN')

# create updater instance
updater = Updater(token=bot_token, use_context=True)

# load owner information from config file
with open('config.json', 'r') as f:
    config = json.load(f)
    owner_name = config['owner']['name']
    owner_social_link = config['owner']['social_link']

# define welcome message
welcome_message = f"Welcome to the bot, {owner_name}! Check out my social link: {owner_social_link}."

# define command handler for /start command
def start(update, context):
    # send welcome message
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

# add command handler to the updater
updater.dispatcher.add_handler(CommandHandler('start', start))

# start the bot
updater.start_polling()

# run the bot until Ctrl-C is pressed
updater.idle()
