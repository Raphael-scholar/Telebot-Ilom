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

## 🚀 Comprehensive Deployment Guide

Deploy Brainy Bot on various platforms to keep it running 24/7!

### 🌐 Render

1. Fork the Brainy Bot repository on GitHub.
2. Sign up for a [Render account](https://render.com/).
3. In the Render dashboard, click "New" and select "Web Service".
4. Connect your GitHub account and select the Brainy Bot repository.
5. Configure your service:
   - Name: `brainy-bot`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`
6. Add environment variables:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your Telegram Bot Token
7. Click "Create Web Service"

Render will automatically deploy your bot and keep it running.

### ☁️ Heroku

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Login to Heroku: `heroku login`
3. Create a new Heroku app:
   ```bash
   heroku create brainy-bot-instance
   ```
4. Set up environment variables:
   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=your_token_here
   ```
5. Deploy your bot:
   ```bash
   git push heroku main
   ```
6. Ensure at least one instance is running:
   ```bash
   heroku ps:scale worker=1
   ```

### 🚂 Railway

1. Fork the Brainy Bot repository on GitHub.
2. Sign up for a [Railway account](https://railway.app/).
3. In the Railway dashboard, click "New Project" > "Deploy from GitHub repo".
4. Select your forked Brainy Bot repository.
5. Railway will automatically detect the Python environment.
6. Add environment variables in the Railway dashboard:
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: Your Telegram Bot Token
7. Deploy the project.

Railway will automatically build and deploy your bot.

### 🌊 DigitalOcean

1. Create a [DigitalOcean account](https://www.digitalocean.com/).
2. Create a new Droplet (choose Ubuntu as the operating system).
3. SSH into your Droplet:
   ```bash
   ssh root@your_droplet_ip
   ```
4. Update and install required packages:
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3-pip git -y
   ```
5. Clone your repository:
   ```bash
   git clone https://github.com/YourUsername/Brainy-Bot.git
   cd Brainy-Bot
   ```
6. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
7. Create a `.env` file and add your token:
   ```bash
   echo "TELEGRAM_BOT_TOKEN=your_token_here" > .env
   ```
8. Run your bot using `screen` to keep it active:
   ```bash
   screen -S brainy-bot
   python3 main.py
   ```
   Press `Ctrl+A` then `D` to detach from the screen.

### 🌐 PythonAnywhere

1. Sign up for a [PythonAnywhere account](https://www.pythonanywhere.com/).
2. In the dashboard, open a Bash console.
3. Clone your repository:
   ```bash
   git clone https://github.com/YourUsername/Brainy-Bot.git
   ```
4. Set up a virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.8 brainy-bot-env
   cd Brainy-Bot
   pip install -r requirements.txt
   ```
5. Create a `.env` file with your token.
6. In the "Web" tab, add a new web app:
   - Choose "Manual Configuration"
   - Set the working directory to your project folder
   - Set the WSGI file to point to your `main.py`
7. In the "Tasks" tab, add a scheduled task to run your bot:
   ```
   python /home/YourUsername/Brainy-Bot/main.py
   ```

### 📡 Google Cloud Platform

1. Create a [Google Cloud account](https://cloud.google.com/).
2. Create a new project in the Google Cloud Console.
3. Enable the Compute Engine API.
4. Create a new VM instance.
5. SSH into your instance from the GCP console.
6. Follow the DigitalOcean steps 4-8 to set up your bot.

Remember to keep your `TELEGRAM_BOT_TOKEN` secret and never share it publicly. Each platform has its own way of managing environment variables securely.

For all deployments, ensure your `requirements.txt` file is up-to-date and includes all necessary dependencies.

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
