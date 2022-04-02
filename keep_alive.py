from flask import Flask
from threading import Thread

app=Flask("")

@app.route("/")
def index():
    return "<h1>Bot is running</h1>"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  s = Thread(target=run)
  s.start()