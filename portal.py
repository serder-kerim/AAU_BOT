import requests
from bs4 import BeautifulSoup

def main(ID, PASSWORD):
    __RequestVerificationToken, login_response_cookies  = get_request_verification_token()
    cookies_login = set_cookies(login_response_cookies, "login")
    header_login = get_header("login")
    data = {
        "__RequestVerificationToken": __RequestVerificationToken,
        "UserName": "UGR/8819/15",
        "Password": 1969
    }
    response_home = requests.post(login_url, headers=header_login, data=data, cookies=cookies_login, allow_redirects=False)
    cookies_home = set_cookies(response_home, "home")
    header_home = get_header("home")
    response = requests.post(grade_rep_url, headers=header_home, cookies=cookies_home)
    with open("web1.html", "w") as file:
        file.write(response.text)
    
    soup = BeautifulSoup(response.text, "html.parser")
    first_table = soup.find("table")
    rows = first_table.find_all("tr")
    table_data = row_data = []
    for row in rows:
        cells = row.find_all(["th",'td'])
        if "yrsm" in row.get('class', []):
            continue
        row_data = [cell.get_text(strip=True) for cell in cells]
        table_data.append(row_data)
    return table_data

def get_header(flag):

    if flag == "login":
        return {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "referer": "https://portal.aau.edu.et/"
        }
    elif flag == "home":
        return {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Google Chrome\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "referer": "https://portal.aau.edu.et/Home"
        }

def get_request_verification_token():
    response_login = requests.get(login_url)
    soup = BeautifulSoup(response_login.text, "html.parser")

    input_field = soup.find("input", {"name": "__RequestVerificationToken"})

    return input_field["value"], response_login.cookies

def set_cookies(response, flag):
    if flag == "login":
        count = 0
        cookies_ = {
            "__RequestVerificationToken" : "",
            "ARRAffinity" : ""
        }
        for cookie in response:
            if count==0:
                cookies_['__RequestVerificationToken'] = cookie.value
            else:
                cookies_['ARRAffinity']  = cookie.value
            count+=1
        return cookies_
    elif flag == "home":
        home_response_cookie = {}
        cookies__ = response.cookies
        for cookie in cookies__:
            home_response_cookie[cookie.name] = cookie.value
            return home_response_cookie

login_url = "https://portal.aau.edu.et/login"

grade_rep_url = "https://portal.aau.edu.et/Grade/GradeReport"
