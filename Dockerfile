FROM python:3.12.1-slim

RUN pip install requests==2.31.0

COPY script.py /app/

CMD /app/script.py
