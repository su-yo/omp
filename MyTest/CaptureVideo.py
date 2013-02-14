import cv2;
import cv2.cv as cv;
import numpy as np;

def InitVideo( MaxCameraIndex = 3 ):
    #
    #variables for 
    #camera devices
    #
    global CvCapture;
    global CameraIndex;
    global CameraFrame;
    
    CameraIndex = 0;
    CvCapture = cv.CaptureFromCAM( CameraIndex );

    #
    #try until
    #correct device is
    #not found
    #
    while CameraIndex < MaxCameraIndex :

        CameraFrame = cv.QueryFrame( CvCapture );

        if CameraFrame != None:
            return;
        else:
            #
            #check next index
            #if current index
            #doesnot capture frame
            #
            print("No VideoCapture device found at current index.");
            print("Current index: {}", CameraIndex );
            if CameraIndex < ( MaxCameraIndex - 1 ) :
                print("Trying next index...");
            CameraIndex += 1;
                
    print("Unable to access VideoCapture device");
    return;
