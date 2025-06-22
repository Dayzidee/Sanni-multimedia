# Heroku Deployment Script for Sanni Multimedia App
Write-Host "Starting Heroku deployment..." -ForegroundColor Green

# Create Heroku app (replace 'sanni-multimedia-app' with your preferred name if taken)
Write-Host "Creating Heroku app..." -ForegroundColor Yellow
& "C:\Program Files\heroku\bin\heroku.cmd" create sanni-multimedia-app

# Add Heroku remote (if app was created via web interface)
# & "C:\Program Files\heroku\bin\heroku.cmd" git:remote -a sanni-multimedia-app

# Deploy to Heroku
Write-Host "Deploying to Heroku..." -ForegroundColor Yellow
git push heroku main

# Run migrations
Write-Host "Running database migrations..." -ForegroundColor Yellow
& "C:\Program Files\heroku\bin\heroku.cmd" run python manage.py migrate

# Collect static files
Write-Host "Collecting static files..." -ForegroundColor Yellow
& "C:\Program Files\heroku\bin\heroku.cmd" run python manage.py collectstatic --noinput

# Optional: Create superuser (comment out if not needed)
# Write-Host "Creating superuser..." -ForegroundColor Yellow
# & "C:\Program Files\heroku\bin\heroku.cmd" run python manage.py createsuperuser

# Open the app
Write-Host "Opening your app..." -ForegroundColor Green
& "C:\Program Files\heroku\bin\heroku.cmd" open

Write-Host "Deployment complete!" -ForegroundColor Green

