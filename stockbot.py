# import packages
import requests
import time
import telepot
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup

# global variable
stock_price_before = 0

# functions
def get_stock_price():
    """
    fungsi ini digunakan untuk web scrap pada situs indoprimer.com agar mendapatkan
    harga terupdate dari saham tujuan (SIDO)
    """
    # hit URL menggunakan request get
    URL = "https://www.indopremier.com/newsSmartSearch.php?code=SIDO"
    page = requests.get(URL)

    # parse / uraikan konten halaman web
    soup = BeautifulSoup(page.content, 'html.parser')

    # cari dan pilih element html dengan class yang unik
    job_elems = soup.find_all('div', class_='panel-toolbar pull-right')
    for job_elem in job_elems:
        # pilih element html yang mengandung harga saham
        price_line = job_elem.find_all('td')[1]                
        # hapus spasi dan koma
        price_text = price_line.text.replace(" ","").replace(",","")        
        # konversi harga saham dari string ke integer
        stock_price = int(price_text)           
    
    # kembalikan harga saham
    return stock_price

def main():          
    # panggil global variable agar nilainya dapat dirubah
    global stock_price_before

    # Perulangan setiap 30 detik
    while True:    
        # panggil fungsi get_stock_price()
        stock_price = get_stock_price()
        # chat_id adalah id untuk room chat dengan bot
        chat_id = "887275636"        
        
        # jika harga saham berubah
        if stock_price != stock_price_before:            
            if stock_price > stock_price_before:
                # pesan yang akan dikirimkan oleh bot
                text = "Harga saham SIDO mengalami kenaikan menjadi Rp. %s" % (stock_price)            
            elif stock_price < stock_price_before:
                # pesan yang akan dikirimkan oleh bot
                text = "Harga saham SIDO mengalami penurunan menjadi Rp. %s" % (stock_price)        
            # kirim pesan 
            telegram_bot.sendMessage (chat_id, text)
            print("[INFO] pesan sedang dikirim")
            # update harga stock_price_before dengan harga terkini
            stock_price_before = stock_price
        time.sleep(30)
    
if __name__ == "__main__":
    # mulai telegram bot
    telegram_bot = telepot.Bot('<MASUKAN TOKEN BOT ANDA>')    
    print ('[INFO] telegram bot sedang berjalan')    
    while 1:        
        time.sleep(5)   
        # panggil fungsi main()     
        main()