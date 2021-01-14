from PIL import Image
from os import path


def process(image, width, height, save_path):
    output = image.resize((width, height))
    output.save(save_path)

def batch_process_square_image(image, save_folder, name):
    for x in {24, 32, 48, 64, 128, 256, 512, 1024}:
        process(image, x, x, path.join(save_folder, f"{name}@{x}.png"))

def batch_process_banner(image, save_folder, name):
    for x,y in {(4096,1024),(2048,512),(1024,256),(512,128),(256,64),(128,32)}:
        process(image, x, y, path.join(save_folder,f'{name}@{x}x{y}.png'))
    pass

if __name__ == "__main__":
    ico = Image.open('piculator-icon.png')
    batch_process_square_image(ico,'Generated','piculator-icon')
    banner_colorful = Image.open('piculator-banner-colorful.png')
    batch_process_banner(banner_colorful,'Generated','piculator-banner-colorful')
    banner_white = Image.open('piculator-banner-white.png')
    batch_process_banner(banner_white,'Generated','piculator-banner-white')
    banner_black = Image.open('piculator-banner-black.png')
    batch_process_banner(banner_black,'Generated','piculator-banner-black')