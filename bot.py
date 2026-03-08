import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    keyboard = InlineKeyboardMarkup()

    web = WebAppInfo(
        url="https://sjjsnsjsj01-dev.github.io/Malek_Aldahab/"
    )

    button = InlineKeyboardButton(
        "🚀 فتح منصة القناص VIP",
        web_app=web
    )

    keyboard.add(button)

    bot.send_message(
        message.chat.id,
        "👑 مرحباً بك في منصة القناص VIP",
        reply_markup=keyboard
    )

bot.infinity_polling()
