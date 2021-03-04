FROM python:3.7.3

ADD requirements.txt /
ADD search.py /

RUN pip install -r requirements.txt
EXPOSE 5003
CMD ["python", "./search.py"]