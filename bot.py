import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    photo1 = "https://images.unsplash.com/photo-1610375461246-83df859d849d"
    photo2 = "https://dummyimage.com/800x400/000/fff.jpg&text=Gold+Trading"

    text = """
👑 مرحباً بك في منصة VIP

📊 تداول الذهب والعملات
⚡ توصيات يومية
💎 تحليلات احترافية

ابدأ الآن بالدخول إلى المنصة 👇
"""

    keyboard = InlineKeyboardMarkup(row_width=1)

    btn = InlineKeyboardButton(
        "🚀 دخول المنصة",
        web_app=WebAppInfo(url="https://sjjsnsjsj01-dev.github.io/Malek_Alda/")
    )

    keyboard.add(btn)

    # ارسال الصورة الاولى
    bot.send_photo(
        message.chat.id,
        photo1,
        caption=text,
        reply_markup=keyboard
    )

    # ارسال الصورة الثانية
    bot.send_photo(
        message.chat.id,
        photo2
    )


# سيرفر لتشغيل البوت على Render
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
