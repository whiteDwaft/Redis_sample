FROM python:3.7

RUN pip install redis fastapi requests uvicorn

EXPOSE 80

COPY ./src /src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]

