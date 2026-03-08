import telebot
import threading
from flask import Flask

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "البوت يعمل بنجاح!")

# ---- web server ----
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# ---- run bot ----
keep_alive()
bot.infinity_polling()
