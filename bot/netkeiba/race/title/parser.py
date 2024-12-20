import os

from bot.netkeiba.const import PATH_RACE_TITLE_CACHE, PATH_RACE_TITLES
from bot.netkeiba.race.calendar.parser import parse_calendar


def extract_store_race_day_urls() -> list[str]:
    html_files = [f for f in os.listdir(PATH_RACE_TITLE_CACHE) if f.endswith('.html')]
    all_urls = []
    for html_file in html_files:
        with open(os.path.join(PATH_RACE_TITLE_CACHE, html_file), 'r', encoding='UTF-8') as file:
            html = file.read()
            urls = parse_calendar(html)
            all_urls.extend(urls)
    # 情報を保存
    with open(PATH_RACE_TITLES, 'w', encoding='UTF-8') as output_file:
        for url in all_urls:
            output_file.write(url + '\n')