import requests

chat_id_bot = "1427660579"
chat_private_id = "-1001171474630"
chat_token = "1606450812:AAGrTv7Eeb1Q9iJEhycSJuuFE7E7Ow_XGGQ"
chat_channel_url = "https://api.telegram.org/bot1606450812:AAGrTv7Eeb1Q9iJEhycSJuuFE7E7Ow_XGGQ/sendMessage"
chat_channel_Headers = {"Content-type": "application/json"}

# Shop Setting
shop_api_url = "https://api.louisvuitton.com/api/kor-kr/catalog/availability/010575"
shop_view_url = "https://kr.louisvuitton.com/kor-kr/products/nano-speedy-monogram-010575"
shop_headers = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'cookie': '_abck=31AB0C9A430DA422B3E1CBF57980642A~0~YAAQfHpGaL+DKq93AQAAJDEHwAVsqgc4L1HI41smpGPLU73umxqsHd8B4I3cOaZpXjW9JTfPMTw8Td8cDN+kpOpvhpvBlu6+mDMl1wCb6Sv2aYxhRf+rwELoVDfNWsbRimngamL/BIMJ3C8KiPxH6WVYe1w7h5FFU4YFzfXO9hwoVhi819bjsGs3UYtDEWXRLEyXwa5jcMlW6YKCjOduMrlH21pR4L62UcdLVF0CWK7UYXZ9FpCy75RiauxIySVACa/4AGHQYUmpYUCk4Usd7Ce8khHmIYabPpvKgAyeq6m/uWq//qoDxvn5CIYjVsoDf6w0IXAQnJawSCRfcF5TdS8hS2SjdTm5RhutyA==~-1~-1~-1'
}

print("프로그램 시작!!!")

res = requests.get(shop_api_url, headers=shop_headers)

print("응답코드 ::" + res.status_code)

if res.status_code == 200:
    data = res.json()
    avail = data["skuAvailability"][0]
    stock = avail["inStock"]

    if stock:
        message = shop_view_url + "\n\n *** 재고있음!빨리빨리@ ***"
    else:
        message = shop_view_url + "\n\n *** 재고없음 ***"

print("프로그램 종료!!")
