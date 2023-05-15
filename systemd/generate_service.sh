#!/usr/bin/env bash


tgbot_service_data="""[Unit]
Description=TelegramBot
After=network.target

[Service]
User=root
WorkingDirectory=${directory}
ExecStart=${directory}/venv/bin/${python} ${directory}/bot.py
Environment="PYTHONIOENCODING=UTF8"
Restart=always

[Install]
WantedBy=multi-user.target
"""

echo "$tgbot_service_data" > ${file};