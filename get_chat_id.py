import time
import telepot
from telepot.loop import MessageLoop

def action(msg):
    chat_id = msg['chat']['id']
    print("Chat ID:", chat_id)
    
telegram_bot = telepot.Bot('<MASUKAN TOKEN BOT ANDA>')
MessageLoop(telegram_bot, action).run_as_thread()
print ('[INFO] telegram bot sedang berjalan')    
while 1:
    time.sleep(10)