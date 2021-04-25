FROM python:3.8.9-alpine

RUN pip install flask

WORKDIR /app/

COPY application.py .

EXPOSE 80

CMD ["python", "application.py"]