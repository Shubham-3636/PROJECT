#pip install python-telegram-bot
#pip install pytelegrambotapi
import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time

updater = Updater("5421809650:AAFThj4Yr3j2lvGwgmtxdDeIvsJXZ8CyP7w", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the CU_Bot. Please write\
    /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /website - To get Website URL
    /youtube - To get the Youtube URL
    /linkedin - To get the LinkedIn profile URL
    /facebook - To get Facebook URL
    /instagram - To get Instagram URL
    /twitter - To get the Twitter URL
    /admission22 - To get admission URL
    /admission_mail - TO get  Admission Email""")


def website_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Website link =>\
        https://www.cuchd.in/")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Youtube Link =>\
        https://youtube.com/c/ChandigarhuniversityAcIn")


def linkedin_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "LinkedIn URL => \
        https://www.linkedin.com/school/chandigarh-university/")


def facebook_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Facebook URL => \
        https://m.facebook.com/chandigarhuniversitygharuan")


def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Instagram URL => \
        https://instagram.com/chandigarhuniversity?igshid=YmMyMTA2M2Y=")


def twitter_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Twitter URL => \
        https://twitter.com/Chandigarh_uni?t=IA3qzhLuLmTRE7JjMxpaIg&s=09")


def admission22_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Admission22 URL => \
        https://cucet.cuchd.in/index.aspx?type=utube")


def admission_mail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Admission Email URL => \
        admissions@cumail.com")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin_url))
updater.dispatcher.add_handler(CommandHandler('admission_mail', admission_mail_url))
updater.dispatcher.add_handler(CommandHandler('facebook', facebook_url))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('twitter', twitter_url))
updater.dispatcher.add_handler(CommandHandler('admission22', admission22_url))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
while True:
    try:
        updater.start_polling()
    except:
        time.sleep(5)
