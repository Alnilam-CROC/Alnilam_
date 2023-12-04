import telebot
from C1 import *


token='6406936841:AAE0K6Tn7MHNDHRkexecSB4a-66dpTNRoHQ'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет! Чтобы получить расписание, отправьте команду /get_timetable')
    print(message.chat.id)

@bot.message_handler(commands=['get_timetable'])
def gettimetable(message):
    bot.send_message(message.chat.id, 'Напишите название вашей группы. Например 221-126')
    bot.register_next_step_handler(message, Group)


def Group(message):
    v_id = 430657422
    user_id = message.from_user.id
    text=message.text
    if giveLink(text)[0]==5:
        bot.send_message(message.chat.id, giveLink(text)[1])
        document = open('Instruction_for_inserting_the_link.pdf', 'rb')
        bot.send_message(message.chat.id, 'В инструкции Вы найдёте, как подключить файл к google calendar')
        bot.send_document(message.chat.id,document)
        bot.send_message(v_id, user_id)
    elif giveLink(text)[0]==3:
        bot.send_message(message.chat.id,'Сайт политеха не доступен, попробуйте ввести номер  группы  еще раз')
    elif giveLink(text)[0]==1:
         bot.send_message(message.chat.id,'Введенной вами группы не существует, проверьте название группы на сайте политеха' )
    else:
        bot.send_message(message.chat.id,'Произошла ошибка при получении ссылки, попробуйте еще раз или обратитесь в поддержку ')
    bot.send_document(message.chat.id,"В случае возникновения технических шоколадок писать @VarvaraKh")



@bot.message_handler(content_types=['stop'])
def stop(message):
    bot.stop_bot()
    
bot.polling(none_stop=True)

