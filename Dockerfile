FROM python:3.7-stretch


# 新代码
COPY . /app

RUN pip3 install pip --upgrade --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple \
 && pip3 install --no-cache-dir -r /app/pip-freeze.txt -i https://mirrors.aliyun.com/pypi/simple

WORKDIR /app

EXPOSE 8002

# ENTRYPOINT ["./start.sh"]
CMD [""]


