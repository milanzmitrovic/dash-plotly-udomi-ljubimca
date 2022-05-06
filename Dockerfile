
FROM python:3.7

COPY . /app_folder

WORKDIR app_folder

RUN pip install -r requirements.txt

EXPOSE 8050

CMD ["python", "app.py"]



