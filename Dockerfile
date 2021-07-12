# Select Base Image
FROM python:3.8-slim
# Update and install required os packages
RUN apt-get update -y
RUN apt-get install gcc -y

# Copy src and install dependencies
WORKDIR app
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app
# Expose Port
EXPOSE 8080
# Run webserver
# TODO : nginx gunicorn
# CMD ["python", "manage.py", "0.0.0.0:8080"]
# CMD ["gunicorn", "backend.wsgi:application", "--workers", "3","--bind", ":8000"]
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "3"]
