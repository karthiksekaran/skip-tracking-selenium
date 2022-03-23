from requests import Session
from bs4 import BeautifulSoup as bs

with Session() as s:
    site = s.get("http://cyberautics.co.in/login.aspx")
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name": "csrf_token"})["value"]
    login_data = {"username": "SKY0038024042", "password": "3pyrLs", "csrf_token": token}
    s.post("http://cyberautics.co.in/login.aspx", login_data)
    home_page = s.get("http://cyberautics.co.in/Users/Createform.aspx")
    print(home_page.content)