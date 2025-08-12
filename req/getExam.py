import requests
import time
from urllib.parse import quote

from req.getProductId import get_product_id

from bs4 import BeautifulSoup

def get_values_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    form = soup.find('form', {'name': 'form1'})

    ques_num = form.find('input', {'name': 'ques_num'}).get('value')
    fail_num = form.find('input', {'name': 'fail_num'}).get('value')
    sign = form.find('input', {'name': 'sign'}).get('value')
    ques_list = form.find('input', {'name': 'ques_list'}).get('value')
    answ_num_list = form.find('input', {'name': 'answ_num_list'}).get('value')

    return ques_num, fail_num, sign, ques_list, answ_num_list
def get_exam(cmesid,course_id,paper_id,product_id):
    # 要请求的网址
    url = f"https://www.cmechina.net/cme/exam.jsp?course_id={course_id}&paper_id={paper_id}&type=7&product_id={product_id}"
    # 设置请求头中的Cookie信息
    cookies = {
        "cmesid": cmesid,
    }
    # 设置请求头，添加User-Agent字段模拟Chrome浏览器，并添加Referer字段
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Referer": f"https://www.cmechina.net/cme/study2.jsp?course_id={course_id}&courseware_id={paper_id}"
    }
    try:
        # 发送GET请求，同时传入Cookie和设置好的请求头
        response = requests.get(url, cookies=cookies,headers=headers)
        # 检查响应状态码，如果是200表示请求成功
        if response.status_code == 200:
            get_values = get_values_from_html(response.text)
            return get_values
        else:
            print(f"请求失败，状态码：{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"请求发生异常：{e}")


if __name__ == '__main__':
    ff = get_product_id("2bd82c18-4d61-4e2c-a788-69688fe0309c","202401007175","07")
    print(ff)
    gg = get_exam("2bd82c18-4d61-4e2c-a788-69688fe0309c","202401007175","07",ff)
    print(gg)