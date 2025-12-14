import telebot
import requests
import json

# Привязка бота к нашей командной строке
bot = telebot.TeleBot ('8419793381:AAGe0yP6Fv1pezSD2TNcYbP0KhwwHpfYnrQ')
api = 'e76340328e46242ed0fbce06e095e45a'


   # Обработка команды /start
@bot.message_handler(commands=['start'])


# Приветствие с функцией написания Вашего имени (относится к старту)
def main(message):
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}! Я - Показываю погоду в нужном Вам городе! Просто напишите название города на удобном для Вас языке, и Вы получите точную информацию!')



@bot.message_handler(commands=['help'])

def main(message):
    bot.send_message(message.chat.id, 'Просто напишите город в котором Вы хотите узнать температуру и погоду! Для перезапуска бота - /start')
# Строчка, которая видит текст и обрабатывает его
@bot.message_handler(content_types=["text"])

# Функция для получения и отправления данных о погоде
def get_weather (message):
    city = message.text.strip().lower()
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if weather.status_code == 200:
        data = json.loads(weather.text)
        bot.reply_to(message, f" На данный момент температура по °C в этом городе: {data["main"]["temp"]}")

    else:
        bot.reply_to(message, f'Город указан неверно!')

# Команда позволяющая боту работать бесконечно
bot.polling(none_stop=True)