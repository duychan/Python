#include <SoftwareSerial.h>
int gasValue = A0; // tín hiệu từ cảm biến
int IN3 = 5; // chân PWM
int IN4 = 4;
int rxPin = 0;                       //   xác định chân dữ liệu rx SoftwareSerial
int txPin = 1;                        // xác định chân dữ liệu tx của SoftwareSerial 
SoftwareSerial blueTooth(rxPin, txPin);  //tạo cong Serial moi ten bluetooth 
void setup()
{
    Serial.begin(9600); 
    blueTooth.begin(9600);      //đặt baudrate giao tiếp bluetooth
    pinMode(gasValue, INPUT); 
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
}
int mode = 0; // thiết lập chế độ + mức độ quay
void loop(){  
    if (blueTooth.available() > 0) {
        mode = blueTooth.read();
        blueTooth.write(gasValue); // hiển thị giá trị lên app
   }

    if(mode == 0){
        adjustSpeed(0, false);
   }

   if(mode == 1){
        adjustSpeed(50, false);
   }

   if(mode == 2){
        adjustSpeed(100, false);
   }

   if(mode == 255){
        adjustSpeed(50, true);
   }

   if(mode == 254){
        adjustSpeed(100, true);
   }

    delay(500);
}

// Hàm thay đổi tốc độ và chế độ quay
/*
    parameter:
    - percent: mức độ công xuất quạt quay ( % )
    - isReverse : chế độ quay ( cùng kim đồng hồ hoặc ngược lại )
*/
void adjustSpeed(int percent, bool isReverse){ 
  percent = constrain(percent, 0, 100); // thiết lập khoảng cho phép của mức độ %
  int val = map(percent, 0, 100, 0, 255); // chuyển giá trị % sang giá trị hợp lệ của analog 
  if(isReverse){
    digitalWrite(IN4, HIGH);
    analogWrite(IN3, 255 - val); // đổi chiều
  }
  else{
    digitalWrite(IN4, LOW);
    analogWrite(IN3, val);
  }
}

// Hàm dừng quạt
void stopFan(){
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}