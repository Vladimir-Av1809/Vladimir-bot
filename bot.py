import telebot

# Ваш токен бота от BotFather
TOKEN = 'сюда вставь свой токен'

bot = telebot.TeleBot(TOKEN)

# Словарь для хранения клиентов: номер телефона -> имя
clients = {}

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправьте номер телефона и ФИО клиента через пробел.\n\nНапример:\n+79998887766 Иванов Иван")

# Обработка всех остальных сообщений
@bot.message_handler(func=lambda message: True)
def handle_client_data(message):
    try:
        parts = message.text.strip().split(' ', 1)
        if len(parts) != 2:
            bot.reply_to(message, "Неверный формат.\nОтправьте номер телефона и ФИО через пробел.\n\nНапример:\n+79998887766 Иванов Иван")
            return

        phone, name = parts
        clients[phone] = name

        # Сообщение клиенту
        text = (
            f"Приветствую! Я - Владимир, механик с любовью к своему делу.\n"
            f"Если хотите, чтобы ваш автомобиль обслужили так, как себе — добро пожаловать!\n"
            f"Работаю аккуратно, без лишних наворотов и ненужных затрат.\n"
            f"Пишите, звоните — всегда на связи!"
        )

        # Отправляем сообщение клиенту
        bot.send_message(phone, text)
        bot.reply_to(message, f"Сообщение успешно отправлено клиенту: {name} ({phone})")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")

# Запуск бота
bot.polling()