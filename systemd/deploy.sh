#!/usr/bin/env bash


SYSTEMD_FILE=${file}

sudo cp "./$SYSTEMD_FILE" /etc/systemd/system/
sudo sudo systemctl enable $SYSTEMD_FILE
sudo systemctl start $SYSTEMD_FILE

sudo systemctl status $SYSTEMD_FILE


echo 'Деплой успешно завершился!'


