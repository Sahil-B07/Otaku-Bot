import telebot


bot = telebot.TeleBot("2103403524:AAFIgabvCWUSw2f_zXD973vJZY9Noipf2iQ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


gifFile = "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif"
audioFile = open('/Users/sahilbhor/Downloads/GunShotSnglShotIn PE1097906.mp3', 'rb')


@bot.message_handler(commands=['music','gif'])
def music_on(message):
	if message.text == "/gif":
		bot.send_document(message.chat.id,gifFile)
	elif message.text == "/music":
		bot.send_audio(message.chat.id, audioFile)


bot.infinity_polling()