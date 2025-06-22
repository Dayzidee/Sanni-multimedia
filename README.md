# Sanni Multimedia Gallery

A Django-based multimedia gallery application for uploading and viewing images.

## Features
- Image upload functionality
- Gallery view with responsive design
- Admin interface for content management
- Static file serving with WhiteNoise

## Deployment on Render

This application is configured for deployment on Render. Here's how to deploy:

### 1. Fork/Clone this repository

### 2. Create a new Web Service on Render
- Go to [render.com](https://render.com)
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select this repository

### 3. Configure the deployment
- **Name**: `sanni-multimedia` (or your preferred name)
- **Region**: Choose closest to your location
- **Branch**: `main`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn myproject.wsgi:application`
- **Plan**: Free

### 4. Add Environment Variables
In the Environment section, add:
- `SECRET_KEY`: A secure secret key for Django
- `DJANGO_DEBUG`: `False` (for production)
- `DATABASE_URL`: (Render will provide this if you add a PostgreSQL database)

### 5. Deploy
Click "Create Web Service" and wait for the deployment to complete.

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   export SECRET_KEY="your-secret-key"
   export DJANGO_DEBUG="True"
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure
- `gallery/`: Main application with models, views, and templates
- `media/`: Uploaded images storage
- `static/`: Static files (CSS, JS, images)
- `myproject/`: Django project settings
- `requirements.txt`: Python dependencies
- `runtime.txt`: Python version specification
- `build.sh`: Build script for Render deployment

