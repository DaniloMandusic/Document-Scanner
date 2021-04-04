import cv2
import img2pdf as img2pdf
import numpy as np
import mapper
import pytesseract

def convertToPdf(dst, imgCounter):
    cv2.imwrite('PicturesTmp/Test_dst.jpg', dst)

    pdf = img2pdf.convert("PicturesTmp/Test_dst.jpg")
    file = open("Pdfs\\img" + str(imgCounter) + ".pdf","wb")
    file.write(pdf)
    file.close()