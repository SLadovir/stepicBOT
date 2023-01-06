import requests
import time


def send_cat(res) -> None:
    API_CATS_URL: str = 'https://aws.random.cat/meow'
    ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
    cat_response: requests.Response
    cat_link: str

    chat_id = res['message']['from']['id']
    cat_response = requests.get(API_CATS_URL)
    if cat_response.status_code == 200:
        cat_link = cat_response.json()['file']
        requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
    else:
        requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')


if __name__ == '__main__':
    API_URL: str = 'https://api.telegram.org/bot'
    BOT_TOKEN: str = '1898674417:AAHvwZRAPg1VLDauHToD10pMHELU_FhxSYU'

    MAX_COUNTER: int = 100

    offset: int = -2
    timeout: int = 60

    counter: int = 0


    while True:
        start_time = time.time()
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                send_cat(result)

        time.sleep(3)
        end_time = time.time()
        print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')

