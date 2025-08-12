import requests
from bs4 import BeautifulSoup




def exam_do(cmesid,course_id,paper_id,ques_num,fail_num,sign,cw_id,ques_list,answ_num_list,xx):



    ques_list = ques_list.split(",")

    cookies = {
        "cmesid": cmesid,
    }

    # 定义表单数据
    form_data = {
        "course_id": course_id,
        "paper_id": paper_id,
        "ques_num": ques_num,
        "fail_num": fail_num,
        "sign": sign,
        "cw_id": cw_id,
        f"ques_{ques_list[0]}": f"{xx[0]}",
        f"ques_{ques_list[1]}": f"{xx[1]}",
        f"ques_{ques_list[2]}": f"{xx[2]}",
        f"ques_{ques_list[3]}": f"{xx[3]}",
        f"ques_{ques_list[4]}": f"{xx[4]}",
        "ques_list": ques_list,
        "answ_num_list": answ_num_list
    }

    # print(form_data)
    # 设置请求头
    headers = {
        "referer": f"https://www.cmechina.net/cme/exam.jsp?course_id={course_id}&paper_id={paper_id}&type=7&product_id={cw_id}",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    }
    # print(headers)
    # 发送模拟请求（这里以提交表单数据为例）
    response = requests.post('https://www.cmechina.net/cme/examDo.jsp', cookies=cookies, data=form_data, headers=headers)
    # print(response.text)
    ger = get_exam_results(response.text)
    return ger


def get_exam_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    answer_lists = soup.find_all('li', class_='answer_list')

    if answer_lists:
        results = []
        for answer_list in answer_lists:
            h3 = answer_list.find('h3')
            question_text = h3.text.split('您的答案：')[0].strip()
            your_answer = h3.text.split('您的答案：')[1].strip()
            result = h3['class'][0]
            results.append([question_text, your_answer, result])
        return results
    else:
        show_exam_div = soup.find('div', class_='show_exam')
        if show_exam_div:
            return "考试通过"
        return "考试结果获取失败"


# if __name__ == '__main__':
#     # ff = get_product_id("43387c54-0d75-478f-a56b-b786814b47c4", "202301000020", "04")
#     # ques_num, fail_num, sign, ques_list, answ_num_list = get_exam("43387c54-0d75-478f-a56b-b786814b47c4", "202301000020", "04", ff)
#     xx = ['A','A','E','E','E',]
#
#
#     kk = exam_do(cmesid="43387c54-0d75-478f-a56b-b786814b47c4",
#                  course_id="202301000020",
#                  paper_id="09",
#                  cw_id='11812131',
#                  ques_num='5',
#                  fail_num='null',
#                  sign='739cf18c818050a1a14ae42e956a2799',
#                  ques_list='44317279283b4bf98f9e9751d7dc0723,5b98806ca2e74f999bef44449610bde5,5f8f83f566944f638ab87162178273f1,f71361b08d5f46c6802d95ebdd595c54,70c57eaa0c2d40e1b080cea19d840387',
#                  answ_num_list='5,5,5,5,5',
#                  xx=xx
#                  )
#     print(kk)
#     # print([['1、围绝经期是指从绝经前的这段时间开始（即从出现接近绝经的内分泌学、生物学和临床特征时起），至绝经后的第（）年。', 'D', 'cuo'], ['2、盆腔器官脱垂（POP）分类', 'D', 'cuo'], ['3、慢性盆腔痛指患者感受到的来自盆腔的疼痛，持续至少（）个月以上', 'D', 'cuo'], ['4、围绝经期女性盆底功能障碍性疾病康复治疗有哪些？', 'D', 'cuo'], ['5、压力性尿失禁可在以下（）情况发生', 'D', 'cuo']])
#     # print([['1、围绝经期是指从绝经前的这段时间开始（即从出现接近绝经的内分泌学、生物学和临床特征时起），至绝经后的第（）年。', 'C', 'cuo'], ['2、盆腔器官脱垂（POP）分类', 'C', 'cuo'], ['3、慢性盆腔痛指患者感受到的来自盆腔的疼痛，持续至少（）个月以上', 'C', 'cuo'], ['4、围绝经期女性盆底功能障碍性疾病康复治疗有哪些？', 'C', 'cuo'], ['5、压力性尿失禁可在以下（）情况发生', 'C', 'cuo']])
#     # print([['1、围绝经期是指从绝经前的这段时间开始（即从出现接近绝经的内分泌学、生物学和临床特征时起），至绝经后的第（）年。', 'B', 'cuo'], ['2、盆腔器官脱垂（POP）分类', 'B', 'cuo'], ['3、慢性盆腔痛指患者感受到的来自盆腔的疼痛，持续至少（）个月以上', 'B', 'cuo'], ['4、围绝经期女性盆底功能障碍性疾病康复治疗有哪些？', 'B', 'cuo'], ['5、压力性尿失禁可在以下（）情况发生', 'B', 'cuo']])
#     int_list = [int(num) for num in input_str.split(",")]
#
#
#     def init(int_list):
#         mapping = {
#             1: "A",
#             2: "B",
#             3: "C",
#             4: "D",
#             5: "E"
#         }
#         result = []
#         for num in int_list:
#             if num in mapping:
#                 result.append(mapping[num])
#         return result
#
# def ed():
#     if kk == "考试通过":
#         return "考试通过"
#     else:
#         for i,result in kk:
#             if result[2] == "cuo":
#                pp[i] -= pp[i]

