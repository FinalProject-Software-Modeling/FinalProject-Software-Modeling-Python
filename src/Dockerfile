FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY /backend_python/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t neptcash_python_backend:1.0.0 .
# docker run -d -p 8000:8000 --name videogames_python_backend videogames_python_backend:1.0.0
