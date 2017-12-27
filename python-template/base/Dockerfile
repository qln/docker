FROM python:3.5

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client libmysqlclient-dev \
		nginx \
		vim \
		curl \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN pip install mysqlclient django uwsgi
