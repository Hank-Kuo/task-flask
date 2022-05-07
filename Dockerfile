FROM python:3.9-slim

ENV FLASK_ENV="production"

COPY . /code
WORKDIR /code

RUN pip install -r requirements.txt
CMD [ "python", "-m", "task.run"]

EXPOSE 5000 