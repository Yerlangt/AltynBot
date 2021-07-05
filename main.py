import telebot
from telebot import types
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot("1528218813:AAFIGAQ3w_3turdq3B13OrnKTyAhi27YeAU")

button_method = KeyboardButton('Method of production 🛠')
button_catalog = KeyboardButton('Catalog 💽')
button_cart = KeyboardButton('Shopping cart 🛒')
button_feedback = KeyboardButton('Feedback 📞')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_method)
greet_kb.add(button_catalog)
greet_kb.add(button_cart)
greet_kb.add(button_feedback)
cart = []


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global cart
    cart = []
    bot.send_message(message.chat.id, 'Welcome to the online shop of vinyl record of Kazakh classical music',
                     reply_markup=greet_kb)


inline_btn_1 = InlineKeyboardButton('Details', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Buy', callback_data='button2')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb1.add(inline_btn_2)

inline_btn_3 = InlineKeyboardButton('Details', callback_data='button3')
inline_btn_4 = InlineKeyboardButton('Buy', callback_data='button4')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_3)
inline_kb2.add(inline_btn_4)


@bot.callback_query_handler(func=lambda c: c.data == 'button1')
def test_callback(call):
    bot.send_message(call.message.chat.id, 'https://www.youtube.com/watch?v=QR8bnM-GvDk',
                     reply_markup=greet_kb)


@bot.callback_query_handler(func=lambda c: c.data == 'button3')
def test_callback(call):
    bot.send_message(call.message.chat.id, 'https://www.youtube.com/watch?v=ojfn8ivjNoo',
                     reply_markup=greet_kb)


@bot.callback_query_handler(func=lambda c: c.data == 'button2')
def test_callback(call):
    pass


@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'Method of production' in message.text:
        bot.send_message(message.chat.id, 'https://youtu.be/sHkWpCLzdko',
                         reply_markup=greet_kb)
    elif 'Catalog' in message.text:

        bot.send_message(message.chat.id, 'Our products')
        bot.send_message(message.chat.id, "Kurmangazy's masterpiece - Adai")
        bot.send_photo(message.chat.id, photo=open('tmp/1.jpg', 'rb'), reply_markup=inline_kb1)

        bot.send_message(message.chat.id, "Seken Turysbekov - Konil Tolqyny")
        bot.send_photo(message.chat.id, photo=open('tmp/2.jpg', 'rb'), reply_markup=inline_kb2)
    elif 'Shopping cart' in message.text:
        bot.send_message(message.chat.id, "Kurmangazy's masterpiece - Adai (15$)")
        bot.send_message(message.chat.id, "Seken Turysbekov - Konil Tolqyny (15$)")
    elif 'Feedback' in message.text:
        bot.send_message(message.chat.id, "email - berikov04@gmail.com")
    else:
        bot.send_message(message.chat.id, "I didn't get it")


bot.polling(none_stop=True)
