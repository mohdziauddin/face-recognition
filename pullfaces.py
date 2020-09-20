import face_recognition
from PIL import Image,ImageDraw


image_of_zia=face_recognition.load_image_file('irfan1.jpg')
zia_face_encoding=face_recognition.face_encodings(image_of_zia)[0]

image_of_rizwan=face_recognition.load_image_file('rizwan1.jpg')
rizwan_face_encoding=face_recognition.face_encodings(image_of_rizwan)[0]

#image_of_adnan=face_recognition.load_image_file('adnan.jpg')
#adnan_face_encoding=face_recognition.face_encodings(image_of_adnan)[0]

#create array of encodeing and names
known_face_encoding=[
        zia_face_encoding,
        rizwan_face_encoding
 #       adnan_face_encoding
        ]
known_face_names=[
        "zia@irfan ",
        "rizwan"
        #"adnan"
        ]
#load test image to find faces
test_image=face_recognition.load_image_file('group.jpg')

#find faces in test image
face_locations=face_recognition.face_locations(test_image)
face_encodings=face_recognition.face_encodings(test_image,face_locations)

#convert to pil format
pil_image=Image.fromarray(test_image)
#create a drw image instances

draw=ImageDraw.Draw(pil_image)
#loop through faces in test images
for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
    matches=face_recognition.compare_faces(known_face_encoding,face_encoding)


    name="unknown persons"

    #if match
    if True in matches:
        first_match_index= matches.index(True)
        name=known_face_names[first_match_index]


    #draw box
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0,0))

    #drw label

    text_width,text_height=draw.textsize(name)
    draw.rectangle(((left,bottom - text_height -10),(right,bottom)),fill=(0,0,0,0),outline=(0,0,0,0))
    draw.text((left+6,bottom - text_height -5),name,fill=(255,255,255,255))


del draw
#display\

pil_image.show()


