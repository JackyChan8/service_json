FROM python:3.12

# set working directory
WORKDIR /opt/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000

# Run application
CMD ["bash", "-c", "while !</dev/tcp/db/5432; do sleep 1; done; alembic upgrade head; uvicorn main:app --reload"]