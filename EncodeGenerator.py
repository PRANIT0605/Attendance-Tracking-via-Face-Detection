from dotenv import load_dotenv
import cv2
import pickle
import face_recognition
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
cred = credentials.Certificate("serviceAccountKey.json")

load_dotenv("sensitive.env")  # This loads the .env file into environment variables
database_url = os.getenv("DATABASE_URL")
storage_bucket_url = os.getenv("STORAGE_BUCKET_URL")

# Importing Student Images
folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentID = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentID.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(studentID)
# print(path)
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithID = [encodeListKnown, studentID]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithID, file)
file.close()
