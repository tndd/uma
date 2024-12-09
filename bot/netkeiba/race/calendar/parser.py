import os

from bs4 import BeautifulSoup

from bot.netkeiba.const import PATH_CALENDAR_CACHE, PATH_RACE_DAY_URLS, URL_BASE


def parse_calendar(html: str) -> list[str]:
    """
    カレンダーから開催日のurlを抜き出し、リストで返す。
    """
    soup = BeautifulSoup(html, 'html.parser')
    race_calendar_div = soup.find('div', class_='race_calendar')
    race_table = race_calendar_div.find('table', summary="レーススケジュールカレンダー")
    urls = [URL_BASE + a['href'].rstrip('/') for a in race_table.find_all('a', href=True)]
    return urls


def extract_store_race_day_urls() -> list[str]:
    html_files = [f for f in os.listdir(PATH_CALENDAR_CACHE) if f.endswith('.html')]
    all_urls = []
    for html_file in html_files:
        with open(os.path.join(PATH_CALENDAR_CACHE, html_file), 'r', encoding='UTF-8') as file:
            html = file.read()
            urls = parse_calendar(html)
            all_urls.extend(urls)
    # URLをテキストファイルに保存
    with open(PATH_RACE_DAY_URLS, 'w', encoding='UTF-8') as output_file:
        for url in all_urls:
            output_file.write(url + '\n')


def test_parse_calendar():
    html = """
        <div class="race_calendar_wrap">
        <div class="race_calendar">
        <h2><img src="https://cdn.netkeiba.com/img.db//style/netkeiba.ja/image/race_side_h_03.png" alt="レーススケジュール"></h2>
        <dl>
        <dt class="fc">
        <span>1990年&nbsp;<strong>01月</strong></span>
        <ul>
        <li class="rev">
        <a href="/?pid=race_kaisai&amp;syusai=10&amp;date=19890105" title="前へ"><img src="https://cdn.netkeiba.com/img.db//style/netkeiba.ja/image/race_calendar_rev_01.gif" alt="前へ"></a>

        <a href="/?pid=race_kaisai&amp;syusai=10&amp;date=19891202" title="前へ"><img src="https://cdn.netkeiba.com/img.db//style/netkeiba.ja/image/race_calendar_rev_02.gif" alt="前へ"></a>

        </li>
        <li class="next">
        <a href="/?pid=race_kaisai&amp;syusai=10&amp;date=19910105" title="次へ"><img src="https://cdn.netkeiba.com/img.db//style/netkeiba.ja/image/race_calendar_next_01.gif" alt="次へ"></a>

        <a href="/?pid=race_kaisai&amp;syusai=10&amp;date=19900203" title="次へ"><img src="https://cdn.netkeiba.com/img.db//style/netkeiba.ja/image/race_calendar_next_02.gif" alt="次へ"></a>

        </li>
        </ul>
        </dt>
        <dd>
        <table cellpadding="0" cellspacing="3" border="0" summary="レーススケジュールカレンダー">
        <tbody><tr>
        <th>月</th>
        <th>火</th>
        <th>水</th>
        <th>木</th>
        <th>金</th>
        <th class="sat">土</th>
        <th class="sun">日</th>
        </tr>
        <tr>
        <td>1</td><td>2</td><td>3</td><td>4</td><td class="selected"><a href="/race/list/19900105/">5</a></td><td class="sat"><a href="/race/list/19900106/">6</a></td><td class="sun"><a href="/race/list/19900107/">7</a></td>
        </tr><tr>
        <td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td class="sat"><a href="/race/list/19900113/">13</a></td><td class="sun"><a href="/race/list/19900114/">14</a></td>
        </tr><tr>
        <td class="sun"><a href="/race/list/19900115/">15</a></td><td>16</td><td>17</td><td>18</td><td>19</td><td class="sat"><a href="/race/list/19900120/">20</a></td><td class="sun"><a href="/race/list/19900121/">21</a></td>
        </tr><tr>
        <td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td class="sat"><a href="/race/list/19900127/">27</a></td><td class="sun"><a href="/race/list/19900128/">28</a></td>
        </tr><tr>
        <td>29</td><td>30</td><td>31</td><td class="no_day">&nbsp;</td><td class="no_day">&nbsp;</td><td class="no_day">&nbsp;</td><td class="no_day">&nbsp;</td>
        </tr>
        </tbody></table>
        </dd>
        </dl>
        </div>
        </div>
        """
    urls = parse_calendar(html)
    assert len(urls) == 10
    assert urls[0] == "https://db.netkeiba.com/race/list/19900105"
    assert urls[1] == "https://db.netkeiba.com/race/list/19900106"
    assert urls[-1] == "https://db.netkeiba.com/race/list/19900128"
