debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
apt-get update && apt-get install -y apache2 php5  php5-mysql php5-sqlite sqlite3 mysql-server python libpython2.7 build-essential python-dev
sudo apt-get install -y python-PIL
cat > /etc/apache2/sites-available/000-default.conf << "EOF"
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName nao.dev
    DocumentRoot /var/www/Nao-App/public/
    <Directory /var/www/Nao-App/public/>
          Options Indexes FollowSymLinks
          AllowOverride none
          Order allow,deny
          allow from all
          RewriteEngine On
          RewriteCond %{REQUEST_FILENAME} -s [OR]
          RewriteCond %{REQUEST_FILENAME} -l [OR]
          RewriteCond %{REQUEST_FILENAME} -d
          RewriteRule ^.*$ - [NC,L]
          RewriteRule ^.*$ index.php [NC,L]
      </Directory>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOF
a2enmod rewrite
touch /var/log/apache2/error.log
touch /var/log/apache2/access.log
touch /etc/php5/apache2/conf.d/custom.ini
cat > /etc/php5/apache2/conf.d/custom.ini << "EOF"
short_open_tag = On
EOF
echo "export PYTHONPATH=\"/var/www/Nao-App/python/pynaoqi-2.7/\"" >> ~/.bashrc
echo "export PYTHONPATH=\"/var/www/Nao-App/python/pynaoqi-2.7/\"" >> /home/vagrant/.bashrc
echo "export PYTHONPATH=\"/var/www/Nao-App/python/pynaoqi-2.7/\"" >> /etc/apache2/envvars
source ~/.bashrc
source /home/vagrant/.bashrc
rm -rf /var/www/html
service apache2 restart
