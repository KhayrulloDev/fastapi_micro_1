FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["sh", "-c", "alembic revision --autogenerate -m 'autogenerate migration' && alembic upgrade head && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]

