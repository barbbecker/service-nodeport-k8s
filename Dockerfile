FROM python:3.8.9-alpine

RUN pip install flask

ENV TESTE=Barbara

WORKDIR /app/

COPY application.py .

EXPOSE 5000

CMD ["python", "application.py"]