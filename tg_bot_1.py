import telebot
from telebot import types

bot = telebot.TeleBot("6351723271:AAHwEKnnniEmiyfonIKEhPfQ2quLOcPzxQ8")


coin_list = {
    "Bitcoin": [[36164.59608078003, 35028.858184814453, 34164.84832763672, 37926.228046417236, 33898.80418777466], "bitcoin.jpg"],
    "Ethereum": [[3016.9944763183594, 2819.7269439697266, 2896.008014678955, 2895.5469131469727, 3055.419445037842], "ethereum.png"],
    "Dogecoin": [[0.2836251974105835, 0.2910567045211792, 0.2961850881576538, 0.2884641408920288, 0.3144310474395752], "dogecoin.png"],
    "Stellar": [[0.2857177734375, 0.2883213758468628, 0.28325304985046387, 0.28830666542053223, 0.28047358989715576], "stellar.jpg"],
    "NEM": [[0.29535410404205322, 0.29521589279174805, 0.2937316417694092, 0.2855343818664551, 0.29337096214294434], "nem.jpg"]
}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Bitcoin")
    item2 = types.KeyboardButton("Ethereum")
    item3 = types.KeyboardButton("Dogecoin")
    item4 = types.KeyboardButton("Stellar")
    item5 = types.KeyboardButton("NEM")
    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Привет, я - NeuroNut, бот, который поможет вам с прогнозированием цен в близжайшие 5 дней для следующих криптовалют:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text in coin_list.keys():
        img = open(coin_list[message.text][1], "rb")
        bot.send_photo(message.chat.id, img)
        list_val_str = [str(i) for i in coin_list[message.text][0]]
        text_mes = '\n-------------------------\n'.join(list_val_str)
        bot.send_message(message.chat.id, text=text_mes+"\n-------------------------\n*цена в USD*")
    else:
        bot.send_message(message.chat.id, text="У адекватных пользователей всё работает.")



bot.polling()