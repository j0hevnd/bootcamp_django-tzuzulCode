FROM python:3

WORKDIR /src

COPY requirements.txt /src

RUN pip install -r requirements.txt

COPY . /src

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]