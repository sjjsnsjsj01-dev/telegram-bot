import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

# ---- start command ----
@bot.message_handler(commands=['start'])
def start(message):

    markup = InlineKeyboardMarkup()

    btn = InlineKeyboardButton(
        "🚀 فتح منصة القناص VIP",
        web_app=WebAppInfo("https://sjjsnsjsj01-dev.github.io/Malek_Aldahab/")
    )

    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "👑 مرحباً بك في منصة القناص VIP\nاضغط الزر لفتح المنصة:",
        reply_markup=markup
    )

# ---- web server ----
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# ---- run bot ----
keep_alive()
bot.infinity_polling()
