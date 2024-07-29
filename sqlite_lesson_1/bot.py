import telebot

API_TOKEN = "6346916937:AAHJNHzLthJQKyhJQxefHfyghIlcm_GV7gs"  # should be moved to env

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    bot.reply_to(
        message,
        """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""",
    )


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()
