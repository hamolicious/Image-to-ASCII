from cv2 import imread
from os import system

def map_to_range(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

class CharacterSets:
    basic = ' .-:=+*#%@'
    black_and_white = ' #'
    black_grey_and_white = ' +#'
    full = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`. '

class ascii_image:
    def __init__(self, image_dir, image_size, **kwargs):
        self.screen_width, self.screen_height = kwargs.get('screen_size', (90, 40))
        self.image_width, self.image_height = self.image_size = image_size

        self.sample_x, self.sample_y = (self.image_width / self.screen_width, self.image_height / self.screen_height)

        self.image = self.load_image(image_dir)
        self.character_set = kwargs.get('charset', CharacterSets.basic)
        self.reverse_charset = kwargs.get('reverse_charset', False)

        self.precompute()

    def load_image(self, image_dir):
        if not type(image_dir) is str : raise TypeError('Directory must be a string')

        image = imread(image_dir)
        if image is None : raise TypeError('Something went wrong')
    
        return image

    def pixel_to_rgb(self, x, y):
        return [self.image[int(y), int(x), i] for i in range(3)]

    def character_from_rgb(self, colour):
        val = sum(colour)/3
        index = map_to_range(val, 0, 255, 0, len(self.character_set)-1)

        charset = self.character_set if not self.reverse_charset else self.character_set[::-1]
        return self.character_set[int(index)]

    def precompute(self):
        self.text_image = ''

        for y in range(self.screen_height):
            for x in range(self.screen_width):
                colour = self.pixel_to_rgb(x * self.sample_x, y * self.sample_y)
                self.text_image += self.character_from_rgb(colour)

            self.text_image += '\n'

    def display(self):
        system('cls')
        print(self.text_image)


















