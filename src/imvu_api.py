import requests

class IMVUAPI:
    def __init__(self):
        self.base_url = 'https://api.imvu.com'

    def get_chat_participants(self, chat_id):
        url = f'{self.base_url}/chat/chat-{chat_id}-10/participants/'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка при получении данных чата: {response.status_code} - {response.text}")

    def get_products(self, product_ids):
        ids = ','.join(map(str, product_ids))
        url = f'http://client-dynamic.imvu.com/api/shop/product.php?pids={ids}'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Ошибка при получении данных продуктов: {response.status_code} - {response.text}")
