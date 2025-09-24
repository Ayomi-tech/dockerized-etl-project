FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Run 'main.py' file whenever container launches
CMD ["python", "main.py"]

