from fastapi import APIRouter, Form, Request, HTTPException
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates


templates = Jinja2Templates(directory="static/templates")
token = APIRouter()
global global_cmesid
global_cmesid = ""



@token.get("/")
def login(request: Request,):

    return templates.TemplateResponse(
        "login.html", #模板文件
        {
            "request": request,
        }) #上下文对象
@token.post("/login")
def get_token(request: Request,cmesid: str = Form(),):
    global global_cmesid
    global_cmesid = cmesid
    print(f"cmesid:{cmesid}")

    if cmesid:
        # 登录成功后，重定向到/index页面，并将cmesid作为查询参数传递
        redirect_url = f"/Course/allList?cmesid={cmesid}"
        return RedirectResponse(url=redirect_url, status_code=302)
    else:
        raise HTTPException(status_code=401, detail="登录失败，请检查输入信息。")


