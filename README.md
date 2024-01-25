# 3-Dimensions-object-manipulation-

#Prototype01
![01](https://github.com/Mullah-Abdul-Khadeer/3-Dimensions-object-manipulation-/assets/134354820/7b097f65-8151-42b1-8ec1-d3a800bd08c1)
Fig:01

![02](https://github.com/Mullah-Abdul-Khadeer/3-Dimensions-object-manipulation-/assets/134354820/9b8893b3-9a5d-40bc-87b8-be394990632a)
Fig:02

![03](https://github.com/Mullah-Abdul-Khadeer/3-Dimensions-object-manipulation-/assets/134354820/44bc9f27-a261-45da-a5d1-134a1f95e4b1)
Fig:03 

https://github.com/Mullah-Abdul-Khadeer/3-Dimensions-object-manipulation-/assets/134354820/df38e85c-cdfa-42d1-a9e7-5d5610bc404d
Testing :01

https://github.com/Mullah-Abdul-Khadeer/3-Dimensions-object-manipulation-/assets/134354820/05eee34c-ca20-474f-ab4b-929192a6a9eb
Testing :02

* Hand model taken from Inmoov open source repository
  Final goal :
       The main objective is to get data for training ML models to replicate realistic hand movements .
  i) Using the opencv package we are able to track and visualize the vectors and joints in the hand
  ii) And using micro controler we are able to replicate the movement
  iii) The joint movement data is recorded and simplified to two units "0" and "1" . Which will denote which finger are open at any instance of time .
       but due to processing capability restriction we are able to get the time stamps down to 1-2 sec. And the data is recorded in the form of an array
       ex: [1,1,1,1,1] - this would denote all fingers are closed  , [0,0,0,0,0] this would denote an open hand .
  iv) The final time stamped data is directly recorded into excel file thorugh serial port connection from the arduino .
  v) This data is to be used for further training ML models
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
