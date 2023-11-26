import telebot
from C1 import *
token='6406936841:AAE0K6Tn7MHNDHRkexecSB4a-66dpTNRoHQ'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет. Напишите название вашей группы. Например 221-126')
    bot.register_next_step_handler(message, Group)

def Group(message):
    text=message.text


    if giveLink(text)[0]==5:
        bot.send_message(message.chat.id,giveLink(text)[1])

    elif giveLink(text)[0]==3:
        bot.send_message(message.chat.id,'сайт политеха не доступен, попробуйте ввести номер  группы  еще раз')
    elif giveLink(text)[0]==0:
         bot.send_message(message.chat.id,'введенной вами группы не существует, проверьте название группы на сайте политеха' )
    else:
        bot.send_message(message.chat.id,'произошла ошибка при получении ссылки, попробуйте еще раз или обратитесь в поддержку ')
'''def giveLink(message):'''


@bot.message_handler(content_types=['stop'])
def stop(message):
    bot.stop_bot()
    
bot.polling(none_stop=True)

