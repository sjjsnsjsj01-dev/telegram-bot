import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    text = """
👑 مرحباً بك في بوابة عالم القناص VIP

📊 منصة تداول الذهب والعملات
📈 تحليلات وتوصيات احترافية
⚡ إشارات يومية

اضغط الزر للدخول إلى المنصة 👇
"""

    keyboard = InlineKeyboardMarkup()

    button = InlineKeyboardButton(
        "🚀 دخول المنصة",
        web_app=WebAppInfo("https://sjjsnsjsj01-dev.github.io/Malek_Aldahab/")
    )

    keyboard.add(button)

    bot.send_message(
        message.chat.id,
        text,
        reply_markup=keyboard
    )


# تشغيل السيرفر (مطلوب لـ Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    t = threading.Thread(target=run)
    t.start()


keep_alive()

print("Bot started...")
bot.infinity_polling()
