Fiware-IoT-Docker.git

This repository contains a Dockerized implementation of an IoT Architecture using FIWARE(https://www.fiware.org/) and Docker(https://www.docker.com/). <br>

The repository is composed of: 
* **docker-compose.yml:** contains the YAML file to implement an architecture with Orion Context Broker(https://fiware-orion.readthedocs.io/en/master/), Cygnus(https://github.com/telefonicaid/fiware-cygnus) for persistence, MySQL database , and connected to Grafana(https://grafana.com/) for visualization

## Getting Started

Just download the repository 


```bash
git clone https://github.com/tavitto16/fiware-iot-docker.git
```


move into the main folder and type: 

```bash
sudo docker-compose up
```

Then the screen will start the services as follows:

* Context Broker at port 1026
* Cygnus at port 5050
* MySQL at port 3306
* Grafana at  port 3000

For the IDAS implementation, you can run it into a raspberry pi by copying the IDAS folder and setting your credentials into the config.ini file. If you wish to use Fiware Oauth Generic Enables, please register at FiwareLab() and get tokens using the file get_token.py

# Requirements: 

* Docker compose
* Python +2.7

# Acknowledge

Please contact Gustavo Hernández(ghp@gatv.ssr.upm.es) José Gonzalez (jose.glezes@gmail.com) for further details. 

