#!/bin/bash
set -e

# Run this as root on the Ubuntu droplet

echo "=== Installing system packages ==="
apt-get update
apt-get install -y python3-venv python3-pip postgresql postgresql-contrib nginx git

echo "=== Creating directories ==="
mkdir -p /var/www/mtp /var/log/gunicorn /run/gunicorn

echo "=== Cloning repo ==="
cd /var/www/mtp
git clone https://github.com/glenansell/morethanparrots-website.git .

echo "=== Creating virtualenv ==="
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Creating PostgreSQL user and database ==="
sudo -u postgres psql << EOF
CREATE USER mtpuser WITH PASSWORD 'mtppass';
CREATE DATABASE mtpdb OWNER mtpuser;
GRANT ALL PRIVILEGES ON DATABASE mtpdb TO mtpuser;
\c mtpdb
GRANT ALL ON SCHEMA public TO mtpuser;
EOF

echo "=== Creating .env file ==="
cat > /var/www/mtp/.env << 'ENVFILE'
DEBUG=False
SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_urlsafe(50))")
ALLOWED_HOSTS=morethanparrots.com,www.morethanparrots.com,localhost
DB_NAME=mtpdb
DB_USER=mtpuser
DB_PASSWORD=mtppass
DB_HOST=localhost
DB_PORT=5432
ENVFILE

echo "=== Running Django setup ==="
cd /var/www/mtp
source venv/bin/activate
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py createsuperuser --noinput --username admin --email admin@morethanparrots.com 2>/dev/null || true

echo "=== Setting permissions ==="
chown -R www-data:www-data /var/www/mtp /var/log/gunicorn /run/gunicorn

echo "=== Installing Gunicorn systemd service ==="
cp deploy/gunicorn.service /etc/systemd/system/gunicorn.service
systemctl daemon-reload
systemctl enable gunicorn
systemctl start gunicorn

echo "=== Installing Nginx config ==="
cp deploy/nginx-morethanparrots.conf /etc/nginx/sites-available/morethanparrots
rm -f /etc/nginx/sites-enabled/default
ln -sf /etc/nginx/sites-available/morethanparrots /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx

echo "=== Setup complete ==="
echo "Site should be live at http://morethanparrots.com"
echo "Admin: http://morethanparrots.com/admin/"
