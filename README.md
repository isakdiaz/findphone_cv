# findphone_opencv

The goal is to return the normalized coordinates of the phone on the floor in various different types of settings. The images folder contains a labels.txt file which has the image names and the coordinates where the phone is found. 

The terminal command is:

$ python find_phone.py ~/find_phone_test_images/51.jpg 

0.2551 0.3129

and it returns the normalized coordinates rounded to 4 significant digits. 

Current Implementation produces 96.12% accuracy on the training dataset using a simple cv2.findContours implementation. This is assuming that <5% radius deviation from ground truth is a correct result.

Below is a sample of the results:


![alt text](https://raw.githubusercontent.com/isakdiaz/findphone_cv/master/sample.jpg)
