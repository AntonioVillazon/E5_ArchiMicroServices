FROM python:3.7.3


ADD requirements.txt /
ADD credits.py /


RUN pip install -r requirements.txt
EXPOSE 5006
CMD ["python", "credits.py"]