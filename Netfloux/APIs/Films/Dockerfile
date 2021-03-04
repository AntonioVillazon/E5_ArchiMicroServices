FROM python:3.7.3


ADD requirements.txt /
ADD manage_films.py /


RUN pip install -r requirements.txt
EXPOSE 5004
CMD ["python", "manage_films.py"]