FROM ubuntu:20.04

RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' \
            /etc/apt/sources.list && \
    apt-get clean && \
    apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get autoclean && \
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple \
                    flask requests \
                    grpcio grpcio-tools protobuf

WORKDIR /app
COPY . /app

RUN python3 -m grpc_tools.protoc \
            -I./proto \
            --python_out=./src \
            --grpc_python_out=./src \
            proto/kvstore.proto


WORKDIR scripts/

RUN chmod +x start_kvstore.sh
CMD ["./start_kvstore.sh"]
