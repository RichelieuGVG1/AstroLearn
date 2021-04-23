import telebot
from telebot import types
from game import play, create_random
import random



bot = telebot.TeleBot('1736780989:AAHppwjEPVMt-X4icSQOsm-zxxGOkcQyvUE')

@bot.message_handler(commands=['start'])
def send_welcome(message):

    with open('ded.txt', 'r') as file:
    	count=int(file.read())
    	file.close()
    count=0
    with open('ded.txt', 'w') as file:
    	file.write(str(count))
    	file.close()

    bot.send_message(message.chat.id, f"Я `бот`. *Приятно* _познакомиться_ ", parse_mode= 'Markdown', reply_markup=keyboard())
    bot.send_photo(message.chat.id, 'https://upload.wikimedia.org/wikipedia/commons/3/36/Retivow.jpg')

@bot.message_handler(commands=['learn'])
def send_welcome(message):
    get_messages(message)


@bot.message_handler(content_types=["text"] )
def get_messages(message):  
    
    chat_id = message.chat.id
    if message.text == 'Учиться📚' or message.text == 'Далее➡️':
    	learning(chat_id)
    elif message.text == 'Вернуться в меню💬' :
        menu(chat_id)
    elif message.text == 'Завершить игру⛔': 
        game_interrupted(chat_id)
    elif message.text == 'Сдать тест🖊️': 
        playing(chat_id)

    elif message.text == 'Помощь🚑':
    	help(chat_id)

    elif message.text == 'Следующий вопрос❓':
    	playing(chat_id)


    else:
    	bot.send_message(chat_id, 'Неизвестная команда. Попробуйте попадать пальцами по клавишам.', parse_mode= 'Markdown', reply_markup=keyboard())

    #bot.send_message(chat_id, f"{ded}", parse_mode= 'Markdown', reply_markup=keyboard())
    
@bot.callback_query_handler(func=lambda call1: not call1.data.startswith('t'))
def query_handler(call1):

    bot.answer_callback_query(callback_query_id=call1.id)
    answer = ''
    #call=call.data
    printed(call1)



def learning(chat_id):
    
	
    bot.send_message(chat_id, "Выберите созвездие:", parse_mode='HTML',reply_markup=answers())

def menu(chat_id):
    bot.send_message(chat_id, "Начните сызнова." ,parse_mode='HTML',reply_markup=keyboard())

def game_interrupted(chat_id):
    with open('ded.txt', 'r') as file:
    	count=int(file.read())
    	file.close()
    count=0
    with open('ded.txt', 'w') as file:
	    	file.write(str(count))
	    	file.close()
    bot.send_message(chat_id, "Вы позорно капитулировали. А ведь тест был проще простого!" ,parse_mode='HTML',reply_markup=keyboard())

def game_ended(chat_id):
    with open('ded.txt', 'r') as file:
    	count=int(file.read())
    	file.close()
    count=0
    with open('ded.txt', 'w') as file:
	    	file.write(str(count))
	    	file.close()
    bot.send_message(chat_id, "Игра завершена. Ваш результат:" ,parse_mode='HTML',reply_markup=keyboard())

def playing(chat_id):
    text = 'игра началась!'

    with open('ded.txt', 'r') as file:
    	count=int(file.read())
    	file.close()
    global answer
    pic, answer, out = create_random()


    bot.send_message(chat_id, 'Выберите верное название созвездия:', parse_mode='HTML', reply_markup=ans_key(answer,out))
    bot.send_photo(chat_id, pic)

    count+=1


    if count==11:
    	game_ended(chat_id)
    else:
	    with open('ded.txt', 'w') as file:
	    	file.write(str(count))
	    	file.close()





def help(chat_id):
    text="Здесь вы научитесь различать созвездия Зимнего полушария на ночном небе. На выбор я предлагаю две функции: *обучение и проверка знаний*\nЧтобы начать обучение, нажмите клавишу _Учиться_. Вам будут предложены для ознакомления схемы созвездий и краткое описание.\nЕсли вы уверены в своих знаниях, нажмите клавишу _Сдать тест_. По картинке постарайтесь отгадать, что на ней изображено.\n\n*Нажмите кнопку в меню, чтобы продолжить*"
    bot.send_message(chat_id, text, parse_mode= 'Markdown', reply_markup=keyboard())

@bot.callback_query_handler(func=lambda call1: not call1.data.startswith('t'))
def printed(call1):
    bot.answer_callback_query(callback_query_id=call1.id, text='Материал изучен')
    data=play()
    out=data[int(call1.data)]
    bot.send_photo(call1.message.chat.id, out[0])
    bot.send_message(call1.message.chat.id, out[1], parse_mode='Markdown', reply_markup=k2())



@bot.callback_query_handler(func=lambda call: call.data.startswith('t'))
def key_call(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Ответ принят')
    #bot.send_message(call.message.chat.id, f"{answer}, {call.data[1:]}", parse_mode='HTML',reply_markup=keyboard1())
    if int(call.data[1:]) == int(answer):
        bot.send_message(call.message.chat.id, '*Ваш ответ верный!*✅', parse_mode='Markdown',reply_markup=keyboard1())
    else:
    	bot.send_message(call.message.chat.id, '*Ваш ответ неверный*❌', parse_mode='Markdown',reply_markup=keyboard1())

def ans_key(answer, out):
    markup = telebot.types.InlineKeyboardMarkup()

    markup.add(telebot.types.InlineKeyboardButton(text=out[0], callback_data='t0'))
    markup.add(telebot.types.InlineKeyboardButton(text=out[1], callback_data='t1'))
    markup.add(telebot.types.InlineKeyboardButton(text=out[2], callback_data='t2'))
    markup.add(telebot.types.InlineKeyboardButton(text=out[3], callback_data='t3'))
    return markup

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn0 = types.KeyboardButton("Помощь🚑")
    btn1 = types.KeyboardButton('Учиться📚')
    btn2 = types.KeyboardButton('Сдать тест🖊️')

    markup.add(btn0)
    markup.add(btn1)
    markup.add(btn2)
    return markup  

def keyboard1():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn0 = types.KeyboardButton('Следующий вопрос❓')
    btn1 = types.KeyboardButton('Завершить игру⛔')

    markup.add(btn0)
    markup.add(btn1)
    return markup

def k2():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn0 = types.KeyboardButton('Вернуться в меню💬')
    btn1 = types.KeyboardButton('Далее➡️')

    markup.add(btn0)
    markup.add(btn1)
    return markup

def answers():
    
    markup = telebot.types.InlineKeyboardMarkup()

    markup.add(telebot.types.InlineKeyboardButton(text='Орион', callback_data='0'))
    markup.add(telebot.types.InlineKeyboardButton(text='Большая Медведица', callback_data='1'))
    markup.add(telebot.types.InlineKeyboardButton(text='Геркулес', callback_data='2'))
    markup.add(telebot.types.InlineKeyboardButton(text='Лебедь', callback_data='3'))
    markup.add(telebot.types.InlineKeyboardButton(text='Лира', callback_data='4'))
    markup.add(telebot.types.InlineKeyboardButton(text='Близнецы', callback_data='5'))
    markup.add(telebot.types.InlineKeyboardButton(text='Лев', callback_data='6'))
    markup.add(telebot.types.InlineKeyboardButton(text='Волопас', callback_data='7'))
    markup.add(telebot.types.InlineKeyboardButton(text='Персей', callback_data='8'))
    markup.add(telebot.types.InlineKeyboardButton(text='Малая Медведица', callback_data='9'))

    return markup

if __name__ == "__main__":
    bot.polling(none_stop=True)
