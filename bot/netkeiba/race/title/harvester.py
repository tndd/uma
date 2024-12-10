from concurrent.futures import ThreadPoolExecutor

from bot.netkeiba.const import PATH_RACE_TITLE_CACHE
from bot.netkeiba.harvester import fetch_html
from bot.netkeiba.race.title.service import read_race_day_urls


def fetch_race_title_html(url: str) -> str:
    encoding = 'EUC-JP'  # netkeibaはEUC-JPエンコーディングを使用
    save_path = f'{PATH_RACE_TITLE_CACHE}/{url.split("/")[-1]}.html'
    return fetch_html(url, save_path, encoding)


def fetch_all_race_title_html(n_worker: int = 16):
    urls = read_race_day_urls()
    with ThreadPoolExecutor(max_workers=n_worker) as executor:
        executor.map(fetch_race_title_html, urls)


if __name__ == '__main__':
    # fetch_all_race_title_html()
    pass
