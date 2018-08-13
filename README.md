# AWS-IoT (Python)
Repositorio con scripts necesarios para la implementación de AWS IoT en Python.

## Prueba de lectura de puertos GPIO

El script consiste en realizar la lectura del GPIO de Raspberry mediante la acción de presionar el botón colocado en el GPIO 23.

```bash
python gpio.py
```

## Prueba de conexión

El script consiste en realziar una prueba de conexión mediante MQTT.

```bash
pip install paho-mqtt
python paho-mqtt.py
```

## Envío de información a AWS IoT Core

Para enviar datos a AWS se utiliza un script de prueba basado en Python.

```bash
python basicPubSub.py \
-e <endpoint> \ # <your-endpoint-id>.iot.ap-southeast-2.amazonaws.com
-r <rootCAFilePath> \ # root-CA.pem
-c <certFilePath> \ # <your-cert-id>-certificate.pem.crt
-k <privateKeyFilePath> \ # <your-cert-id>-private.pem.key
-id <clientId> \ # autobot
-t <topic> \ # home/switches/button1
-M <message> \ # PRESSED
-m <mode> # publish

```

## Autoridad Certificadora

```bash
curl https://www.symantec.com/content/en/us/enterprise/verisign/roots/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem > root-CA.pem
```

## Node-Red

### Actualizar

```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/raspbian-deb-package/master/resources/update-nodejs-and-nodered)
```

### Iniciar el servicio

```bash
node-red-start
```

### Autoinicio del servicio

```bash
sudo systemctl enable nodered.service
```

### Bloques de configuración

* rpi gpio: Lectura de pines.
* switch: asignar un valor estático.
* change: definir un tipo de salida.
* debug: obtener salida en consola.
* mqtt: configurar conexión con AWS.
    * Punto de enlace.
    * Puerto.
    * Ceritificados.
    * Llaves.

### Node-red-dashboard

* Mostrado de texto.
* Mostrado de gráficas.

```
localhost:1880/ui
```
