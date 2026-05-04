# Django Student Portal - Deployment Guide

## Prerequisites

- Linux/Windows/macOS server with Python 3.8+
- PostgreSQL database (recommended for production)
- Nginx or Apache web server
- Gunicorn or uWSGI application server
- SSL certificate (from Let's Encrypt or similar)

---

## Option 1: Deploy on Linux with Gunicorn + Nginx

### 1. Server Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python, pip, and PostgreSQL
sudo apt install -y python3 python3-pip python3-venv postgresql postgresql-contrib

# Install Nginx
sudo apt install -y nginx

# Install Gunicorn system-wide
sudo pip3 install gunicorn
```

### 2. Clone Project

```bash
# Clone or upload project
cd /var/www
git clone <your-repo-url> django-student-portal
cd django-student-portal

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Database

```bash
# Create PostgreSQL database and user
sudo -u postgres psql

# In PostgreSQL shell:
CREATE DATABASE studentportal;
CREATE USER studentuser WITH PASSWORD 'strong_password';
ALTER ROLE studentuser SET client_encoding TO 'utf8';
ALTER ROLE studentuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE studentuser SET default_transaction_deferrable TO on;
ALTER ROLE studentuser SET default_transaction_read_committed TO 'committed read';
GRANT ALL PRIVILEGES ON DATABASE studentportal TO studentuser;
\q
```

### 4. Update Django Settings

Create `.env` file:

```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
SECRET_KEY=your-generated-secret-key-here
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=studentportal
DATABASE_USER=studentuser
DATABASE_PASSWORD=strong_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 5. Collect Static Files

```bash
source venv/bin/activate
python manage.py collectstatic --noinput
```

### 6. Create Gunicorn Service

Create `/etc/systemd/system/gunicorn_studentportal.service`:

```ini
[Unit]
Description=Gunicorn daemon for studentportal
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/django-student-portal
ExecStart=/var/www/django-student-portal/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:/run/gunicorn_studentportal.sock \
          studentportal.wsgi:application

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn_studentportal
sudo systemctl start gunicorn_studentportal
sudo systemctl status gunicorn_studentportal
```

### 7. Configure Nginx

Create `/etc/nginx/sites-available/studentportal`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /var/www/django-student-portal/staticfiles/;
    }

    location /media/ {
        alias /var/www/django-student-portal/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn_studentportal.sock;
    }

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        alias /var/www/django-student-portal/staticfiles/;
    }

    location /media/ {
        alias /var/www/django-student-portal/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn_studentportal.sock;
    }
}
```

Enable site:

```bash
sudo ln -s /etc/nginx/sites-available/studentportal /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 8. Set Up SSL with Let's Encrypt

```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com
```

---

## Option 2: Deploy on Heroku

### 1. Create Procfile

```
web: gunicorn studentportal.wsgi
release: python manage.py migrate
```

### 2. Update Settings

```bash
# Create .env for Heroku
ALLOWED_HOSTS=your-app.herokuapp.com
```

### 3. Deploy

```bash
heroku login
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

---

## Option 3: Deploy on PythonAnywhere

### 1. Upload Files

- Upload project to PythonAnywhere

### 2. Set Web App

- Create new web app
- Choose Python 3.9+
- Select Django

### 3. Configure

- Point source code to `/home/username/django-student-portal`
- Set virtual environment to `/home/username/.virtualenvs/studentportal`
- Update WSGI configuration

### 4. Database

- Use PythonAnywhere MySQL or external PostgreSQL

---

## Post-Deployment Checklist

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Test application
python manage.py runserver

# Check for issues
python manage.py check --deploy
```

---

## Monitoring & Maintenance

### View Logs

```bash
# Gunicorn logs
sudo journalctl -u gunicorn_studentportal -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

### Backup Database

```bash
# PostgreSQL backup
sudo -u postgres pg_dump studentportal > backup.sql

# Restore backup
sudo -u postgres psql studentportal < backup.sql
```

### Update Application

```bash
# Pull latest changes
git pull origin main

# Install new dependencies
source venv/bin/activate
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart service
sudo systemctl restart gunicorn_studentportal
```

---

## Security Best Practices

1. **Update System Regularly**
   ```bash
   sudo apt update && sudo apt upgrade
   ```

2. **Configure Firewall**
   ```bash
   sudo ufw allow 22
   sudo ufw allow 80
   sudo ufw allow 443
   sudo ufw enable
   ```

3. **Set Up Fail2Ban**
   ```bash
   sudo apt install fail2ban
   sudo systemctl enable fail2ban
   ```

4. **Regular Backups**
   - Database backups daily
   - Code backups to Git repository
   - Media files to cloud storage

5. **Monitor Logs**
   - Set up log aggregation
   - Monitor for errors
   - Track performance metrics

---

## Troubleshooting

### Gunicorn won't start

```bash
# Check permissions
sudo chown -R www-data:www-data /var/www/django-student-portal

# Check socket
ls -la /run/gunicorn_studentportal.sock

# View error logs
sudo journalctl -u gunicorn_studentportal -n 50
```

### Database connection fails

```bash
# Check PostgreSQL status
sudo service postgresql status

# Test connection
psql -U studentuser -d studentportal -h localhost
```

### Static files not loading

```bash
# Ensure correct permissions
sudo chown -R www-data:www-data /var/www/django-student-portal/staticfiles

# Recollect static files
source venv/bin/activate
python manage.py collectstatic --noinput --clear
```

---

## Performance Optimization

### Database

- Add indexes
- Use connection pooling
- Enable query caching

### Application

- Enable caching
- Minify static files
- Use CDN for static assets

### Server

- Enable gzip compression
- Optimize worker count
- Monitor resource usage

---

## Scaling Considerations

1. **Load Balancing**
   - Use multiple Gunicorn workers
   - Deploy behind load balancer

2. **Caching**
   - Use Redis for caching
   - Cache database queries

3. **Database**
   - Set up read replicas
   - Implement connection pooling
   - Regular backups

4. **Storage**
   - Use S3 for media files
   - Use CDN for static files

---

## Support & Resources

- [Django Deployment Documentation](https://docs.djangoproject.com/en/stable/howto/deployment/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Let's Encrypt](https://letsencrypt.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

**Happy Deploying!** 🚀
