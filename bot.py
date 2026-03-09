import telebot
import threading
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8231171750:AAEhl2vzp5RcTHr0y2OyQhNGjk_jkl3I7WA"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    photo = "https://images.unsplash.com/photo-1610375461246-83df859d849d"

    text = """
👑 *مرحباً بك في منصة القناص VIP*

منصة احترافية لتداول الذهب والعملات الرقمية.

📊 إشارات تداول دقيقة  
⚡ توصيات فورية  
📈 تحليلات احترافية  
💎 عضوية VIP حصرية  

اختر أحد الخيارات 👇
"""

    keyboard = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton(
        "🚀 دخول المنصة",
        web_app=WebAppInfo(
            url="https://sjjsnsjsj01-dev.github.io/Malek_Aldahab/"
        )
    )

    btn2 = InlineKeyboardButton(
        "📢 قناة التوصيات",
        url="https://t.me/yourchannel"
    )

    btn3 = InlineKeyboardButton(
        "💬 الدعم الفني",
        url="https://t.me/yourusername"
    )

    keyboard.add(btn1)
    keyboard.add(btn2, btn3)

    bot.send_photo(
        message.chat.id,
        photo,
        caption=text,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

# ----- Web server for Render -----

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot running"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

keep_alive()

bot.infinity_polling()
