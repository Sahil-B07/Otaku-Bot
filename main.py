import telebot
import os

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


gifFile = "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/5eeea355389655.59822ff824b72.gif"
audioFile = "https://mp3gaga.com/wp-content/uploads/2021/03/COOLIO-GANGSTER-PARADISE-Mp3gaga.com_.mp3"


@bot.message_handler(commands=['music','gif'])
def music_on(message):
	if message.text == "/gif":
		bot.send_document(message.chat.id,gifFile)
	elif message.text == "/music":
		# bot.send_audio("@otaku_testing", audioFile)  # send the file to the channel
		bot.send_audio(message.chat.id, audioFile)
		


bot.infinity_polling()
