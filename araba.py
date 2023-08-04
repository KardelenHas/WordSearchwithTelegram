# import requests
# import time
# from bs4 import BeautifulSoup
# import telegram  # python-telegram-bot kütüphanesini içe aktarın

# # bot_token = '6305595663:AAEcNNdOyuvC4JQcIPqhe7KLglVQP5vyl70'
# # chat_id = '5568007406'  

# def send_telegram_message(alert_str, status):
#     #SENT MESAGE TO TELEGRAM BOT 
#     token = '6305595663:AAEcNNdOyuvC4JQcIPqhe7KLglVQP5vyl70' # telegram token
#     receiver_id = 5568007406 # https://api.telegram.org/bot<TOKEN>/getUpdates
#     bot = telepot.Bot(token)
    
#     filehandle_diff = open("previous_content.txt", 'r', encoding="utf-8")
#     diff = filehandle_diff.read() 
#     filehandle_diff.close()
    
#     if alert_str != "":
#         bot.sendMessage(receiver_id, 'ALERT! -- SOMETHING CHANGED !!! ' + alert_str) # send a activation message to telegram receiver id
#         bot.sendMessage(receiver_id, 'DIFFERENCE: ' + diff)
#         bot.sendPhoto(receiver_id, photo=open('./output_ss/out_ss.png', 'rb'))
#     else:
#         bot.sendMessage(receiver_id, 'Status: ' + status)

# def kelime_arama(url, kelimeler, aralik):
#     while True:
#         try:
#             # İnternet sayfasını indir
#             response = requests.get(url)
#             soup = BeautifulSoup(response.text, 'html.parser')

#             # Sayfa içerisinde arama yap
#             found_keywords = []
#             for kelime in kelimeler:
#                 if kelime in soup.get_text():
#                     found_keywords.append(kelime)

#             # Bulunan kelimeleri göster ve Telegram mesajı gönder
#             if found_keywords:
#                 print("Sayfada bulunan kelimeler:", found_keywords)
#                 message = "Sayfada bulunan kelimeler: " + ", ".join(found_keywords)
#                 send_telegram_message(message)

#             # Belirtilen aralık kadar bekle
#             time.sleep(aralik)

#         except requests.exceptions.RequestException as e:
#             print("Bağlantı hatası:", e)

# # Ana program
# if __name__ == '__main__':
#     # İzlenecek sayfa URL'si
#     url = 'https://www.mercedes-benz.com.tr/passengercars/buy/new-car/search-results.html'

#     # Aranacak kelimeler (liste olarak)
#     kelimeler = ['eqb', 'CLS']

#     # Arama aralığı (saniye cinsinden)
#     aralik = 10

#     # Kelime arama fonksiyonunu başlat
#     kelime_arama(url, kelimeler, aralik)



import requests
import time
from bs4 import BeautifulSoup
import telegram
import asyncio

bot_token = '6305595663:AAEcNNdOyuvC4JQcIPqhe7KLglVQP5vyl70'
chat_id = '5568007406'

async def send_telegram_message(message):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

async def kelime_arama(url, kelimeler, aralik):
    while True:
        try:
            # İnternet sayfasını indir
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Sayfa içerisinde arama yap
            found_keywords = []
            for kelime in kelimeler:
                if kelime in soup.get_text():
                    found_keywords.append(kelime)

            # Bulunan kelimeleri göster ve Telegram mesajı gönder
            if found_keywords:
                print("Sayfada bulunan kelimeler:", found_keywords)
                message = "Sayfada bulunan kelimeler: " + ", ".join(found_keywords)
                await send_telegram_message(message)

            # Belirtilen aralık kadar bekle
            await asyncio.sleep(aralik)

        except requests.exceptions.RequestException as e:
            print("Bağlantı hatası:", e)

def main():
    # İzlenecek sayfa URL'si
    url = 'https://www.mercedes-benz.com.tr/passengercars/buy/new-car/search-results.html'

    # Aranacak kelimeler (liste olarak)
    kelimeler = ['eqb', 'eqa', 'eqc']

    # Arama aralığı (saniye cinsinden)
    aralik = 10

    # Event loop oluştur
    loop = asyncio.get_event_loop()

    try:
        # Asenkron işlevleri event loop içinde çalıştır
        loop.create_task(kelime_arama(url, kelimeler, aralik))
        loop.run_forever()
    except KeyboardInterrupt:
        # Ctrl+C ile programı sonlandırırken event loop'u kapat
        print("Program sonlandırıldı.")
        loop.close()

if __name__ == '__main__':
    main()
