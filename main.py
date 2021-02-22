import requests
import telegram

# Telegram setting
chat_id_bot = "1427660579"
chat_private_id = "-1001171474630"
chat_token = "1606450812:AAGrTv7Eeb1Q9iJEhycSJuuFE7E7Ow_XGGQ"
bot = telegram.Bot(token=chat_token)
chat_channel_url = "https://api.telegram.org/bot1606450812:AAGrTv7Eeb1Q9iJEhycSJuuFE7E7Ow_XGGQ/sendMessage"
chat_channel_Headers = {"Content-type": "application/json"}

# Shop Setting
shop_api_url = "https://api.louisvuitton.com/api/kor-kr/catalog/availability/010575"
shop_view_url = "https://kr.louisvuitton.com/kor-kr/products/nano-speedy-monogram-010575"
shop_headers = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'cookie': '_abck=31AB0C9A430DA422B3E1CBF57980642A~0~YAAQfHpGaL+DKq93AQAAJDEHwAVsqgc4L1HI41smpGPLU73umxqsHd8B4I3cOaZpXjW9JTfPMTw8Td8cDN+kpOpvhpvBlu6+mDMl1wCb6Sv2aYxhRf+rwELoVDfNWsbRimngamL/BIMJ3C8KiPxH6WVYe1w7h5FFU4YFzfXO9hwoVhi819bjsGs3UYtDEWXRLEyXwa5jcMlW6YKCjOduMrlH21pR4L62UcdLVF0CWK7UYXZ9FpCy75RiauxIySVACa/4AGHQYUmpYUCk4Usd7Ce8khHmIYabPpvKgAyeq6m/uWq//qoDxvn5CIYjVsoDf6w0IXAQnJawSCRfcF5TdS8hS2SjdTm5RhutyA==~-1~-1~-1',
    'referer': 'https://kr.louisvuitton.com/kor-kr/women/handbags/mini-bags/_/N-1ou97wg?page=3',
    'origin': 'https://kr.louisvuitton.com'
}

default_url = "https://kr.louisvuitton.com/kor-kr/homepage"
default_headers = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}


class Stock:
    def check_stock(self):
        try:
            res = requests.get(shop_api_url, headers=shop_headers, timeout=5)
            print(res.status_code)

            if res.status_code == 200:
                data = res.json()
                avail = data["skuAvailability"][0]
                stock = avail["inStock"]

                if stock:
                    message = "*** 재고있음!빨리빨리@ ***\n\n" + shop_view_url
                    requests.get(chat_channel_url)
                    params = '{"chat_id": "%s", "text": "%s"}' % (chat_private_id, message)
                    requests.post(chat_channel_url, headers=chat_channel_Headers, data=params.encode("UTF-8"))
                else:
                    message = "*** 재고없음 ***"

                return message
        except Exception as ex:
            return ex


m = Stock()
m.check_stock()
