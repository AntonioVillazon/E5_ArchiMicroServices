FROM python:3.7.3

RUN mkdir /usr/src/app/
#COPY . /usr/src/app/
#WORKDIR /usr/src/app/

ADD moviesDB.db /usr/src/app/
ADD profilsDB.db /usr/src/app/
ADD requirements.txt /
ADD films_catalogue.py /

RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "./films_catalogue.py"]