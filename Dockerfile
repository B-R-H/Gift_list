FROM python:3
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY ./ /app
EXPOSE 5000
ENTRYPOINT ["python","app.py"]
