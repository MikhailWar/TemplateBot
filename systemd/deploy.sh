#!/usr/bin/env bash

envfile='./env_tgbot'
export $(grep -v '^#' $envfile | xargs)

SYSTEMD_FILE=${SYSTEMD_FILE_PROJECT}




sudo cp "./$SYSTEMD_FILE" /etc/systemd/system/
sudo sudo systemctl enable $SYSTEMD_FILE
sudo systemctl start $SYSTEMD_FILE

sudo systemctl status $SYSTEMD_FILE


echo 'Деплой успешно завершился!'


