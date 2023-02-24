import telebot
from telebot import types

bot = telebot.TeleBot('6158927267:AAGZZLjbCPM2NGMdnRfAW-49JK7rojMuWHY')

@bot.message_handler(commands=['start',])
def start_message(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, f'Вас приветствует бот!')
    bot.register_next_step_handler(msg, inline)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    chat_id = c.chat.id
    
    msg = bot.send_message(chat_id, c.text)
    bot.register_next_step_handler(msg, inline)


# @bot.callback_query_handler(func=lambda c: True)
# def function1(c):
#     chat_id = c.chat.id
#     msg = bot.send_message(chat_id, price_history(c.text), reply_markup=inline_keyboard)
#     bot.register_next_step_handler(msg, inline)


# @bot.callback_query_handler(func=lambda c: True)
# def function2(c):
#     chat_id = c.chat.id
#     msg = bot.send_message(chat_id, chek_amount(c.text), reply_markup=inline_keyboard)
#     bot.register_next_step_handler(msg, inline)


# @bot.callback_query_handler(func=lambda c: True)
# def function3(c):
#     chat_id = c.chat.id
#     msg = bot.send_message(chat_id, sales_report(c.text), reply_markup=inline_keyboard)
#     bot.register_next_step_handler(msg, inline)


# @bot.callback_query_handler(func=lambda c: True)
# def function4(c):
#     chat_id = c.chat.id
#     print(product_position(c.text))
#     msg = bot.send_message(chat_id, product_position(c.text), reply_markup=inline_keyboard)
#     bot.register_next_step_handler(msg, inline)


# @bot.callback_query_handler(func=lambda c: True)
# def function5(c):
#     chat_id = c.chat.id
#     article_and_new_title = c.text
#     change_title(article_and_new_title, WB_token, x_supplier_id)
#     sent_msg = bot.send_message(chat_id, "Название успешно изменено")
#     bot.register_next_step_handler(sent_msg, inline)


# @bot.callback_query_handler(func=lambda c: True)
# def function6(c):
#     global WB_token, x_supplier_id
#     chat_id = c.chat.id
#     x_supplier_id = c.text.split(' ')[0]
#     WB_token = c.text.split(' ')[1]
#     sent_msg = bot.send_message(chat_id, "Введите артикул и название товара")
#     bot.register_next_step_handler(sent_msg, function5)


bot.polling()