
from PIL import Image

i = input("Введите номер изображения от 01 до 04: ")

if i == '01':
    image = Image.open('01.png')
    image.show()
elif i == '02':
    image = Image.open('02.png')
    image.show()
elif i == '03':
    image = Image.open('03.png')
    image.show()
elif i == '04':
    image = Image.open('04.png')
    image.show()