FROM python:3.9

EXPOSE 8501

WORKDIR /app

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["streamlit","run","app.py", "--server.port", "8501"]