FROM python:3.15.0a1-alpine3.22

WORKDIR /app

# copy all files in CURRENT DIR to WORKDIR (= /app)
COPY . .

# install dependencies (flask) => similar to "npm install"
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
