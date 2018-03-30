# findphone_opencv

1) train_phone_finder.py ​ takes a single command line argument which is a path to a
folder with labeled images and ​ labels.txt​ ​ that has been attached to this
description. This script may generate any artifacts you want in the current folder.
Here is what a terminal command will look like:
> python train_phone_finder.py ~/find_phone 

2) find_phone.py ​ takes a single command line argument which is a path to the jpeg
image to be tested. This script may use data in the local folder previously
generated by ​ train_phone_finder.py ​ . ​ ​ This script has to print the normalized
coordinates of the phone detected on this test image in the format shown below.
Here is what a terminal command will look like. Please, notice space separated
float numbers on a single line without parentheses (!):
> python find_phone.py ~/find_phone_test_images/51.jpg 
0.2551 0.3129 
