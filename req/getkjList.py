import requests
from bs4 import BeautifulSoup


def extract_info(html):
    result = []
    soup = BeautifulSoup(html, 'html.parser')
    course_lists = soup.find_all('li', class_='course_list')
    for course in course_lists:
        course_tit = course.find('h3', class_='course_tit').text.strip()
        status_span = course.find('span', class_='kstg') or course.find('span', class_='xxz')
        status_text = status_span.text.strip() if status_span else "未学习"
        result.append([course_tit, status_text])
    result = courseware_id(result)
    return result

def courseware_id(result):
    new_list = []
    i = 0
    for sublist in result:
        sublist.append(f'{i + 1:02d}')
        new_list.append(sublist)
        i += 1
    return new_list


def get_kj_list(cmesid,course_id):
    url = f"https://www.cmechina.net/cme/course.jsp?course_id={course_id}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }

    cookies = {"cmesid": cmesid}

    # 发送POST请求进行登录，带上表单数据和请求头
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        kj_info = extract_info(response.text)
        return kj_info
    else:
        print("登录失败，状态码：", response.status_code)

if __name__ == '__main__':
    ff = get_kj_list("43387c54-0d75-478f-a56b-b786814b47c4","202301000020")

    print(ff)