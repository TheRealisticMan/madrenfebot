import telebot

bot = telebot.TeleBot("346767451:AAG6yFuIV5AFO3hB5jY1BDHerhV4DvDS-54")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()
