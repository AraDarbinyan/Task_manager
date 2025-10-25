FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

ENV DATABASE_URL=sqlite:///./taskmanager.db
ENV JWT_ALGORITHM=HS256
ENV JWT_SECRET_KEY=your_secret_key

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000