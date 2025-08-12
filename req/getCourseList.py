import requests



def get_Course_list(cmesid):
    login_url = "https://www.cmechina.net/cme/myHome.jsp"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }

    cookies = {"cmesid": cmesid}

    # 发送POST请求进行登录，带上表单数据和请求头
    response = requests.get(login_url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        personal_info, table_info = extract_info(response.text)
        return personal_info, table_info
    else:
        print("登录失败，状态码：", response.status_code)

from bs4 import BeautifulSoup

def extract_info(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 提取个人信息
    personal_info = {
        '姓名': soup.find('h4').text.split('，')[1],
        '科室': soup.find('p', class_='user_department').text.split('：')[1],
        '机构': soup.find_all('p')[2].text.split('：')[1],
        '单位': soup.find_all('p')[3].text.split('：')[1]
    }

    # 提取表格信息
    table = soup.find('table', class_='home_table')
    rows = table.find_all('tr')[1:]
    table_info = []
    for row in rows:
        cols = row.find_all('td')
        a_tag = cols[0].find('a')
        if a_tag:
            course_id = a_tag['href'].split('=')[1]
        else:
            course_id = None
        table_info.append({
            '项目名称': cols[0].text.split('\n')[0],
            # '项目编号': cols[0].text.split('项目编号：')[1].strip(), # 地区账号课程不同导致，可能会出现问题
            '学分': cols[1].text,
            '学习状态': cols[2].text,
            '操作': cols[4].text,
            'course_id': course_id
        })

    return personal_info, table_info
if __name__ == '__main__':
    personal_info, table_info = get_Course_list("fa3753f3-4bda-4b46-b1f3-7ac237cb3ac3")
    print(personal_info, table_info)