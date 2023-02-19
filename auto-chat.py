import requests
import random
import json
import time
from common.utils import (
    config,
    logger
)

def conf():
    return config('./config/config.conf')

def get_content():
    contents = json.loads(conf()['chat']['contents'])
    content = random.choice(contents)
    return content

def chat(authorization, chanel_id):
    header = {
        "authorization": authorization,
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    content = get_content()
    msg = {
        "content": content,
        "nonce": "10767619081{}01984".format(random.randrange(0, 1000)),  # 923802142370693120 923802484009336832
        "tts": False
    }
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(chanel_id)
    proxy = conf()['proxy']
    proxy_str = f"socks5h://{proxy['username']}:{proxy['password']}@{proxy['host']}:{proxy['port']}"
    proxies = {
        "http": proxy_str,
        "https": proxy_str,
    }
    try:
        logger.info(f'sending "{content}" ...')
        res = requests.post(url=url, headers=header, data=json.dumps(msg), proxies=proxies)#, verify=False)
        logger.info('sent!')
    except requests.RequestException as e:
        logger.error(e)

if __name__ == '__main__':
    while True:
        chat(conf()['keys']['authorization'], conf()['keys']['channel'])
        logger.info('waiting for 1 hour...')
        time.sleep(60*60)