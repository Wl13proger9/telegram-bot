import google.generativeai as genai
from dotenv import load_dotenv
import telebot
import google.generativeai as genai
import random

try:
    show_errors = False
    load_dotenv()
    bot = telebot.TeleBot("7866356419:AAEAfjmbrwtBTOAmQvIqLGxQVBmZ61NPUKM", parse_mode=None)
    genai.configure(api_key=("AIzaSyDxx79EEWdzMlgQUPL--JZNGX2bNcdbkMg"))


    generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",}


    safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",},
    {"category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",},]


    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction="твой пол женский, твое имя Ясу, твоя фамилия Мидзуно, тебе 16 лет")


    chat_session = model.start_chat(history=[])




    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет👋")
        


    @bot.message_handler(func=lambda message: True)
    def log_and_reply(message):

            response = chat_session.send_message(message.text)
            model_response = response.text

            
            chat_id = message.chat.id
            bot.send_message(chat_id, response.text)


            chat_session.history.append({"role": "user", "parts": [message.text]})
            chat_session.history.append({"role": "model", "parts": [model_response]})




    print("Бот работает")
    bot.infinity_polling()
except Exception as e:
     print("при выполнении кода произошла ошибка\nтекст ошибки:  "+str(e))     