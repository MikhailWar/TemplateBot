#!/usr/bin/env bash

envfile=./env_tgbot

export $(grep -v '^#' $envfile | xargs)
systemd_file=./${SYSTEMD_FILE_PROJECT}


tgbot_service_data="""[Unit]
Description=TelegramBot
After=network.target

[Service]
User=root
WorkingDirectory=${WORKING_DIRECTORY}
ExecStart=${WORKING_DIRECTORY}/venv/bin/${PYTHON_VERSION} ${WORKING_DIRECTORY}/${RUN_FILE}
Environment="PYTHONIOENCODING=UTF8"
Restart=always

[Install]
WantedBy=multi-user.target
"""

echo "$tgbot_service_data" > $systemd_file;