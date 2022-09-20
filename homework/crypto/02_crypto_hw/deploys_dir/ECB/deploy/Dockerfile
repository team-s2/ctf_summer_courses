# sudo docker build -t ecb_test:latest .
# sudo docker run -p 13100:13100 ecb_test:latest
FROM ubuntu:20.04

RUN apt-get -qq update && apt-get install -qq --no-install-recommends xinetd python3-pip
RUN apt-get install -qq --no-install-recommends netcat
RUN pip3 install pycryptodome

COPY ecb_test.py /
COPY secret.py /
COPY service.conf /
COPY wrapper /

RUN chmod +x /ecb_test.py /secret.py
RUN chmod +x /service.conf /wrapper

EXPOSE 13100

CMD ["/usr/sbin/xinetd", "-filelog", "/dev/stderr", "-dontfork", "-f", "/service.conf"]