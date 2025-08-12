# 使用官方的Python基础镜像，这里以Python 3.11为例
FROM python:3.10.8

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的 /app 目录下
COPY . /app

# 安装项目依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露FastAPI应用运行的端口，这里假设应用运行在8000端口
EXPOSE 3000

# 设置容器启动时执行的命令，这里是运行FastAPI应用
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]