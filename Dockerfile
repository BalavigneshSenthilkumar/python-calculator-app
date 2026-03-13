FROM python:3.12-slim

# install tkinter system dependency
RUN apt-get update && apt-get install -y python3-tk tk

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
