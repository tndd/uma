from requests import get


def fetch_html(
    url: str,
    save_path: str,
    encoding: str = 'UTF-8',
) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = get(url, headers=headers)
    response.encoding = encoding
    if response.status_code == 200:
        with open(save_path, 'w', encoding='UTF-8') as file:
            file.write(response.text)
        print(f"HTML saved to {save_path}")
    else:
        print(f"Error: Status code {response.status_code}")