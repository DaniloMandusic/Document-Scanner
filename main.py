import cv2
import ScanPicture
import ReadFromPicture
import ConvertToPdf
import TextToVoice
import OrderByLecture
from tkinter import *
from tkinter import messagebox
import subprocess
import os

#function that opens folder
def open_add_folder():
    subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner1\\pictures"')

#function that processes pictures and opens folder with processed pictures
def process_pictures():
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
    p2 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Scanned Pictures/"
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
    # for all pictures in folder with all pictures
    for p in os.listdir(picturesPath):
        # p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)
        ConvertToPdf.convertToPdf(dst,imgNameCounter)
        #cv2.imwrite(p2 + "/img" + str(imgNameCounter) + ".jpg", dst)
        imgNameCounter += 1

    subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner1\\Pdfs"')

#function that read all files from pictures and put them in one text document
def read_from_pictures():
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
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

#text to speech function for button
def text_to_speech():
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
    # for all pictures in folder with all pictures
    text = ""

    for p in os.listdir(picturesPath):
        # p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)
        text += ReadFromPicture.readFromPicture(dst)

    TextToVoice.textToVoice(text)

#start of desktop design
app = Tk()

#function for order by lecture button
def order_by_lecture():
    newWindow = Toplevel(app)

    lectures_array = []

    def populate_list():
        lectures_list.delete(0, END)
        for lecture in lectures_array:
            lectures_list.insert(END, lecture)

    def add_item():
        if price_text.get() == '':
            messagebox.showerror('Required Fields', 'Please include all fields')
            return
        lectures_array.append(price_text.get())
        lectures_list.insert(END, price_text.get())

        lectures_entry.delete(0,END)

    def remove_item():
        lectures_array.remove(price_text.get())
        lectures_entry.delete(0,END)
        populate_list()

    def order():
        OrderByLecture.orderByLecture(lectures_array)
        subprocess.Popen('explorer "C:\\Users\\danilo\\pycharmprojects\\documentscanner1\\Lectures"')

    # sets the title of the
    # Toplevel widget
    newWindow.title("Order by lectures")

    # sets the geometry of toplevel
    newWindow.geometry("350x320")

    price_text = StringVar()
    #first entry
    lectures_entry = Entry(newWindow, textvariable = price_text)
    lectures_entry.grid(row = 0, column = 0, pady = 20, padx = 20)
    #add button
    add_btn = Button(newWindow, text='Add lecture', command = add_item)
    add_btn.grid(row=1, column=0, pady=20)
    #remove button
    remove_btn = Button(newWindow, text='Remove lecture', command = remove_item)
    remove_btn.grid(row=1, column=1, pady=20)
    #process button
    process_btn = Button(newWindow, text='Proceed', command = order)
    process_btn.grid(row=0, column=1, pady=20)
    #lectures_list
    lectures_list = Listbox(newWindow, height = 8, width = 50)
    lectures_list.grid(row = 2, column = 0, columnspan = 3, rowspan = 6, pady = 20, padx = 20)
    scrollbar = Scrollbar(newWindow)
    scrollbar.grid(row=2, column=3)
    # Set scroll to listbox
    lectures_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=lectures_list.yview)

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

#text to speech button
speech_btn = Button(app, text='Add Part', border=0, command = text_to_speech)
img4 = PhotoImage(file="Button Pictures/button_text-to-speech.png")
speech_btn.config(image=img4)
speech_btn.grid(row=1, column=1, pady=20)

order_btn = Button(app, text='Add Part', border=0, command = order_by_lecture)
img5 = PhotoImage(file="Button Pictures/button_order-by-lectures.png")
order_btn.config(image=img5)
order_btn.grid(row=1, column=2, pady=20)

app.title('Document Scanner')
app.geometry("1000x300")

#start program
app.mainloop()