FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend/

COPY ./requirements.txt /app/backend/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/backend/

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]
