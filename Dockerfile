FROM python:3.9-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY . ./
RUN chmod +x /code/start_server.sh
RUN chown -R www-data:www-data /code
CMD ["/code/start_server.sh"]
EXPOSE 8000