import random

from requests import get


def get_random_user_agent():
    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
    os_versions = ['10.0', '10_15_7', '11.0', '12.0']
    browser_versions = {
        'Chrome': [f'{random.randint(80, 91)}.0.{random.randint(4000, 4500)}.{random.randint(100, 200)}'],
        'Firefox': [f'{random.randint(80, 89)}.0'],
        'Safari': [f'{random.randint(13, 14)}.1.{random.randint(0, 2)}'],
        'Edge': [f'{random.randint(80, 91)}.0.{random.randint(800, 900)}.{random.randint(50, 100)}']
    }

    browser = random.choice(browsers)
    os_version = random.choice(os_versions)
    browser_version = random.choice(browser_versions[browser])

    if browser == 'Chrome':
        return f'Mozilla/5.0 (Windows NT {os_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{browser_version} Safari/537.36'
    elif browser == 'Firefox':
        return f'Mozilla/5.0 (Windows NT {os_version}; Win64; x64; rv:{browser_version}) Gecko/20100101 {browser}/{browser_version}'
    elif browser == 'Safari':
        return f'Mozilla/5.0 (Macintosh; Intel Mac OS X {os_version}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{browser_version} {browser}/605.1.15'
    elif browser == 'Edge':
        return f'Mozilla/5.0 (Windows NT {os_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/{browser_version}'

def get_random_header():
    return {
        'User-Agent': get_random_user_agent()
    }


def fetch_html(
    url: str,
    save_path: str,
    encoding: str = 'UTF-8',
) -> str:
    # url末尾に/がある場合は削除
    if url.endswith('/'):
        url = url[:-1]
    # ブラウザであるかのように偽装
    response = get(url, headers=get_random_header())
    response.encoding = encoding
    if response.status_code == 200:
        with open(save_path, 'w', encoding='UTF-8') as file:
            file.write(response.text)
        print(f"HTML saved to {save_path}")
    else:
        print(f"Error: Status code {response.status_code}")



def test_random_header():
    for _ in range(10):
        print(get_random_header())


if __name__ == '__main__':
    test_random_header()
