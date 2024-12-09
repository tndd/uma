from bot.race import generate


def fetch_race_calender_html():
    urls = generate.gen_url_for_access_to_calendar()
    return urls



def test_fetch_race_calender_html():
    urls = fetch_race_calender_html()
    assert urls[0] == "https://db.netkeiba.com/race/list/199001"
    assert urls[1] == "https://db.netkeiba.com/race/list/199002"
    assert urls[-1] == "https://db.netkeiba.com/race/list/202412"
