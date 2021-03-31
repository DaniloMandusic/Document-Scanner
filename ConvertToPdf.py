import cv2
import img2pdf as img2pdf
import numpy as np
import mapper
import pytesseract

def convertToPdf(dst):
    cv2.imwrite('Pictures/Test_dst.jpg', dst)

    pdf = img2pdf.convert("Test_dst.jpg")
    file = open("newfile.pdf","wb")
    file.write(pdf)
    file.close()