from bot.netkeiba.const import PATH_RACE_DAY_URLS


def read_race_day_urls():
    with open(PATH_RACE_DAY_URLS, 'r', encoding='UTF-8') as file:
        return [line.strip() for line in file.readlines()]


def test_read_race_day_urls():
    urls = read_race_day_urls()
    assert len(urls) > 0
    assert urls[0] == 'https://db.netkeiba.com/race/list/20050903'
    assert urls[-1] == 'https://db.netkeiba.com/race/list/20210131'


if __name__ == '__main__':
    test_read_race_day_urls()
