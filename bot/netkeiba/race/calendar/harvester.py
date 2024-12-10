from concurrent.futures import ThreadPoolExecutor

from requests import get

from bot.netkeiba.const import PATH_CALENDAR_CACHE
from bot.netkeiba.harvester import fetch_html
from bot.netkeiba.race.calendar.generater import gen_url_for_access_to_calendar


def fetch_race_calender_html(url: str) -> str:
    encoding = 'EUC-JP'  # netkeibaはEUC-JPエンコーディングを使用
    save_path = f'{PATH_CALENDAR_CACHE}/{url.split("/")[-1]}.html'
    return fetch_html(url, save_path, encoding)


def fetch_all_race_calender_html(n_worker: int = 16):
    urls = gen_url_for_access_to_calendar()
    with ThreadPoolExecutor(max_workers=n_worker) as executor:
        executor.map(fetch_race_calender_html, urls)


if __name__ == '__main__':
    pass
