import os
import cv2
import ReadFromPicture
import ScanPicture

def orderByLecture(lectures):

    ####################creating folders for lectures##################

    for l in lectures:
        l = l.lower()
        #print(l)

    path = os.getcwd()
    path = path + "/Lectures"

    try:
        os.mkdir(path)
    except OSError:
        print(OSError)
    else:
        print("folder created")

    for l in lectures:
        tmppath = path
        tmppath = tmppath + '/' + l

        try:
            os.mkdir(tmppath)
        except OSError:
            print(OSError)
        else:
            print("folder created")
    #########################end of creating folders for lectures####################

    #########################sorting lectures to folders############################
    lectureTexts = []

    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner1\Pictures"

    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Pictures/"
    p2 = "C:/Users/danilo/PycharmProjects/DocumentScanner1/Lectures/"
    picturesArray = []
    #for all pictures in folder with all pictures
    for p in os.listdir(picturesPath):
        #p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)
        text = ReadFromPicture.readFromPicture(dst)

        picturesArray.append(dst)
        lectureTexts.append(text.lower())

    for text in lectureTexts:
        maxNum = 0
        maxNumIndex = 0

        for l in lectures:
            numOfMatches = text.count(l)

            if(maxNum < numOfMatches):
                maxNum = numOfMatches
                maxNumIndex = lectures.index(l)

        cv2.imwrite(p2 + lectures[maxNumIndex] +"/img" + str(imgNameCounter) + ".jpg", picturesArray[lectureTexts.index(text)])
        imgNameCounter += 1
    #########################end ofsorting lectures to folders############################