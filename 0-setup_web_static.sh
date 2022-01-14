#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

apt-get update
apt-get -y install nginx
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "simple content, to test your Nginx configuration" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -hR ubuntu:ubuntu /data/
sed -i '/^\tserver_name.*/a \\n\tlocation /hbnb_static/ \{\n\t\talias /data/web_static/current/;\n\t\}\n' /etc/nginx/sites-available/default
service nginx restart
