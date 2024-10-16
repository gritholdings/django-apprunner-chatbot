FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

# Ensure the start.sh script is executable
RUN chmod +x /app/start.sh

# The entrypoint script will run before the application starts
CMD ["/app/start.sh"]