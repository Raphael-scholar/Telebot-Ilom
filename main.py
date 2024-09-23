import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import html
import random
import time
from collections import defaultdict
import urllib.parse
import threading
from flask import Flask, render_template_string

# Initialize BetterStack
BETTERSTACK_API_KEY = os.environ['UPTIME_API_KEY']

# Bot configuration
TELEGRAM_API_KEY = os.environ['YOUR_BOT_TOKEN']
TRIVIA_API_URL = "https://opentdb.com/api.php?amount=1&category=17&type=multiple"
NINJA_API_KEY = os.environ['YOUR_NINJA_API_KEY']
FACT_API_URL = "https://api.api-ninjas.com/v1/facts?limit=1&category=science"
NEWS_API_KEY = os.environ['NEWS_API_KEY']
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey={NEWS_API_KEY}"

bot = telebot.TeleBot(TELEGRAM_API_KEY)

# User data
user_data = defaultdict(lambda: {'score': 0, 'streak': 0, 'total_questions': 0, 'correct_answers': 0, 'last_interaction': time.time()})

# Daily challenge
daily_challenge = None
last_challenge_update = 0

# Cache for API responses
cache = {}

# Log event function
def log_event(event_type, message):
    # Implement your logging logic here
    print(f"{event_type}: {message}")

# Enhanced bot functions
def get_science_question():
    try:
        if 'trivia_question' in cache and time.time() - cache['trivia_question']['timestamp'] < 3600:
            return cache['trivia_question']['data']
        
        response = requests.get(TRIVIA_API_URL)
        response.raise_for_status()
        data = response.json()
        if data['response_code'] == 0:
            question = data['results'][0]
            decoded_question = {
                'question': html.unescape(question['question']),
                'correct_answer': html.unescape(question['correct_answer']),
                'options': [html.unescape(ans) for ans in question['incorrect_answers'] + [question['correct_answer']]]
            }
            random.shuffle(decoded_question['options'])
            cache['trivia_question'] = {'data': decoded_question, 'timestamp': time.time()}
            return decoded_question
    except requests.RequestException as e:
        log_event('error', f"Error fetching science question: {e}")
    return None

def get_science_fact():
    try:
        if 'science_fact' in cache and time.time() - cache['science_fact']['timestamp'] < 3600:
            return cache['science_fact']['data']
        
        headers = {'X-Api-Key': NINJA_API_KEY}
        response = requests.get(FACT_API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            fact = data[0]['fact']
            cache['science_fact'] = {'data': fact, 'timestamp': time.time()}
            return fact
    except requests.RequestException as e:
        log_event('error', f"Error fetching science fact: {e}")
    return None

def get_quiz_keyboard(options):
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [InlineKeyboardButton(option, callback_data=f"answer:{urllib.parse.quote(option)}") for option in options]
    keyboard.add(*buttons)
    return keyboard

def get_science_news():
    try:
        if 'science_news' in cache and time.time() - cache['science_news']['timestamp'] < 3600:
            return random.choice(cache['science_news']['data'])
        
        response = requests.get(NEWS_API_URL)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'ok' and data['articles']:
            cache['science_news'] = {'data': data['articles'], 'timestamp': time.time()}
            return random.choice(data['articles'])['title']
    except requests.RequestException as e:
        log_event('error', f"Error fetching science news: {e}")
    return None

def update_daily_challenge():
    global daily_challenge, last_challenge_update
    current_time = time.time()
    if current_time - last_challenge_update > 86400:  # 24 hours
        daily_challenge = get_science_question()
        last_challenge_update = current_time

# Bot handlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🧪 Welcome to the Enhanced Science Raphael's Quiz Bot! 🔬\n\n"
        "Commands:\n"
        "/quiz - Start a new quiz question\n"
        "/fact - Get a random science fact\n"
        "/score - See your current score and stats\n"
        "/leaderboard - View the top 5 players\n"
        "/daily_challenge - Get a daily science challenge\n"
        "/fun_fact - Get a fun science fact\n"
        "/science_news - Get latest science news\n"
        "/help - Show this help message\n\n"
        "Are you ready to explore the wonders of science? Let's begin with /quiz or /fact!"
    )
    bot.reply_to(message, welcome_text)
    log_event('info', f"User {message.from_user.id} started the bot")

@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    chat_id = message.chat.id
    question = get_science_question()
    if question:
        user_data[chat_id]['current_question'] = question
        user_data[chat_id]['question_start_time'] = time.time()
        quiz_text = (
            f"🔬 *Science Question:*\n\n"
            f"{question['question']}\n\n"
            f"Choose your answer:"
        )
        bot.send_message(chat_id, quiz_text, reply_markup=get_quiz_keyboard(question['options']), parse_mode='Markdown')
        log_event('info', f"User {chat_id} started a new quiz")
    else:
        bot.send_message(chat_id, "🚫 Sorry, I couldn't fetch a question right now. Please try again later.")
        log_event('warning', f"Failed to fetch quiz question for user {chat_id}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('answer:'))
def check_answer(call):
    chat_id = call.message.chat.id
    answer = urllib.parse.unquote(call.data.split(':')[1])
    
    if 'current_question' in user_data[chat_id]:
        question = user_data[chat_id]['current_question']
        time_taken = time.time() - user_data[chat_id]['question_start_time']
        user_data[chat_id]['total_questions'] += 1
        user_data[chat_id]['last_interaction'] = time.time()
        
        if answer == question['correct_answer']:
            points = max(10, 20 - int(time_taken))
            user_data[chat_id]['score'] += points
            user_data[chat_id]['streak'] += 1
            user_data[chat_id]['correct_answers'] += 1
            response = (
                f"✅ *Correct!* Well done!\n\n"
                f"🏆 You earned *{points} points*.\n"
                f"🔥 Current streak: *{user_data[chat_id]['streak']}*\n\n"
                f"_Time taken: {time_taken:.2f} seconds_"
            )
            log_event('info', f"User {chat_id} answered correctly")
        else:
            user_data[chat_id]['streak'] = 0
            response = (
                f"❌ Sorry, that's incorrect.\n\n"
                f"The correct answer is: *{question['correct_answer']}*\n"
                f"🔥 Streak reset to 0\n\n"
                f"_Time taken: {time_taken:.2f} seconds_"
            )
            log_event('info', f"User {chat_id} answered incorrectly")
        
        bot.answer_callback_query(call.id, "Answer recorded!")
        bot.send_message(chat_id, response, parse_mode='Markdown')
        if time.time() - user_data[chat_id]['last_interaction'] < 10:
            bot.send_message(chat_id, "Ready for another question? Use /quiz to continue or /score to see your stats.")
        else:
            del user_data[chat_id]['current_question']
            bot.send_message(chat_id, "This question has expired. Start a new one with /quiz")
    else:
        bot.answer_callback_query(call.id, "This question has expired. Start a new one with /quiz")

@bot.message_handler(commands=['score'])
def show_score(message):
    chat_id = message.chat.id
    user_stats = user_data[chat_id]
    accuracy = (user_stats['correct_answers'] / user_stats['total_questions'] * 100) if user_stats['total_questions'] > 0 else 0
    
    score_text = (
        f"🏆 *Your Current Stats* 🏆\n\n"
        f"Score: *{user_stats['score']}* points\n"
        f"Current Streak: *{user_stats['streak']}*\n"
        f"Questions Answered: *{user_stats['total_questions']}*\n"
        f"Correct Answers: *{user_stats['correct_answers']}*\n"
        f"Accuracy: *{accuracy:.2f}%*\n\n"
        f"Keep it up! Can you reach the top of the /leaderboard?"
    )
    bot.send_message(chat_id, score_text, parse_mode='Markdown')
    log_event('info', f"User {chat_id} checked their score")

@bot.message_handler(commands=['leaderboard'])
def show_leaderboard(message):
    sorted_users = sorted(user_data.items(), key=lambda x: x[1]['score'], reverse=True)[:5]
    leaderboard_text = "🏆 *Top 5 Science Trivia Masters* 🏆\n\n"
    for i, (user_id, data) in enumerate(sorted_users, 1):
        user_info = bot.get_chat(user_id)
        name = user_info.first_name if user_info.first_name else "Anonymous"
        leaderboard_text += f"{i}. {name}: *{data['score']}* points\n"
    
    bot.send_message(message.chat.id, leaderboard_text, parse_mode='Markdown')
    log_event('info', f"User {message.chat.id} viewed the leaderboard")

@bot.message_handler(commands=['fact'])
def send_science_fact(message):
    fact = get_science_fact()
    if fact:
        fact_text = f"🧠 *Did you know?*\n\n{fact}"
        bot.send_message(message.chat.id, fact_text, parse_mode='Markdown')
        log_event('info', f"User {message.chat.id} requested a science fact")
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't fetch a science fact right now. Please try again later.")
        log_event('warning', f"Failed to fetch science fact for user {message.chat.id}")

@bot.message_handler(commands=['daily_challenge'])
def daily_challenge_handler(message):
    update_daily_challenge()
    if daily_challenge:
        challenge_text = (
            f"🌟 *Daily Science Challenge* 🌟\n\n"
            f"{daily_challenge['question']}\n\n"
            f"Options:\n"
            f"A) {daily_challenge['options'][0]}\n"
            f"B) {daily_challenge['options'][1]}\n"
            f"C) {daily_challenge['options'][2]}\n"
            f"D) {daily_challenge['options'][3]}\n\n"
            f"Reply with your answer (A, B, C, or D). Good luck!"
        )
        bot.send_message(message.chat.id, challenge_text, parse_mode='Markdown')
        log_event('info', f"User {message.chat.id} started the daily challenge")
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't fetch today's challenge. Please try again later.")
        log_event('warning', f"Failed to fetch daily challenge for user {message.chat.id}")

@bot.message_handler(commands=['fun_fact'])
def fun_fact(message):
    facts = [
        "Bananas are berries, but strawberries aren't!",
        "A day on Venus is longer than its year.",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
        "The human brain uses the same amount of power as a 10-watt light bulb.",
        "Octopuses have three hearts and blue blood."
    ]
    bot.send_message(message.chat.id, f"🎉 *Fun Science Fact:*\n\n{random.choice(facts)}", parse_mode='Markdown')
    log_event('info', f"User {message.chat.id} requested a fun fact")

@bot.message_handler(commands=['science_news'])
def science_news(message):
    news = get_science_news()
    if news:
        bot.send_message(message.chat.id, f"📰 *Latest Science News:*\n\n{news}", parse_mode='Markdown')
        log_event('info', f"User {message.chat.id} requested science news")
    else:
        bot.send_message(message.chat.id, "Sorry, I couldn't fetch the latest science news. Please try again later.")
        log_event('warning', f"Failed to fetch science news for user {message.chat.id}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I don't understand that command. Use /help to see available commands.")
    log_event('info', f"User {message.chat.id} sent an unknown command: {message.text}")

# Flask app for WebView
app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <html>
            <head>
                <title>Science Trivia Bot</title>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background-color: #f0f0f0; }
                    h1 { color: #4CAF50; }
                </style>
            </head>
            <body>
                <h1>Raphael Science Trivia Bot</h1>
                <p>Your bot is running! Visit <a href="https://t.me/@Raphealgeniusbot">t.me/@Raphealgeniusbot</a> to start playing.</p>
            </body>
        </html>
    """)

# BetterStack Uptime check
@app.route('/health')
def health_check():
    return "OK", 200

def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = threading.Thread(target=run_flask)
    t.start()

if __name__ == "__main__":
    print("Enhanced Science Trivia Bot is running...")
    keep_alive()
    bot.polling(none_stop=True)