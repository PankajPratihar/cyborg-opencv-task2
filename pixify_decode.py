import numpy as np
import cv2
import os
import sys
import time
import random

'''
Guidelines :- 1) You are not allowed to import libraries other than those already mentioned
              2) You are allowed to code only in the function given below . Code present anywhere else would be ignored by the code verifying exec.
              3) You must code in such a way that the code inside the function is robust for all test cases.
              4) The code verifying exectubale would iterate over the test cases and call this function with one test image at a time. 
'''

def decode(image):
    '''
    Description:- This function takes in image as the input (a numpy array) and returns the character embedded in the image
    For example : if yellow squares = 4 , red squares = 3 , number of shapes containing shapes = 5 . Then the correct character to be returned would be (4*2 + 3*1 + 5) which is p. 
    Note :- if the value comes out to be 32 then the function should return an empty single space " ".
    '''
      # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define color ranges in HSV
    yellow_lower = np.array([30, 200, 200])
    yellow_upper = np.array([30, 255, 255])
    lower_red = np.array([0,200, 20])
    upper_red = np.array([10, 255, 255])

   

    # Create masks for each color
    yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    red_mask1 = cv2.inRange(hsv_image, lower_red, upper_red)

    # Find contours for each mask
    contours_yellow, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_red, _ = cv2.findContours(red_mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    red=len(contours_red)
    yellow=len(contours_yellow)

    img=image[85:620,80:620,:]
    img[np.all(img == 0, axis=2)] = 255

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,b_th=cv2.threshold(gray,30,255,cv2.THRESH_BINARY)
    ret,r_b_th=cv2.threshold(gray,80,255,cv2.THRESH_BINARY)
    ret,r_b_sh_th=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    ret,r_b_sh_y_th=cv2.threshold(gray,250,255,cv2.THRESH_BINARY)

    # #red_box
    # red=b_th-r_b_th
    # red_contour,h=cv2.findContours(red,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    # n_red=0
    # for i in range(len(red_contour)):
    #     a=int(cv2.contourArea(red_contour[i])/100)
    #     n_red+=a

    # #yellow box
    # yellow=r_b_sh_th-r_b_sh_y_th
    # yellow_contour,h=cv2.findContours(yellow,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    # n_yellow=0
    # for i in range(len(yellow_contour)):
    #     a=int(cv2.contourArea(yellow_contour[i])/100)
    #     n_yellow+=a
 

    #shapes
    shape=r_b_th-r_b_sh_th
    kernel=np.array(np.ones((int(535/5),int(540/5))))
    stride = (int(535/5),int(540/5))
    n_shape=0
    for y in range(0, 535, stride[0]):
        for x in range(0,540 , stride[1]):
            patch = shape[y:y + kernel.shape[0], x:x + kernel.shape[1]]
            result = np.sum(patch * kernel)
            if result!=0:
                n_shape+=1
  
       

    ############ Enter your Code Here #################
    # character_no = contours_red + 2*contours_yellow + n_shape
    # if 1 <= character_no <= 26:
    #     character = chr(96 + character_no)
    # else: 
    #     character=chr(character_no)
 

    
    

    ############ Enter your Code Here #################
    character = " "
    character_no = red + 2*yellow + n_shape
    alphabat="abcdefghijklmnopqrstuvwxyz"
    # if character_no==32:
    #     return ''
    # if character_no>=1 and character_no<=26:
    #     return alphabat[character_no-1]
    if 1 <= character_no <= 26:
      character = alphabat[character_no - 1]
    else:
      character = " "
    ###################################################
    return character

    