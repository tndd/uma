import os

from bot.netkeiba.const import PATH_CALENDAR_CACHE, PATH_RACE_DAY_URLS
from bot.netkeiba.race.calendar.harvester import fetch_all_race_calender_html
from bot.netkeiba.race.calendar.parser import extract_store_race_day_urls


def fetch_race_day_urls():
    """
    開催日のURLの保存までを行う
    """
    # cacheがない場合のみダウンロード実行
    if not os.path.exists(PATH_CALENDAR_CACHE):
        fetch_all_race_calender_html()
    # 開催日のURLをファイルから抽出
    extract_store_race_day_urls()


def get_race_day_urls():
    """
    開催日のURLを文字列として取得するところまでを行う
    """
    # ファイルがない場合はダウンロード実行
    if not os.path.exists(PATH_RACE_DAY_URLS):
        fetch_race_day_urls()
    with open(PATH_RACE_DAY_URLS, 'r', encoding='UTF-8') as file:
        return [line.strip() for line in file.readlines()]



# def test_fetch_race_day_urls():
#     # fetch_race_day_urls()を実行
#     fetch_race_day_urls()
#     # URLファイルが作成されたことを確認
#     assert os.path.exists(PATH_RACE_DAY_URLS), "URLファイルが作成されていません"


def test_get_race_day_urls():
    # URLリストを取得
    urls = get_race_day_urls()
    # URLリストが空でないことを確認
    assert len(urls) > 0, "URLリストが空です"
    # 各URLが正しい形式であることを確認
    for url in urls:
        assert url.startswith("https://db.netkeiba.com/race/list/"), "不正なURL形式です"
