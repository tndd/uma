from requests import get


def fetch_race_calender_html(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = get(url, headers=headers)
    response.encoding = 'EUC-JP'  # netkeibaはEUC-JPエンコーディングを使用
    save_path = f'bot/netkeiba/race/calendar/cache/{url.split("/")[-1]}.html'
    if response.status_code == 200:
        with open(save_path, 'w', encoding='UTF-8') as file:
            file.write(response.text)
        print(f"HTML saved to {save_path}")
    else:
        print(f"Error: Status code {response.status_code}")


def fetch_race_calender_htmls():
    pass



if __name__ == '__main__':
    url = 'https://db.netkeiba.com/race/list/199001'
    fetch_race_calender_html(url)
