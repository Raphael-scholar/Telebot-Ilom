# 🧠 Brainy Bot by Raphael

![Brainy Bot Logo](https://api.placeholdit.com/800x200?text=Brainy+Bot+Logo)

Elevate your Telegram experience with Brainy Bot – your intelligent companion for text styling, information retrieval, and interactive fun!

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-✓-blue.svg)](https://core.telegram.org/bots/api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Key Features

- **Smart Text Styling**: Transform plain text into visually stunning images
- **Multilingual Support**: Communicate effortlessly in 50+ languages
- **Instant Information**: Get weather updates, currency rates, and news at your fingertips
- **Entertainment Hub**: Enjoy mini-games and interactive challenges
- **Personal Assistant**: Set reminders and schedule important events
- **Knowledge Engine**: Solve math problems and get explanations on various topics

## 🚀 Quick Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Raphael/Brainy-Bot.git
   cd Brainy-Bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   - Create `.env` file: `TELEGRAM_BOT_TOKEN=your_token_here`

4. **Launch Brainy Bot**
   ```bash
   python main.py
   ```

## 🎮 Usage Guide

Interact with Brainy Bot using these commands:

- `/start` - Wake up Brainy Bot
- `/style <text>` - Create stylized text images
- `/ask <question>` - Get answers on various topics
- `/weather <city>` - Fetch current weather data
- `/play` - Start a fun mini-game
- `/remind <time> <message>` - Set a smart reminder

## 🌐 Deployment Options

### Heroku
```bash
heroku create brainy-bot-instance
heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
git push heroku main
```

### Railway
1. Fork this repository
2. Connect your GitHub to Railway
3. Deploy with environment variables set

### DigitalOcean
1. Create a Droplet (Ubuntu recommended)
2. SSH and clone the repository
3. Follow Quick Setup steps
4. Use `screen` to keep Brainy Bot active

## 🤝 Contribute to Brainy Bot

We welcome contributions! Here's how:

1. Fork the repo
2. Create your feature branch: `git checkout -b cool-new-feature`
3. Commit changes: `git commit -am 'Add cool feature'`
4. Push to the branch: `git push origin cool-new-feature`
5. Submit a pull request

## 📄 License & Acknowledgements

- Licensed under MIT - see [LICENSE](LICENSE)
- Built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and [Pillow](https://python-pillow.org/)
- Special thanks to all contributors and users!

![Brainy Bot Footer](https://api.placeholdit.com/800x100?text=Empower+Your+Chat+with+Brainy+Bot)
