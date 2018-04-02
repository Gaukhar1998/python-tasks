import cv2
import numpy as np
import operator
import os
from PIL import Image
import pytesseract
    
MIN_CONTOUR_AREA = 100
RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_HEIGHT = 30

class ContourWithData():
    npaContour,boundingRect = None, None         
    intRectX,intRectY,intRectWidth,intRectHeight,fltArea = 0,0,0,0,0.0         

    def calculateRectTopLeftPointAndWidthAndHeight(self):               
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight

    def checkIfContourIsValid(self):                            
        if self.fltArea < MIN_CONTOUR_AREA: return False
        return True

def main():
    allContoursWithData = []                
    validContoursWithData = []              

    try:
        npaClassifications = np.loadtxt("classifications.txt", np.float32)                  
    except:
        print ("error, unable to open classifications.txt, exiting program\n")
        os.system("pause")
        return

    try:
        npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)                 
    except:
        print ("error, unable to open flattened_images.txt, exiting program\n")
        os.system("pause")
        return

    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))       
    kNearest = cv2.ml.KNearest_create()                   
    kNearest.train(npaFlattenedImages, cv2.ml.ROW_SAMPLE, npaClassifications)

    src_path = 'C:/Users/hp/Desktop/OpenCV_3_KNN_Character_Recognition_Python-master/'
    image = 'words2.jpg'
    
    def get_string(img_path):
        img = cv2.imread(img_path,0)
        kernel = np.ones((1,1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
    
        cv2.imwrite(src_path+"without_noise.jpg", img)
        result = src_path + "without_noise.jpg"
        return result

    
    tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
    TESSDATA_PREFIX= 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata'
    tessdata_dir_config = 'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata\\configs'
    hey = get_string(src_path+image)
    print(pytesseract.image_to_string(Image.open(image), lang='eng', config=tessdata_dir_config))
    print(src_path+image)
    #print(words)
    imgTestingNumbers = cv2.imread(image) 
    #cv2.imshow("image",imgTestingNumbers)
    #cv2.waitkey(0)
    if imgTestingNumbers is None:                           
        print ("error: image not read from file \n\n")   
        os.system("pause")                                 
        return                                              

    imgGray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)      
    imgBlurred = cv2.GaussianBlur(imgGray, (5,5), 0)                    
    imgThresh = cv2.adaptiveThreshold(imgBlurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)                                   
    imgThreshCopy = imgThresh.copy()        
    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                 cv2.RETR_EXTERNAL,         
                                                 cv2.CHAIN_APPROX_SIMPLE)   

    for npaContour in npaContours:                             
        contourWithData = ContourWithData()                                            
        contourWithData.npaContour = npaContour                                         
        contourWithData.boundingRect = cv2.boundingRect(contourWithData.npaContour)     
        contourWithData.calculateRectTopLeftPointAndWidthAndHeight()                    
        contourWithData.fltArea = cv2.contourArea(contourWithData.npaContour)           
        allContoursWithData.append(contourWithData)                                     

    for contourWithData in allContoursWithData:                 
        if contourWithData.checkIfContourIsValid():             
            validContoursWithData.append(contourWithData)      
        

    validContoursWithData.sort(key = operator.attrgetter("intRectX"))         # sort contours from left to right

    strFinalString = ""         
    for contourWithData in validContoursWithData:            
                                                
        cv2.rectangle(imgTestingNumbers,                                       
                      (contourWithData.intRectX, contourWithData.intRectY),     
                      (contourWithData.intRectX + contourWithData.intRectWidth, contourWithData.intRectY + contourWithData.intRectHeight),      
                      (255, 0, 0),1)                        

        imgROI = imgThresh[contourWithData.intRectY : contourWithData.intRectY + contourWithData.intRectHeight,     
                           contourWithData.intRectX : contourWithData.intRectX + contourWithData.intRectWidth]

        imgROIResized = cv2.resize(imgROI, (RESIZED_IMAGE_WIDTH, RESIZED_IMAGE_HEIGHT))             
        npaROIResized = imgROIResized.reshape((1, RESIZED_IMAGE_WIDTH * RESIZED_IMAGE_HEIGHT))      
        npaROIResized = np.float32(npaROIResized)       
        retval, npaResults, neigh_resp, dists = kNearest.findNearest(npaROIResized, k = 3)     

        strCurrentChar = str(chr(int(npaResults[0][0])))                                             

        strFinalString = strFinalString + strCurrentChar            

    #print ("\n" + strFinalString + "\n")            

    #cv2.imshow("imgTestingNumbers", imgTestingNumbers)      
    #cv2.waitKey(0)                                          

    #cv2.destroyAllWindows()             

    return

if __name__ == "__main__":
    main()