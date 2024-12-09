from bot.race.const import URL_RACE_LIST


def gen_year_month() -> list[str]:
    """
    各月ごとのカレンダー情報を取得するための年月リスト。
    """
    ym_list = []
    for year in range(1990, 2025):
        for month in range(1, 13):
            month_str = str(month).zfill(2)
            ym_list.append(str(year) + month_str)
    return ym_list


def gen_url_for_access_to_calendar():
    """
    このURLからカレンダーの情報を参照。
    カレンダーからレースがあった日のレースリストページのURLを取得。
    """
    urls = []
    for ym in gen_year_month():
        url = URL_RACE_LIST + ym
        urls.append(url)
    return urls


def test_gen_year_month():
    ym_list = gen_year_month()
    assert ym_list[0] == "199001"
    assert ym_list[1] == "199002"
    assert ym_list[-1] == "202412"


def test_gen_url_for_access_to_calendar():
    urls = gen_url_for_access_to_calendar()
    assert urls[0] == "https://db.netkeiba.com/race/list/199001"
    assert urls[1] == "https://db.netkeiba.com/race/list/199002"
    assert urls[-1] == "https://db.netkeiba.com/race/list/202412"


if __name__ == "__main__":
    pass