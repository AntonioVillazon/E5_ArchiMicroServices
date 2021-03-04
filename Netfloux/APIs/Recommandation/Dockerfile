FROM python:3.7.3


ADD requirements.txt /
ADD recommandation.py /


RUN pip install -r requirements.txt
EXPOSE 5002
CMD ["python", "./recommandation.py"]