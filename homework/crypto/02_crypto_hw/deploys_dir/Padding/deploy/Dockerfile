# sudo docker build -t padding_orcale:latest .
# sudo docker run -p 13102:13102 padding_orcale:latest
FROM ubuntu:20.04

RUN apt-get -qq update && apt-get install -qq --no-install-recommends xinetd python3-pip
RUN apt-get install -qq --no-install-recommends netcat
RUN pip3 install pycryptodome

COPY padding_orcale.py /
COPY secret.py /
COPY service.conf /
COPY wrapper /

RUN chmod +x /padding_orcale.py /secret.py
RUN chmod +x /service.conf /wrapper

EXPOSE 13102

CMD ["/usr/sbin/xinetd", "-filelog", "/dev/stderr", "-dontfork", "-f", "/service.conf"]