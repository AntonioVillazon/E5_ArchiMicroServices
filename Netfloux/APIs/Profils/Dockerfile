FROM python:3.7.3

ADD requirements.txt /
ADD manage_profils.py /

RUN pip install -r requirements.txt
EXPOSE 5005
CMD ["python", "./manage_profils.py"]