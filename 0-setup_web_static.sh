#!/usr/bin/env bash
# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file with content
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Ensure ownership of the /data folder by ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Remove existing symbolic link if it exists
sudo rm -rf /data/web_static/current

# Create a symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Update Nginx configuration
config_content="server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}"

echo "$config_content" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0