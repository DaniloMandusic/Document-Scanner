import cv2
import img2pdf as img2pdf
import numpy as np
import mapper
import pytesseract

def readFromPicture(dst):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Python38\\Tesseract\\tesseract.exe'

    print(pytesseract.image_to_string(dst))
    return pytesseract.image_to_string(dst)
    #cv2.imwrite('Test_dst.jpg', dst)

    #string = pytesseract.image_to_string(dst)