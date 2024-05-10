import telebot
from telebot.types import InputMediaPhoto
import random
from telebot import types
token="7181433193:AAG07jOHaRsdlqwMzv2kJNtSogayq_GvcHQ"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Приветствую в тг боте ресторана Kriper!\n/start Приветствие\
                     \n/about О разрабтчиках\
                     \n/help список команд\
                     \n/restaurant список ресторанов\
                     \n/food когда не знаешь что взять \
                     ")

@bot.message_handler(commands=['restaurant'])
def send_photos(message):
    bot.send_message(message.chat.id,'Ресторан в джунглях')    
    bot.send_media_group(message.chat.id,
    [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in ['TelegramBot/jungle_1.png', \
                                                                    'TelegramBot/jungle_2.png', \
                                                                    'TelegramBot/jungle_3.png', \
                                                                    'TelegramBot/jungle_4.png', \
                                                                    'TelegramBot/jungle_5.png', ]])

    bot.send_message(message.chat.id,'Ресторан на горе')
    bot.send_media_group(message.chat.id,
    [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in ['TelegramBot/mountain_1.png', \
                                                                    'TelegramBot/mountain_2.png', \
                                                                    'TelegramBot/mountain_3.png', \
                                                                    'TelegramBot/mountain_4.png', ]])
    
    bot.send_message(message.chat.id,'Ресторан в адских условиях')
    bot.send_media_group(message.chat.id,
    [telebot.types.InputMediaPhoto(open(photo, 'rb')) for photo in ['TelegramBot/nether_1.png', \
                                                                    'TelegramBot/nether_2.png', \
                                                                    'TelegramBot/nether_3.png', ]])
    
@bot.message_handler(commands=['food'])
def send_food(message):
    food=['Торт','Тушёный кролик','Жареная говядина','Жареная свинина','Тыквенный пирог','Подозрительный суп','Зачарованное золотое яблоко','Печенье','Свекольный суп','Паучий глаз','Гнилая плоть','Ядовитый картофель']
    foodChoice=random.choice(food)
    if foodChoice=='Паучий глаз':
        bot.send_message(message.chat.id,f'{foodChoice}\nБеее!? Тебе не повезло, возьми что-нибудь по вкуснее!')
    elif foodChoice=='Гнилая плоть':
        bot.send_message(message.chat.id,f'{foodChoice}\nБеее!? Тебе не повезло, возьми что-нибудь по вкуснее!')
    elif foodChoice=='Ядовитый картофель':
        bot.send_message(message.chat.id,f'{foodChoice}\nБеее!? Тебе не повезло, возьми что-нибудь по вкуснее!')
    elif foodChoice=='Подозрительный суп':
        bot.send_message(message.chat.id,f'{foodChoice}\nВау! Мы даже не знаем что с тобой случиться когда съешь! Бери на свой страх и риск!')
    else:
        bot.send_message(message.chat.id,f'{foodChoice}\nМММ! Это звучит вкусно! Давай попробуй!')
        
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,"/start Приветствие\
                     \n/about О разрабтчиках\
                     \n/help список команд\
                     \n/restaurant список ресторанов\
                     \n/food когда не знаешь что взять \
                     ")
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_start= types.InlineKeyboardButton(text='Приветствие', callback_data='btn_start')
    btn_about= types.InlineKeyboardButton(text='О разрабтчиках', callback_data='btn_about')
    btn_help= types.InlineKeyboardButton(text='список команд', callback_data='btn_help')
    btn_restaurant= types.InlineKeyboardButton(text='список ресторанов', callback_data='btn_restaurant')
    btn_food= types.InlineKeyboardButton(text='когда не знаешь что взять', callback_data='btn_food')
    markup.add(btn_start,btn_about,btn_help,btn_restaurant,btn_food)
    bot.send_message(message.chat.id, "Нажми давай", reply_markup = markup)

@bot.message_handler(commands=['about'])
def about_message(message):
    bot.send_message(message.chat.id,"https://vk.com/wiuss")

    bot.send_message(message.chat.id,"https://vk.com/netakusik3333")  

@bot.callback_query_handler(func=lambda callback: callback.data)    
def check_callback_data(callback):    
    if callback.data == 'btn_start':
        bot.send_message(callback.message.chat.id, "Команда приветствие,нужна для начала работы тг-бот")
    elif callback.data == 'btn_about':
        bot.send_message(callback.message.chat.id, "Команда о разработчиках, нужна чтобы узнать информацию о разработчиках или связаться с ним")
    elif callback.data == 'btn_help':
        bot.send_message(callback.message.chat.id, "Команда помощь, нужна чтобы узнать информацию о командах")
    elif callback.data == 'btn_restaurant':
        bot.send_message(callback.message.chat.id, "Команда ресторан, нужна чтобы посмотреть рестораны")
    elif callback.data == 'btn_food':
        bot.send_message(callback.message.chat.id, "Команда что поесть, нужна чтобы помочь выбрать блюдо")
    else:
        bot.send_message(callback.message.chat.id, "Что-то случилось нехорошое!")

bot.infinity_polling()