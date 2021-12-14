
#include <iostream>
#include<string>
using namespace std;
#include "BluetoothSerial.h"
#include <time.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
}
clock_t tStart = clock();
void loop() {
  int num = rand() % 100;
  string str = to_string(num);
  for (int i = 0; i < str.length(); i++) {
    SerialBT.write(str[i]);
  }
  SerialBT.write('#');

  string str1 = to_string((clock() - tStart)); //divide by 100 in python
  for (int i = 0; i < str1.length(); i++) {
    SerialBT.write(str1[i]);
  }
  SerialBT.write('#');
  SerialBT.write('\n');
  Serial.println("The device started, now you can pair it with bluetooth!");
  delay(20);
}
