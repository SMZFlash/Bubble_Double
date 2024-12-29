import telebot
import random
import schedule
import time
import threading

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

user_data = {}

quizzes = {
    'english': [
        {
            'question': 'What is the capital of France?',
            'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
            'correct_option': 'Paris'
        },
        {
            'question': 'What is the largest ocean on Earth?',
            'options': ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
            'correct_option': 'Pacific Ocean'
        },
        {
            'question': 'Which planet is known as the Red Planet?',
            'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
            'correct_option': 'Mars'
        },
        {
            'question': 'What is the smallest country in the world?',
            'options': ['Monaco', 'Vatican City', 'San Marino', 'Liechtenstein'],
            'correct_option': 'Vatican City'
        },
        {
            'question': 'Who wrote "Romeo and Juliet"?',
            'options': ['Charles Dickens', 'Mark Twain', 'William Shakespeare', 'Jane Austen'],
            'correct_option': 'William Shakespeare'
        },
        {
            'question': 'What is the chemical symbol for water?',
            'options': ['H2O', 'O2', 'CO2', 'NaCl'],
            'correct_option': 'H2O'
        },
        {
            'question': 'Which gas do plants absorb from the atmosphere?',
            'options': ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Hydrogen'],
            'correct_option': 'Carbon Dioxide'
        },
        {
            'question': 'What is the largest mammal in the world?',
            'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Great White Shark'],
            'correct_option': 'Blue Whale'
        },
        {
            'question': 'In which year did the Titanic sink?',
            'options': ['1912', '1905', '1898', '1920'],
            'correct_option': '1912'
        },
        {
            'question': 'What is the main ingredient in guacamole?',
            'options': ['Tomato', 'Avocado', 'Pepper', 'Onion'],
            'correct_option': 'Avocado'
        },
        {
            'question': 'Which continent is known as the "Dark Continent"?',
            'options': ['Asia', 'Africa', 'South America', 'Australia'],
            'correct_option': 'Africa'
        },
        {
            'question': 'What is the hardest natural substance on Earth?',
            'options': ['Gold', 'Iron', 'Diamond', 'Quartz'],
            'correct_option': 'Diamond'
        },
        {
            'question': 'Which element has the atomic number 1?',
            'options': ['Helium', 'Oxygen', 'Hydrogen', 'Carbon'],
            'correct_option': 'Hydrogen'
        },
        {
            'question': 'What is the capital of Japan?',
            'options': ['Seoul', 'Beijing', 'Tokyo', 'Bangkok'],
            'correct_option': 'Tokyo'
        },
        {
            'question': 'Which famous scientist developed the theory of relativity?',
            'options': ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Nikola Tesla'],
            'correct_option': 'Albert Einstein'
        },
        {
            'question': 'What is the largest desert in the world?',
            'options': ['Sahara', 'Arabian', 'Gobi', 'Antarctic'],
            'correct_option': 'Antarctic'
        }
    ]
}

words = {
    'english': [
        {'word': 'Apple', 'translation': 'Яблоко', 'example': 'I eat an apple every day.'},
        {'word': 'Book', 'translation': 'Книга', 'example': 'This book is very interesting.'},
        {'word': 'Car', 'translation': 'Машина', 'example': 'I have a red car.'},
        {'word': 'Dog', 'translation': 'Собака', 'example': 'My dog loves to play.'},
        {'word': 'Elephant', 'translation': 'Слон', 'example': 'The elephant is the largest land animal.'},
        {'word': 'Fish', 'translation': 'Рыба', 'example': 'I like to eat fish for dinner.'},
        {'word': 'Guitar', 'translation': 'Гитара', 'example': 'He plays the guitar beautifully.'},
        {'word': 'House', 'translation': 'Дом', 'example': 'They live in a big house.'},
        {'word': 'Ice cream', 'translation': 'Мороженое', 'example': 'I love chocolate ice cream.'},
        {'word': 'Juice', 'translation': 'Сок', 'example': 'I drink orange juice in the morning.'},
        {'word': 'Key', 'translation': 'Ключ', 'example': 'I lost my house key.'},
        {'word': 'Lion', 'translation': 'Лев', 'example': 'The lion is known as the king of the jungle.'},
        {'word': 'Mountain', 'translation': 'Гора', 'example': 'We climbed the mountain last summer.'},
        {'word': 'Notebook', 'translation': 'Блокнот', 'example': 'I write my notes in a notebook.'},
        {'word': 'Orange', 'translation': 'Апельсин', 'example': 'An orange is a good source of vitamin C.'},
        {'word': 'Pencil', 'translation': 'Карандаш', 'example': 'I need a pencil to write.'},
        {'word': 'Queen', 'translation': 'Королева', 'example': 'The queen lives in a palace.'},
        {'word': 'River', 'translation': 'Река', 'example': 'The river flows through the city.'},
        {'word': 'Sun', 'translation': 'Солнце', 'example': 'The sun rises in the east.'},
        {'word': 'Tree', 'translation': 'Дерево', 'example': 'The tree provides shade in the summer.'},
        {'word': 'Umbrella', 'translation': 'Зонт', 'example': 'I take an umbrella when it rains.'},
        {'word': 'Violin', 'translation': 'Скрипка', 'example': 'She plays the violin in the orchestra.'},
        {'word': 'Window', 'translation': 'Окно', 'example': 'I looked out of the window.'},
        {'word': 'Xylophone', 'translation': 'Ксилофон', 'example': 'The xylophone is a musical instrument.'},
        {'word': 'Yogurt', 'translation': 'Йогурт', 'example': 'I eat yogurt for breakfast.'},
        {'word': 'Zebra', 'translation': 'Зебра', 'example': 'The zebra has black and white stripes.'},
        {'word': 'Friend', 'translation': 'Друг', 'example': 'My friend is coming over today.'},
        {'word': 'Family', 'translation': 'Семья', 'example': 'I love my family very much.'},
        {'word': 'School', 'translation': 'Школа', 'example': 'I go to school every day.'},
        {'word': 'Teacher', 'translation': 'Учитель', 'example': 'My teacher is very kind.'},
        {'word': 'Student', 'translation': 'Студент', 'example': 'The student is studying for the exam.'},
        {'word': 'City', 'translation': 'Город', 'example': 'I live in a big city.'},
        {'word': 'Country', 'translation': 'Страна', 'example': 'This country has beautiful landscapes.'},
        {'word': 'Food', 'translation': 'Еда', 'example': 'I love Italian food.'},
        {'word': 'Drink', 'translation': 'Напиток', 'example': 'Water is the best drink for health.'},
    ]
}

@bot.message_handler(commands=['quiz2'])
def quiz2(message):
    chat_id = message.chat.id
    language = user_data.get(chat_id, {}).get('language')
    
    if language is None:
        bot.send_message(chat_id, "Сначала выберите язык с помощью /set_language <язык>.")
        return

    question_data = random.choice(quizzes[language])
    user_data.setdefault(chat_id, {})['current_question'] = question_data
    user_data[chat_id].setdefault('quiz2_score', 0)

    options = question_data['options']
    random.shuffle(options)

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        markup.add(option)
    
    bot.send_message(chat_id, question_data['question'], reply_markup=markup)
    bot.register_next_step_handler(message, check_answer_quiz2)

def check_answer_quiz2(message):
    chat_id = message.chat.id
    user_answer = message.text
    correct_answer = user_data[chat_id]['current_question']['correct_option']

    if user_answer == correct_answer:
        user_data[chat_id]['quiz2_score'] += 1  # Увеличиваем счетчик для второго квиза
        bot.send_message(chat_id, f"Верно! Ваш счёт: {user_data[chat_id]['quiz2_score']}. /quiz2 для следующего вопроса.")
    else:
        final_score = user_data[chat_id]['quiz2_score']
        bot.send_message(chat_id, f"Неверно. Правильный ответ: {correct_answer}. Викторина завершена. Ваш итоговый счёт: {final_score}.")
        user_data[chat_id]['quiz2_score'] = 0  # Сбрасываем счет после завершения викторины
    
    del user_data[chat_id]['current_question']

def check_answer(message):
    chat_id = message.chat.id
    user_answer = message.text
    correct_answer = user_data[chat_id]['current_word']['translation']

    if user_answer.lower() == correct_answer.lower():
        user_data[chat_id].setdefault('score', 0)
        user_data[chat_id]['score'] += 1
        user_data[chat_id].setdefault('quiz1_score', 0)
        user_data[chat_id]['quiz1_score'] += 1  # Увеличиваем счетчик для первого квиза
        bot.send_message(chat_id, f"Верно! Ваш счёт: {user_data[chat_id]['score']}. /quiz для следующего слова")
    else:
        final_score = user_data[chat_id]['quiz1_score']
        bot.send_message(chat_id, f"Неверно. Правильный ответ: {correct_answer}. Викторина завершена. Ваш итоговый счёт: {final_score}.")
        user_data[chat_id]['quiz1_score'] = 0  # Сбрасываем счет после завершения викторины

    del user_data[chat_id]['current_word']

def send_daily_word(chat_id):
    language = user_data.get(chat_id, {}).get('language')
    if language:
        word_info = random.choice(words[language])
        bot.send_message(
            chat_id,
            f"Новое слово: {word_info['word']}\n"
            f"Перевод: {word_info['translation']}\n"
            f"Пример: {word_info['example']}"
        )

def schedule_daily_messages(chat_id, time_str):
    schedule.every().day.at(time_str).do(send_daily_word, chat_id=chat_id)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

@bot.message_handler(commands=['save_word'])
def save_word(message):
    chat_id = message.chat.id
    args = message.text.split()
    
    if len(args) < 3:
        bot.send_message(chat_id, "Пожалуйста, укажите слово и его перевод. Пример: /save_word Apple Яблоко")
        return
    
    word = args[1]
    translation = args[2]
    
    # Initialize personal dictionary if not exists
    user_data.setdefault(chat_id, {}).setdefault('personal_dictionary', [])
    
    # Save the word and translation
    user_data[chat_id]['personal_dictionary'].append({'word': word, 'translation': translation})
    bot.send_message(chat_id, f"Слово '{word}' с переводом '{translation}' сохранено.")

@bot.message_handler(commands=['view_dictionary'])
def view_dictionary(message):
    chat_id = message.chat.id
    personal_dict = user_data.get(chat_id, {}).get('personal_dictionary', [])
    
    if not personal_dict:
        bot.send_message(chat_id, "Ваш словарь пуст.")
        return
    
    response = "Ваш личный словарь:\n"
    for entry in personal_dict:
        response += f"{entry['word']} - {entry['translation']}\n"
    
    bot.send_message(chat_id, response)

@bot.message_handler(commands=['quiz'])
def quiz(message):
    chat_id = message.chat.id
    if 'language' not in user_data.get(chat_id, {}) or user_data[chat_id]['language'] is None:
        bot.send_message(chat_id, "Сначала выберите язык с помощью /set_language english")
        return

    word_data = random.choice(words['english'])
    user_data.setdefault(chat_id, {})['current_word'] = word_data
    user_data[chat_id].setdefault('quiz1_score', 0)

    options = [ word_data['translation']]
    while len(options) < 4:
        random_word = random.choice(words['english'])
        if random_word['translation'] not in options:
            options.append(random_word['translation'])
    
    random.shuffle(options)

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    for option in options:
        markup.add(option)
    
    bot.send_message(chat_id, f"Переведите слово '{word_data['word']}'", reply_markup=markup)
    bot.register_next_step_handler(message, check_answer)

@bot.message_handler(commands=['start'])
def start(message):
    user_data[message.chat.id] = {'language': None, 'words_learned': 0, 'notification_time': None, 'score': 0, 'quiz1_score': 0, 'quiz2_score': 0}
    bot.send_message(message.chat.id, "Привет! Я бот для изучения языков. Используйте команду /set_language <язык>, чтобы выбрать язык; /get_word, чтобы изучить новое слово; /quiz, чтобы начать квиз по отгадыванию английских слова; /stats, чтобы посмотреть, сколько новых слов вы выучили; /save_word, чтобы сохранить слово; /view_dictionary, чтобы просмотреть ваш словарь; /quiz2, чтобы начать викторину с вопросами; /set_notification_time, чтобы установить время для отправки нового слова.")

@bot.message_handler(commands=['set_language'])
def set_language(message):
    args = message.text.split()
    if len(args) > 1:
        language = args[1].lower()
        if language in words:
            user_data[message.chat.id]['language'] = language
            bot.send_message(message.chat.id, f"Язык установлен на {language.capitalize()}.")
        else:
            bot.send_message(message.chat.id, "Язык не поддерживается. Пожалуйста, выберите другой.")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, укажите язык. Пример: /set_language english")

@bot.message_handler(commands=['set_notification_time'])
def set_notification_time(message):
    args = message.text.split()
    if len(args) > 1:
        time_str = args[1]
        user_data[message.chat.id]['notification_time'] = time_str
        schedule_daily_messages(message.chat.id, time_str)
        bot.send_message(message.chat.id, f"Время уведомления установлено на {time_str}.")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, укажите время. Пример: /set_notification_time 09:00")

@bot.message_handler(commands=['get_word'])
def get_word(message):
    user_id = message.chat.id
    language = user_data.get(user_id, {}).get('language')
    
    if language:
        word_info = random.choice(words[language])
        bot.send_message(
            user_id,
            f"Слово: {word_info['word']}\n"
            f"Перевод: {word_info['translation']}\n"
            f"Пример: {word_info['example']}"
        )
        user_data[user_id]['words_learned'] += 1
    else:
        bot.send_message(user_id, "Сначала установите язык с помощью команды /set_language.")

@bot.message_handler(commands=['stats'])
def stats(message):
    user_id = message.chat.id
    words_learned = user_data.get(user_id, {}).get('words_learned', 0)
    bot.send_message(user_id, f"Вы изучили {words_learned} слов.")

@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.send_message(message.chat.id, "Извините, я не понимаю эту команду.")

# Start the scheduling thread
threading.Thread(target=run_schedule, daemon=True).start()

if __name__ == '__main__':
    bot.polling(none_stop=True)