FROM python:3.9
RUN apt-get update
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
RUN /usr/local/bin/python -m pip install --upgrade pip
CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "8080"]
