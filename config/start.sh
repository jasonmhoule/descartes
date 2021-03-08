#!bin/bash

echo "SELENIUM_IP=$SELENIUM_IP" >> usr/local/lib/R/etc/Renviron

mkdir -p /home/$USER/.ssh
gsutil cp -r gs://jmh_config/jmh_config/.ssh /home/$USER/.ssh
gsutil cp -r gs://jmh_config/jmh_config/.gitconfig /home/$USER

/init
