# -*- coding: utf-8 -*-
"""JustOursBot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Nw50AQVxSAbN3H_kMkze-5WNBKfvrQN
"""

! pip install pytelegrambotapi

import telebot
from time import sleep
import datetime

bot = telebot.TeleBot('1029253111:AAG-6Ju6oOSbcaNdvy-WESfeSQK0Rd5cX8I')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row(telebot.types.InlineKeyboardButton('Добавить заметки'), telebot.types.InlineKeyboardButton('Пока')) 


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Ты выбрал команду /start и JustOursBot начал работать', reply_markup=keyboard1)
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgY143B_L9r4x7N40vIKgprzb9jMOGAAIjAAP3AsgPlczTTWG9fUcYBA')

@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton('Message the developer', url='telegram.me/dench327')
   )
   bot.send_message(
       message.chat.id,
       '1) To receive a list of available currencies press /exchange.\n' +
       '2) Click on the currency you are interested in.\n' +
       '3) You will receive a message containing information regarding the source and the target currencies, ' +
       'buying rates and selling rates.\n' +
       '4) Click “Update” to receive the current information regarding the request. ' +
       'The bot will also show the difference between the previous and the current exchange rates.\n' +
       '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.',
       reply_markup=keyboard
   )
@bot.message_handler(commands=['end'])
def end_command(message):
  bot.send_message(message.chat.id, 'Ты выбрал команду /end, а значит нам пора прощаться(')
  bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIgZV43DjtWgQZxIrbYfHAq4uSDH0n-AAIbAAM7YCQU0JSc0CWOUYcYBA')
bot.polling(none_stop=True)