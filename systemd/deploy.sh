#!/usr/bin/env bash

SYSTEMD_FILE="tgbot.service"
./generate_service.sh
sudo cp "./$SYSTEMD_FILE" /etc/systemd/system/
sudo sudo systemctl enable $SYSTEMD_FILE
sudo systemctl start $SYSTEMD_FILE

sudo systemctl status $SYSTEMD_FILE


echo 'Деплой успешно завершился!'


