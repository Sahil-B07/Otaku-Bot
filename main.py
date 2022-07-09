
import telebot 
import os, requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand

API_KEY = os.getenv('Otaku_API')

bot = telebot.TeleBot(API_KEY)

def Imarkup():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(
		InlineKeyboardButton("🔎 Music", callback_data="music"),
		InlineKeyboardButton("🔎 Gifs", callback_data="gify"),
		InlineKeyboardButton("🔎 Search gif inline", callback_data="inlineGif")
	)
	return markup 

# Call back actions
@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
	if call.data == "music":
		bot.answer_callback_query(call.id, "")
		songs(call)
	elif call.data == "gify":
		bot.answer_callback_query(call.id, "")
		giffy(call)
	elif call.data == "inlineGif":
		bot.answer_callback_query(call.id, "Convention!")
		bot.send_message(call.from_user.id,"use /gif then type your context\nExample:\n1./gif anime\n2./gif smile\n...")


# Commands

@bot.message_handler(commands=['start', 'help', 'music','igif'])
def commands(message):
	userName = message.from_user.username

	if message.text == "/start":
		bot.reply_to(message, f"{userName}, how are you doing?", reply_markup=Imarkup())
	elif message.text == "/help":
		bot.reply_to(message, "/gif - get some intresting gifs\n/music - Listen to your fav music\ninline GIF - use /gif then type your context")
	elif message.text == "/music":
		# bot.send_audio("@otaku_testing", audioFile)  # send the file to the channel
		# bot.send_audio(message.from_user.id, audioFile)
		songs(message)
	elif message.text == "/igif":
		bot.send_message(message.from_user.id,"use /gif then type your context\nExample:\n1./gif anime\n2./gif smile\n...")



@bot.message_handler(func=lambda message: True)
def inlineGif(message):
	inpText = message.text
	if "/gif" in inpText:
		context = inpText.replace("/gif", " ").strip()
		if context != "":
			giffy(message, context)
		else:
			giffy(message)
	else:
		bot.send_message(message.from_user.id,"Wrong Input\nTry again!", reply_markup=Imarkup())

command = [BotCommand("start","to start the bot"), BotCommand("help","A guide to use Otaku"),
		    BotCommand("gif","Get random gifs"), BotCommand("igif","Inline gif search"),
			    BotCommand("music","Listen to your fav music")]
bot.set_my_commands(command)

#Tenor
apikey = "LIVDSRZULELA" 
lmt = 1

# Functions 

audioFile = "https://mp3gaga.com/wp-content/uploads/2021/03/COOLIO-GANGSTER-PARADISE-Mp3gaga.com_.mp3"

def giffy(message, search_term = "Hello"):
	r = requests.get("https://g.tenor.com/v1/random?&q=%s&key=%s&limit=%s" % (search_term,apikey,lmt)).json()
	imageUrl = str(r['results'][0]['url'])
	botMsg = bot.reply_to(message,"Searching Gif...")
	bot.send_document(message.from_user.id,"http://103.222.20.150/ftpdata/Movies/tv%20series/English/Game%20Of%20Thrones/Season%201/Game%20of%20Thrones%20-%200xSpecial%201%20-%20Inside%20Game%20of%20Thrones.mkv")
	bot.delete_message(message.from_user.id, botMsg.message_id)

def songs(message):
	# bot.send_audio("@otaku_testing", audioFile)  # send the file to the channel
	bot.send_audio(message.from_user.id, audioFile)


bot.infinity_polling()
