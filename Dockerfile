# pull official base image
FROM python:3.8.0-alpine

#Add User
RUN adduser -D testapp

# set work directory
WORKDIR /testapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /testapp/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /testapp/

RUN chown -R testapp:testapp /testapp

USER testapp

#Port
EXPOSE 5000

#command
CMD ["gunicorn", "--b", "127.0.0.1:8000", "wsgi:app"]
#CMD ["python", "app.py"]