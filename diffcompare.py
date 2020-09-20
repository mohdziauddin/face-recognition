import face_recognition
from PIL import Image
#img=Image.open('noman.jpg')
#img.show()

'''image=face_recognition.load_image_file('noman.jpg')
face_location=face_recognition.face_locations(image)
print(face_location)
length=len(face_location)
print(length)'''

image_of_zia=face_recognition.load_image_file('zia.jpg')
zia_face_encoding=face_recognition.face_encodings(image_of_zia)[0]

noman_image=face_recognition.load_image_file('rizwan.jpg')
noman_face_encoding=face_recognition.face_encodings(noman_image)[0]

result=face_recognition.compare_faces([zia_face_encoding],noman_face_encoding)

if result[0]:
    print("both are same images")
else :
    print("not same images")

