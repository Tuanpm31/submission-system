FROM python:3.8
# App setup
ADD . /code
WORKDIR /code

# Requirements installation
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "./entrypoint.sh"]


#COPY ./entrypoint.sh /
#ENTRYPOINT ["entrypoint.sh"]
#CMD ["python manage.py runserver"]