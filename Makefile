install:
	pip install -r requirements.txt
generate_service:
	./systemd/generate_service.sh
deploy:
	./systemd/deploy.sh
logs:
	systemctl status ${file}
