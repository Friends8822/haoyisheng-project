from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
import markdown

md = APIRouter()
@md.get("/md", response_class=HTMLResponse)
async def read_md(request: Request):
    try:
        # 构建Markdown文件的路径，这里假设Markdown文件都存放在'md_files'目录下
        md_file_path = "README.md"
        with open(md_file_path, "r", encoding="utf-8") as md_file:
            md_content = md_file.read()
            # 将Markdown内容转换为HTML
            html_content = markdown.markdown(md_content)
            return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content=f"Markdown file {md_file_path} not found.", status_code=404)