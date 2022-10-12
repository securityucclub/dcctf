FROM ubuntu:22.04

RUN apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd sudo

RUN useradd -m ctf
RUN echo "ctf:ctf" | chpasswd

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail
COPY ./sudoers /etc/sudoers
COPY ./flag.txt /root/flag.txt

RUN chmod +x /start.sh
RUN chmod 400 /root/flag.txt

CMD ["/start.sh"]

EXPOSE 5000
