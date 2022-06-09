
.PHONY: run mqtt_conf all source_config copy_source_config

LOGIN_USER=kai
TARGETIP=192.168.0.210
APP_NAME=bmp280

DEPLOY_PATH=/home/$(LOGIN_USER)/$(APP_NAME)

run_local:
	cd src && python3 main.py

run:
	echo "Running $(APP_NAME) on board with IP" $TARGETIP
	@ssh $(LOGIN_USER)@$(TARGETIP) mkdir -p /tmp/$(APP_NAME)
	@scp src/* $(LOGIN_USER)@$(TARGETIP):/tmp/$(APP_NAME)
	@ssh $(LOGIN_USER)@$(TARGETIP) "cd /tmp/$(APP_NAME) && sudo QT_QPA_PLATFORM=linuxfb python main.py"
#	ssh $(LOGIN_USER)@$(TARGETIP)
deploy: 
	echo "Deploying $(APP_NAME) on board with IP" $TARGETIP
	@ssh $(LOGIN_USER)@$(TARGETIP) mkdir -p $(DEPLOY_PATH)
	@scp src/* $(LOGIN_USER)@$(TARGETIP):$(DEPLOY_PATH)
	@ssh $(LOGIN_USER)@$(TARGETIP) "sudo echo \"cd $(DEPLOY_PATH) && sudo QT_QPA_PLATFORM=linuxfb python main.py &\" | sudo tee -a /customer/demo.sh"
	@ssh $(LOGIN_USER)@$(TARGETIP) "sudo chmod +x /customer/demo.sh"
	@ssh $(LOGIN_USER)@$(TARGETIP) "sudo reboot"

source_config: 
	echo "No source configuration, compile for smlcd version full"

copy_source_config:
