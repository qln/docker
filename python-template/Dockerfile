FROM zangxn/python35-django2-uwsgi:base

COPY nginx.conf /etc/nginx/nginx.conf

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN mkdir /usr/local/app

WORKDIR /usr/local/app

COPY ./hello/ .

COPY ./uwsgi.ini .

EXPOSE 80

CMD ["/entrypoint.sh"]
