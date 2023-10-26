FROM jerry9916/centos:8

WORKDIR /root/websocket-demo

COPY *.py *.txt /root/websocket-demo/

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8886

ENTRYPOINT ["python3", "server.py"]