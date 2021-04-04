import cv2
import img2pdf as img2pdf
import numpy as np
import pytesseract as pytesseract
import pyttsx3
import mapper
import ScanPicture
import ReadFromPicture
import ConvertToPdf
import TextToVoice
import OrderByLecture
from tkinter import *
import subprocess
import os

#design for desktop app

#function that opens folder
def open_add_folder():
    subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner\\pictures"')

#function that processes pictures and opens folder with processed pictures
def process_pictures():
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
    p2 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Scanned Pictures/"
    picturesArray = []
    # for all pictures in folder with all pictures
    for p in os.listdir(picturesPath):
        # p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)

        cv2.imwrite(p2 + "/img" + str(imgNameCounter) + ".jpg",dst)
        imgNameCounter += 1

    subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner1\\scanned pictures"')

#function that exports all images to pdf files
def export_to_pdf():
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
    p2 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pdfs/"
    picturesArray = []
    # for all pictures in folder with all pictures
    for p in os.listdir(picturesPath):
        # p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)
        ConvertToPdf.convertToPdf(dst,imgNameCounter)
        #cv2.imwrite(p2 + "/img" + str(imgNameCounter) + ".jpg", dst)
        imgNameCounter += 1

    subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner1\\Pdfs"')

def read_from_pictures():
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
    p2 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pdfs/"
    picturesArray = []
    # for all pictures in folder with all pictures
    text = ""

    for p in os.listdir(picturesPath):
        # p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)
        text += ReadFromPicture.readFromPicture(dst)

    txtFile = open("Text From Images\\text.txt","w")
    txtFile.write(text)
    txtFile.close()

    subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner1\\Text From Images"')

#start of desktop design
app = Tk()

#part
# part_text = StringVar()
# part_label = Label(app, text = 'Part name', font = ('bold',14), pady = 20, padx = 20)
# part_label.grid(row = 0, column = 0)
# part_entry = Entry(app, textvariable = part_text)
# part_entry.grid(row = 0, column = 1)

#button for adding pictures for scanning
add_btn = Button(app, text='Add Part', border=0, command = open_add_folder)
img0 = PhotoImage(file="Button Pictures/button_add.png")
add_btn.config(image=img0)
add_btn.grid(row=0, column=0, pady=20)

#button for processing pictures
scan_btn = Button(app, text='Add Part', border=0, command = process_pictures)
img1 = PhotoImage(file="Button Pictures/button_process-pictures.png")
scan_btn.config(image=img1)
scan_btn.grid(row=0, column=1, pady=20)

#convert to pfd button
convert_btn = Button(app, text='Add Part', border=0, command = export_to_pdf)
img2 = PhotoImage(file="Button Pictures/button_convert-to-pdf.png")
convert_btn.config(image=img2)
convert_btn.grid(row=0, column=2, pady=20)

#read from pictures button
read_btn = Button(app, text='Add Part', border=0, command = read_from_pictures)
img3 = PhotoImage(file="Button Pictures/button_read-from-pictures.png")
read_btn.config(image=img3)
read_btn.grid(row=1, column=0, pady=20)

speech_btn = Button(app, text='Add Part', border=0)
img4 = PhotoImage(file="Button Pictures/button_text-to-speech.png")
speech_btn.config(image=img4)
speech_btn.grid(row=1, column=1, pady=20)

order_btn = Button(app, text='Add Part', border=0)
img5 = PhotoImage(file="Button Pictures/button_order-by-lectures.png")
order_btn.config(image=img5)
order_btn.grid(row=1, column=2, pady=20)

app.title('Document Scanner')
app.geometry("1000x300")

#start program
app.mainloop()


# dst = ScanPicture.scanPicture('C:/Users/danilo/PycharmProjects/DocumentScanner/Pictures/1.jpg')
# text = ReadFromPicture.readFromPicture(dst)
# #TextToVoice.textToVoice(text)
# #ConvertToPdf.convertToPdf(dst)
# OrderByLecture.orderByLecture()

#name your picture
# image = cv2.imread('1.jpg')
# image = cv2.resize(image, (1500, 880))
#
# # creating copy of original image
# orig = image.copy()
#
# # convert to gray and blur
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
# #detect edges
# edged = cv2.Canny(blurred, 0, 50)
# orig_edged = edged.copy()
#
# # find the contours in the edged image, keeping only the
# # largest ones, and initialize the screen contour
# (contours, _) = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)
#
# #x,y,w,h = cv2.boundingRect(contours[0])
# #cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),0)
#
# # get approximate contour
# for c in contours:
#     p = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * p, True)
#
#     if len(approx) == 4:
#         target = approx
#         break
#
#
# # mapping target points to 800x800 quadrilateral
# approx = mapper.mapp(target)
# pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])
#
# M = cv2.getPerspectiveTransform(approx,pts2)
# dst = cv2.warpPerspective(orig,M,(800,800))
#
# cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
# dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("dst.jpg", dst)
# cv2.waitKey(0)
#
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Python38\\Tesseract\\tesseract.exe'
#
# print(pytesseract.image_to_string(dst))
# cv2.imwrite('Test_dst.jpg', dst)
#
# string = pytesseract.image_to_string(dst)
#
# pdf = img2pdf.convert("Test_dst.jpg")
# file = open("newfile.pdf","wb")
# file.write(pdf)
# file.close()
#
# engine = pyttsx3.init()
# engine.say(string)
# engine.runAndWait()