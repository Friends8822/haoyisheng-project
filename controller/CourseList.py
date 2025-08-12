from time import sleep

from fastapi import APIRouter, Request, Body
from starlette.templating import Jinja2Templates

from req.examDo import exam_do
from req.getCourseList import get_Course_list
from req.getExam import get_exam
from req.getProductId import get_product_id
from req.getkjList import get_kj_list

courseList = APIRouter()
templates = Jinja2Templates(directory="static/templates")

#获取课程列表
@courseList.get("/allList")
def getCourseList(request: Request, cmesid: str = None):
    personal_info, table_info = get_Course_list(cmesid)

    return templates.TemplateResponse(
        "courseList.html", #模板文件
        {
            "request": request,
            "personal_info": personal_info,
            "table_info": table_info,
            "cmesid": cmesid,
        }) #上下文对象


#获取课件
@courseList.get("/course")
def getCourse(request: Request,cmesid:str = None, course_id: str = None):
    kjlb = get_kj_list(cmesid = cmesid, course_id = course_id)

    # print(kjlb)
    return templates.TemplateResponse(
        "kjlb.html",  # 模板文件
        {
            "request": request,
            "cmesid": cmesid,
            "kjlb": kjlb,
            "course_id": course_id,
        })  # 上下文对象

@courseList.post("/yijian")
def yijian(cmesid:str = None, course_id: str = None):
    pass

#考试请求
@courseList.post("/exam")
def exam(data=Body()):
    cmesid = data['cmesid']
    course_id = data['course_id']
    courseware_id = data['courseware_id']
    product_id = get_product_id(cmesid = cmesid,course_id = course_id,courseware_id = courseware_id)
    # 拿到cmesid，course_id，courseware_id 去获取product_id
    print(f'product_id:{product_id}')
    # 获取考试题参数
    ques_num, fail_num, sign, ques_list, answ_num_list = get_exam(cmesid=cmesid,course_id=course_id,paper_id=courseware_id,product_id=product_id)


    #开始考试
    ee = xhk(cmesid=cmesid,course_id=course_id,courseware_id=courseware_id,product_id=product_id,ques_num=ques_num,fail_num=fail_num,
        sign=sign,ques_list=ques_list,answ_num_list=answ_num_list)

    return ee


def xhk ( cmesid: str = None,
          course_id: str = None,
          courseware_id: str = None,
          product_id: str = None,
          ques_num: str = None,
          fail_num: str = None,
          sign: str = None,
          ques_list: str = None,
          answ_num_list: str = None,
        ):

    #初始化选项
    int_list = [int(num) for num in answ_num_list.split(",")]

    def init(int_list):
        mapping = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E"
        }
        result = []
        for num in int_list:
            if num in mapping:
                result.append(mapping[num])
        return result

    bj = int_list

    # 判断结果
    def ed(kk, bj):
        if kk == "考试通过":
            return "考试通过"
        else:
            for x in range(len(kk)):
                if kk[x][2] == "dui":
                    print()
                else:
                    int_list[x] -= 1
        return int_list
    for i in range(5):
        bjn = init(bj)
        # 开始考试
        exam_jieguo = exam_do(cmesid=cmesid,
                              course_id=course_id,
                              paper_id=courseware_id,
                              cw_id=product_id,
                              ques_num=ques_num,
                              fail_num=fail_num,
                              sign=sign,
                              ques_list=ques_list,
                              answ_num_list=answ_num_list,
                              xx = bjn)


        sleep(5)
        bjn = ed(exam_jieguo, bj)
        # print(bjn)



    return "考试通过"
