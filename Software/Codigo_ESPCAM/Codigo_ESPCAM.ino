#include "esp_camera.h"
#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "driver/rtc_io.h"
#include <WiFi.h>
#include <WiFiClient.h>
#include "ESP32_FTPClient.h"
#include <NTPClient.h>
#include <WiFiUdp.h>
#include "time.h"
#include "FS.h"
#include "SD_MMC.h"

char* ftp_server = "192.168.1.11";  // Dirección IP del servidor FTP
char* ftp_user = "hola";  // Nombre de usuario del servidor FTP
char* ftp_pass = "2181";  // Contraseña del servidor FTP
char* ftp_path = "/";  // Ruta en el servidor FTP

const char* WIFI_SSID = "******";  // Nombre de la red Wi-Fi
const char* WIFI_PASS = "*******";  // Contraseña de la red Wi-Fi

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", (-3600*5), 60000);// Cliente NTP para obtener la hora actual
ESP32_FTPClient ftp(ftp_server, ftp_user, ftp_pass, 6000, 2);// Cliente FTP para la conexión y transferencia de archivos

// Definición de pines para el modelo de cámara AI-THINKER
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27
#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22
#define SDMMC_FREQ_DEFAULT 20000000

camera_config_t config;

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0); // Deshabilitar detector de caídas de voltaje
  Serial.begin(115200);
  pinMode(3, OUTPUT);
  
  

  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.println("Conectando a WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Conectando a WiFi...");
  }

  Serial.println("Dirección IP:");
  Serial.println(WiFi.localIP());
  
  // Configuración de la cámara
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG; 
  if (psramFound()) { // Verificar si se encontró una memoria PSRAM
    config.frame_size = FRAMESIZE_UXGA; // Tamaño de fotograma: UXGA (1600x1200)
    config.jpeg_quality = 10; // Calidad de compresión JPEG: 10 
    config.fb_count = 2; // Contador de buffers de frame: 2 (mejor rendimiento)
  } else {
    config.frame_size = FRAMESIZE_XGA; // Tamaño de fotograma: XGA (1024x768)
    config.jpeg_quality = 12; // Calidad de compresión JPEG: 12 
    config.fb_count = 1; // Contador de buffers de frame: 1
  }


  // Inicialización de la tarjeta SD
  if (!SD_MMC.begin()) {
    Serial.println("Fallo al montar la tarjeta SD");
    return;
  }

  // Verificación del tipo de tarjeta SD
  uint8_t cardType = SD_MMC.cardType();// Obtener el tipo de tarjeta SD
  
  if (cardType == CARD_NONE) {
    Serial.println("No se ha detectado una tarjeta SD");
    return;
  }

  delay(1000); // Retardo de 1 segundo
  timeClient.begin(); // Inicializar el cliente NTP
  timeClient.update(); // Obtener la hora actual desde el servidor NTP
  delay(3000); // Retardo de 3 segundos
  Serial.println(timeClient.getFormattedTime()); // Imprimir la hora formateada obtenida del servidor NTP

   digitalWrite(3, HIGH);//Encendido de los leds antes de inicializar la camara para que se acostumbre a esta luz
  // Inicialización de la cámara
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Error al inicializar la cámara: 0x%x", err);
    return;
  }

  delay(10000);//tiempo de espera para que la cámara se ajuste a la luz proporcionada
  
  // Verificación de disponibilidad del servidor FTP y envío de imágenes
  if (ftpAvailable()) {
    ftp.OpenConnection();
    sendImagesToServerAndDelete();
  }

  takeAndSavePhoto();

  esp_deep_sleep(3*3600* 1000000);// Se despierta cada 3 horas para tomar captura 
}

void loop() {
  
}

void takeAndSavePhoto() {
  camera_fb_t* fb = NULL;

  // Capturar imagen con la cámara
  fb = esp_camera_fb_get();

  if (!fb) {
    Serial.println("Fallo al capturar la imagen de la cámara");
    delay(1000);
    ESP.restart();
  }

  // Obtener la fecha y hora actual
  unsigned long epochTime = timeClient.getEpochTime();
  struct tm* ptm = gmtime((time_t*)&epochTime);
  int year = ptm->tm_year + 1900;
  int month = ptm->tm_mon + 1;
  int day = ptm->tm_mday;
  int hour = ptm->tm_hour;
  int minute = ptm->tm_min;
  String dateTime;

  dateTime = String(day) + "_" + String(month) + "_" + String(year) + "_" + String(hour);

  String path = "/" + String(dateTime) + ".jpg";

  Serial.println("Subiendo " + path);

  // Guardar la imagen capturada en la tarjeta SD
  
  fs::FS& fs = SD_MMC;// Seleccionar el sistema de archivos (SD_MMC en este caso)
  Serial.printf("Nombre del archivo de imagen: %s\n", path.c_str());

  File file = fs.open(path.c_str(), FILE_WRITE);
  if (!file) {
    Serial.println("Error al abrir el archivo en modo de escritura");
  } else {
    file.write(fb->buf, fb->len);
    Serial.printf("Archivo guardado en la ruta: %s\n", path.c_str());
  }
  
  file.close(); // Cerrar el archivo
  esp_camera_fb_return(fb); // Liberar el búfer de frame de la cámara
  digitalWrite(3, LOW); //apagado de los leds
  
}

void sendImagesToServerAndDelete() {
  Serial.println("Enviando imágenes al servidor FTP y eliminándolas de la tarjeta SD:");
  
  File root = SD_MMC.open("/"); // Abrir la carpeta raíz en la tarjeta SD
  File file = root.openNextFile(); // Abrir el siguiente archivo en la carpeta raíz

  while (file) {
    if (!file.isDirectory()) {
      String filename = file.name();// Obtener el nombre del archivo
      Serial.println(filename);
      if (filename.endsWith(".jpg")) {// Verificar si el archivo es una imagen JPG
        Serial.println("Subiendo " + filename);
        ftp.InitFile("Type I");
        ftp.NewFile(filename.c_str());

        if (file.size() > 0) {
          uint8_t buf[256];
          size_t len;
          while ((len = file.read(buf, sizeof(buf))) > 0) {
            ftp.WriteData(buf, len);
          }
        }
        // Cerrar el archivo
        ftp.CloseFile();
        file.close();
        
        // Eliminar el archivo de la tarjeta SD
        SD_MMC.remove(filename.c_str());
      }
    }
    
    delay(4000);
    file = root.openNextFile();// Abrir el siguiente archivo en la carpeta raíz
  }

  root.close();
}

bool ftpAvailable() {
  Serial.println("Comprobando disponibilidad del servidor FTP...");
  WiFiClient client;
  
  if (client.connect(ftp_server, 21)) {
    Serial.println("El servidor FTP está disponible");
    client.stop();
    return true;
  } else {
    Serial.println("El servidor FTP no está disponible");
    return false;
  }
}
