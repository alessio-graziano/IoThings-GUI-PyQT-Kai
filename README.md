# IoThings-GUI-PyQT-Kai

Codice del Workshop **GUI con EMBEDDED LINUX e PytQT su schede KAY**

## Kai build tools

1. Per creare un container con l'immagine kai basta eseguire il comando:

`docker run -d -it -v ~/SMLCD72-Kai:/Kai --network host --name kai-boards-sigmastar-host shinsekaisrl/kai-boards-sigmastar-host /bin/bash`

2. Clonare il repository nella cartella
`git clone https://github.com/alessio-graziano/IoThings-GUI-PyQT-Kai.git`

## Hello world

Per compilare dal container Docker spostarsi nella cartella hello_world ed eseguire:

`arm-linux-gnueabihf-gcc hello_world.c -o hello_world`

Per il debug punto punto su scheda KAI utilizzare visual studio code ed una distribuzione Kai-full

## BME280

Per avviare la demo copiare il file read_bme280 sulla board (Es. `scp read_bme280.py kai@kai.local:/home/kai`).

Installare smbus2 e bme280 usando pip: `pip install smbus2 bme280`

Eseguire con python: `python3 read_bme280.py`

## BME280-PyQT

Per avviare la demo copiare la cartella sulla board (Es. `scp -R BME280-pyQT kai@kai.local:/home/kai`)

Installare smbus2 e bme280 se non fatto precedentemente.

Eseguire: `python3 main.py`
