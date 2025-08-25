FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

#-u is needed so the prints come up. Otherwise they dont show in real time.
CMD ["python", "-u", "app.py"]

