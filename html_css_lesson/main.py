import requests
from bs4 import BeautifulSoup

"""


"""
# url = "https://store.steampowered.com/search/?filter=topsellers"
# url = "https://store.steampowered.com/specials#tab=TopSellers"
# url = "https://store.steampowered.com/search/results/?query&start=50&count=50&dynamic_data=&sort_by=_ASC&supportedlang=ukrainian&snr=1_7_7_7000_7&filter=topsellers&infinite=1"
url = "https://www.work.ua/jobs-kyiv-"
# query = input("Введіть назву вакансії: ")
query = "python developer"
query = query.replace(" ", "+")
url += query
response = requests.get(url)

html = response.text
soup = BeautifulSoup(html, "html.parser")


def get_salary(div):
    salary_div = div.find("div", class_=None)
    if salary_div:
        return salary_div.span.text


def get_company(div):
    company_div = div.find("div", class_="mt-xs")

    return company_div.span.text


def get_title(div):
    return div.h2.a.text


def get_details(div):
    id_ = div.find("h2", class_="my-0").a["href"]
    url = f"https://www.work.ua{id_}"
    response = requests.get(url)

    html = response.text
    soup_ = BeautifulSoup(html, "html.parser")

    info_ul = soup_.find("ul", class_="list-unstyled sm:mt-2xl mt-lg mb-0")

    address_li = info_ul.find_all("li", class_="text-indent no-style mt-sm mb-0")
    for li in address_li:
        if li.span["title"] == "Адреса роботи":
            address = li.text.split()
            address = " ".join(address)
            address = address.replace("На мапі", "")

            print(address)

    phone_span = soup_.find("span", id="contact-phone")
    if phone_span:
        print(phone_span.a.text)
    # print()


for div in soup.find_all(
    "div",
    class_="card card-hover card-search card-visited wordwrap job-link js-job-link-blank mt-lg",
) + soup.find_all(
    "div",
    class_="card card-hover card-search card-visited wordwrap job-link js-job-link-blank",
):
    # print(div)
    print("назва:", get_title(div))
    print("компанія:", get_company(div))

    salary = get_salary(div)
    if salary:
        print("зп:", salary)

    get_details(div)

    print()

[]
"""
O(n^2)
O(n^3)
O(n)
O(n*log(n))
"""

"""
є список чисел
у ньому точно є два числа сума яких дорівнює 3
знайдіть ці числа

"""
