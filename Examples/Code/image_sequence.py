from image_to_ascii import ascii_image

images = [
    'Examples/Images/frame-00.png',
    'Examples/Images/frame-01.png',
    'Examples/Images/frame-02.png',
    'Examples/Images/frame-03.png',
    'Examples/Images/frame-04.png',
    'Examples/Images/frame-05.png',
    'Examples/Images/frame-06.png',
    'Examples/Images/frame-07.png',
    'Examples/Images/frame-08.png',
    'Examples/Images/frame-09.png',
]

for i in range(len(images)):
    images[i] = ascii_image(images[i], (256, 256))

while True:
    for image in images:
        image.display()

