from flask import Flask, render_template_string
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    uptime = time.time() - start_time
    days, remainder = divmod(uptime, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Science Trivia Bot Status</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }
                .container {
                    text-align: center;
                    background-color: white;
                    padding: 2rem;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #4CAF50;
                }
                p {
                    font-size: 1.2rem;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Science Trivia Bot Status</h1>
                <p>🟢 Bot is alive and running!</p>
                <p>Uptime: {{ days }} days, {{ hours }} hours, {{ minutes }} minutes, {{ seconds }} seconds</p>
            </div>
        </body>
        </html>
    ''', days=int(days), hours=int(hours), minutes=int(minutes), seconds=int(seconds))

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

start_time = time.time()

# This function will be imported and called in your main bot file
def initialize_keep_alive():
    keep_alive()
    return start_time