import telebot

TOKEN = '7748033957:AAEcAPfWBM8kRaEk6o-S_hT05EbqJZ6KlBQ'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()