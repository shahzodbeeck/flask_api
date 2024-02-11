import json
import aiohttp


async def down(link):
    url = "https://sssinstagram.com/r"
    data = {
        "link": f"{link}",
        "token": ""
    }
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "uz-UZ,uz;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/json;charset=UTF-8",
        "cookie": "random_n=eyJpdiI6ImQwTmNBMW1XWFo4K1Q2WUZxS2R6S0E9PSIsInZhbHVlIjoia3VGMzdLTlNTclcrNjFXdGFRelJoSWFxREpDTU1XQnh0Q1RUYkdKL3p2WlRzeis5WXFMR2lBeno2M0JGQjJkcSIsIm1hYyI6IjQ0MTAxZjk5OWE2MTc2MmM4MzljYTgwMTI0NmUwY2NjN2Y4YWZmOWNjYWZhZWIzMzA5OGUxNjgxN2U4Yjg0ODMiLCJ0YWciOiIifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IkVmVldUN2JhUXZ0Ykk5VlYzQU85bFE9PSIsInZhbHVlIjoiamtPNUpFanpSRGREVmtoMzRCT3daRTJDT21SR0RyNXRpY1k3RlhhenIxMEZKVGRBRi9Ea0ttWjNPVHBJbTZmZzlCMG1kQVlucEV6QkVJcWZxRFZNSEh6ZUZDK1o1Ukc2VmFBZDNLK0hXaE5reGRXN2tNRUEybXlUUldTU0k0blEiLCJtYWMiOiIzNTkzY2IyNDVlYzNiNDg2MjkyMWJmNjBkNGMxM2RiNDk0N2QxOGJahNjY5MGYwNWJlZTNjMDY1ZjEzNGU5YzNhIiwidGFnIjoiIn0%3D; sssinstagram_session=eyJpdiI6ImpQWWZFak9rMUJudExFYjJlNDhNTXc9PSIsInZhbHVlIjoiZElBY1d3K0ZrdVBnRkxZa0wrdUdtYVVialczOXFjelNkRHV6WEUrSXFibllTUXFQUUtwSmt3WFo1SmkrSVd1dllGK3NSVG5rTk1FT1p2Z0I5Qi9yMWZYcXU5cGsyanFOQXlpL2FGcnZraTZob3NyVFJWbk91Y3BuZDl4ZmdGRFYiLCJtYWMiOiJiYTYzOTRjOGYyM2ZlMGJjZTc1OGFkOWFiMTgxOWUyMWUzNzkyOGM3MmE0OTA3MjE5Y2RmYjY0MzdiYjE2NTQzIiwidGFnIjoiIn0%3D; _ga_90WCZ6NHEE=GS1.1.1691817399.2.0.1691817399.0.0.0; _ga=GA1.2.487178783.1691682727; _gid=GA1.2.960230855.1691817400; _gat_UA-3524196-4=1; __gads=ID=cd7938a141d46d56-22dbbe9d4dde00ab:T=1691682729:RT=1691817399:S=ALNI_Ma9-kCT3MZk3_L6vs4hU41NTUaRug; __gpi=UID=00000c5dbba4d1ee:T=1691682729:RT=1691817399:S=ALNI_Mbw4I2eL1H_BEIb55oPWwn1dNknew; _ga_CN2Z3TL83Y=GS1.2.1691817400.2.0.1691817434.26.0.0",
        "origin": "https://sssinstagram.com",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "x-xsrf-token": "eyJpdiI6IkVmVldUN2JhUXZ0Ykk5VlYzQU85bFE9PSIsInZhbHVlIjoiamtPNUpFanpSRGREVmtoMzRCT3daRTJDT21SR0RyNXRpY1k3RlhhenIxMEZKVGRBRi9Ea0ttWjNPVHBJbTZmZzlCMG1kQVlucEV6QkVJcWZxRFZNSEh6ZUZDK1o1Ukc2VmFBZDNLK0hXaE5reGRXN2tNRUEybXlUUldTU0k0blEiLCJtYWMiOiIzNTkzY2IyNDVlYzNiNDg2MjkyMWJmNjBkNGMxM2RiNDk0N2QxOGJhNjY5MGYwNWJlZTNjMDY1ZjEzNGU5YzNhIiwidGFnIjoiIn0="

    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            response_text = await response.text()
    response_data = json.loads(response_text)
    return response_data
async def instagram(url):
    headers = {
        'authority': 'instagrab.app',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.1.661703434.1685185653; _ga_FKM4JVNKDN=GS1.1.1690351182.7.0.1690351182.0.0.0',
        'origin': 'https://instagrab.app',
        'referer': 'https://instagrab.app/',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'page': url,
        'ftype': 'all',
        'ajax': '1',
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://instagrab.app/", headers=headers, data=data) as response:
            try:
                if response.status == 200:
                    matches = re.findall(r'<div class="card-body">.*?<a class="btn btn-primary btn-dl" rel="noreferrer" target="_blank" href="(.*?)">.*?</a>.*?</div>', await response.text(), re.DOTALL)

                    result = []
                    for match in matches:
                        link = match
                        title = match
                        type = 'mp4' if 'mp4' in title else 'jpg'

                        result.append({
                            'link': link,
                            'type': type,
                        })

                    import json
                    return result
                else:
                    return {"Error occurred:", response.status}
            except:
                return {"status": False, "message": "Something went wrong"}