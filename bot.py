import telebot
import threading
import time
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    # إرسال صورة الترحيب
    photo_url = "https://i.imgur.com/6Iej2c3.jpeg"

    text = """
👑 مرحباً بك في منصة القناص VIP

منصة متخصصة في تقديم توصيات تداول احترافية.

📊 إشارات تداول دقيقة  
⚡ توصيات فورية  
📈 تحليلات احترافية  
💎 محتوى خاص VIP
"""

    bot.send_photo(message.chat.id, photo_url, caption=text)

    # انتظار ثانية
    time.sleep(1)

    # زر فتح الموقع
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        "🚀 دخول منصة القناص VIP",
        web_app=WebAppInfo("https://sjjsnsjsj01-dev.github.io/Malek_Aldahab/")
    )

    markup.add(button)

    bot.send_message(
        message.chat.id,
        "اضغط للدخول إلى المنصة:",
        reply_markup=markup
    )

# ---- web server ----
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()
bot.infinity_polling()
