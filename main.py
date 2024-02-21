import telebot

bot = telebot.TeleBot("7020192176:AAG9G16SSQDgXMI8_3674vIVc4WXgi01UM8")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет!")

bot.polling()

