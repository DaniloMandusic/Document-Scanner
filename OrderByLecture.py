import os
import cv2
import ReadFromPicture
import ScanPicture

def orderByLecture():

    ####################creating folders for lectures##################
    lectures = []

    while True:
        lecture = input("Name of lecture?")
        if(lecture == ""):
            break
        else:
            lectures.append(lecture)

    for l in lectures:
        print(l)

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

    outPath = "C:\Miniconda\envs\.."
    picturesPath = r"C:\Users\danilo\PycharmProjects\DocumentScanner\Pictures"

    # iterate through the names of contents of the folder
    # for image_path in os.listdir(path):
    #     # create the full input path and read the file
    #     input_path = os.path.join(path, image_path)
    #     image_to_rotate = ndimage.imread(input_path)
    #
    #     # rotate the image
    #     rotated = ndimage.rotate(image_to_rotate, 45)
    #
    #     # create full output path, 'example.jpg'
    #     # becomes 'rotate_example.jpg', save the file to disk
    #     fullpath = os.path.join(outPath, 'rotated_' + image_path)
    #     misc.imsave(fullpath, rotated)
    imgNameCounter = 0
    p1 = "C:/Users/danilo/PycharmProjects/DocumentScanner/Pictures/"
    p2 = "C:/Users/danilo/PycharmProjects/DocumentScanner/Lectures/"
    picturesArray = []
    #for all pictures in folder with all pictures
    for p in os.listdir(picturesPath):
        #p is name of picture
        input_path = p1 + p
        dst = ScanPicture.scanPicture(input_path)
        text = ReadFromPicture.readFromPicture(dst)

        picturesArray.append(dst)
        lectureTexts.append(text)

    for text in lectureTexts:
        maxNum = 0
        maxNumIndex = 0

        for l in lectures:
            numOfMatches = text.count(l)

            if(maxNum < numOfMatches):
                maxNum = numOfMatches
                maxNumIndex = lectures.index(l)

        print(p2 + lectures[maxNumIndex] +"/img" + str(imgNameCounter) + "," + str(lectureTexts.index(text)) + " goes into lecture " + lectures[maxNumIndex])
        # order pictures in right folders with appropriate names
        cv2.imshow("a",picturesArray[lectureTexts.index(text)])
        cv2.waitKey(0)

        testPath = "C:/Users/danilo/PycharmProjects/DocumentScanner/Lectures/45"
        cv2.imwrite(p2 + lectures[maxNumIndex] +"/img" + str(imgNameCounter) + ".jpg", picturesArray[lectureTexts.index(text)])
        imgNameCounter += 1
    #########################end ofsorting lectures to folders############################