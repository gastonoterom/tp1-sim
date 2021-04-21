FROM python:3.9.2

RUN pip install pipenv

ADD . /flask-deploy

WORKDIR /flask-deploy


RUN pip install -r requirements.txt
RUN pip install gunicorn[gevent]

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:5000 wsgi:app --log-level info

