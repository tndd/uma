from concurrent.futures import ThreadPoolExecutor

from requests import get

from bot.netkeiba.race.calendar.generater import gen_url_for_access_to_calendar


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


def fetch_all_race_calender_html(n_worker: int = 16):
    urls = gen_url_for_access_to_calendar()
    with ThreadPoolExecutor(max_workers=n_worker) as executor:
        executor.map(fetch_race_calender_html, urls)


if __name__ == '__main__':
    pass
