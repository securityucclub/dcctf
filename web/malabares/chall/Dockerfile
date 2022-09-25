FROM ubuntu:20.04

ENV TZ=America/Santiago
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y apache2 php systemctl curl

RUN service apache2 start
COPY ./files/index.php /var/www/html
COPY ./files/flag.php /var/www/html
COPY ./files/robots.txt /var/www/html
COPY ./files/source.zip /var/www/html

COPY ./start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]

EXPOSE 80
