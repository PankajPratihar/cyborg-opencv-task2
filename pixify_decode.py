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
     
    


  
    square=0
    for i in range(100,700,100):
        for j in range(100,700,100):
           
            if i==600 or j==600:
                continue
            img=image[i+10:i+90,j+10:j+90]
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            _, threshold=cv2.threshold(gray,179,255,cv2.THRESH_BINARY_INV)
            compare=np.full([80,80],0,dtype=np.uint8)
            if not (compare==threshold).all():
              square+=1
  

 
  
       

    ############ Enter your Code Here #################
    character=" "
    character_no = red + 2*yellow + square
    if 1 <= character_no <= 26:
        character = chr(96 + character_no)
    else: 
        character=chr(character_no)
 

    
    


    ###################################################
    return character

    