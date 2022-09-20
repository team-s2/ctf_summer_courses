# sudo docker build -t cbc_test:latest .
# sudo docker run -p 13101:13101 cbc_test:latest
FROM ubuntu:20.04

RUN apt-get -qq update && apt-get install -qq --no-install-recommends xinetd python3-pip
RUN apt-get install -qq --no-install-recommends netcat
RUN pip3 install pycryptodome

COPY task.py /
COPY secret.py /
COPY service.conf /
COPY wrapper /

RUN chmod +x /task.py /secret.py
RUN chmod +x /service.conf /wrapper

EXPOSE 13101

CMD ["/usr/sbin/xinetd", "-filelog", "/dev/stderr", "-dontfork", "-f", "/service.conf"]