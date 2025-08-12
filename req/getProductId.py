import requests
import re


def get_product_id(cmesid, course_id, courseware_id):
    url = f"https://www.cmechina.net/cme/study2.jsp?course_id={course_id}&courseware_id={courseware_id}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }

    cookies = {"cmesid": cmesid}

    # 发送POST请求进行登录，带上表单数据和请求头
    response = requests.get(url, headers=headers, cookies=cookies)

    if response.status_code == 200:
        product_id = re.search(r'product_id=(\d+)', response.text)
        if product_id:
            return product_id.group(1)
        else:
            print("未找到product_id")
    else:
        print("登录失败，状态码：", response.status_code)

if __name__ == '__main__':
    product_id_value = get_product_id("2bd82c18-4d61-4e2c-a788-69688fe0309c", "202401007175", "07")
    print(product_id_value)