FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install OpenCV and other system dependencies if needed
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
