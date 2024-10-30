# django-apprunner-chatbot

Two types of apps:

App 1 - Static Page

AWS Apprunner -> Amazon ECR -> Docker -> Django - HTML + Tailwind CSS

App 2 - Single Page Application

Django REST API - AWS Amplify Gen 2 (Not installed in this repo) - React (Not installed in this repo)

## Features

* Authentication
  * Sign In, Sign Out
  * Uses email instead of username

## Requirements
Django 5.0

## Installation
Before running the application, make sure to install the necessary dependencies. Follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.

3. Assuming that you have a supported version of Python installed, you can first set up your environment with:
   ```
   python3.11 -m venv env
   . env/bin/activate
   ```
   Note: If `command not found: python3.11`, use `brew install python@3.11`

4. Install the backend dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
   This command will install all the Python packages listed in the `requirements.txt` file.

5. Perform necessary installation. This is to install Tailwind CSS.
   ```
   chmod +x ./scripts/install.sh
   ./scripts/install.sh
   ```

6. For local development, add this in `BASE_DIR/credentials.json`:
   ```
   {
      "SECRET_KEY": "django-xxxx",
      ...
   }
   ```

## Local Development
1. Activate environment
   ```
   . env/bin/activate
   ```

2. Run server locally
   ```
   python manage.py runserver
   ```

## Local Database Migration
1. Perform schema check
   ```
   python manage.py check
   ```

2. Perform make migrations
   ```
   python manage.py makemigrations
   ```

3. Apply migrations
   ```
   python manage.py migrate
   ```
## Deployment To Production
### Step 1: Preparation
Build docker. To run locally:
```
docker buildx build --platform=linux/amd64 -t chatbot .
docker run --platform=linux/amd64 -p 8000:8000 chatbot:latest
```

### Step 2: Deployment to AWS App Runner
```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 907965464542.dkr.ecr.us-east-1.amazonaws.com
docker tag chatbot:latest 907965464542.dkr.ecr.us-east-1.amazonaws.com/django-apprunner-chatbot/chatbot:latest
docker push 907965464542.dkr.ecr.us-east-1.amazonaws.com/django-apprunner-chatbot/chatbot:latest
```

## Troubleshooting
### CSS classes not being applied from Tailwind CSS
This error is due to Tailwind not finding any classes to scan in what it 'thinks' is your HTML code directories. To fix, run:
```
./scripts/install.sh
```