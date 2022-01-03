
#include <iostream>
#include<string>
using namespace std;
#include "BluetoothSerial.h"


#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {
  SerialBT.write('#');
  int num = rand() % 100;
  string str = to_string(num);
  for (int i = 0; i < str.length(); i++) {
    SerialBT.write(str[i]);
  }
  SerialBT.write('#');
  SerialBT.write('\n');
  delay(20);
}
