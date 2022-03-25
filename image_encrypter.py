from PIL import Image
from lfsr import LFSR  # import your LFSR class for use in ImageEncrypter


class ImageEncrypter:
    # initialize an ImageEncrypter object with an LFSR and image file name
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name

    # open the image specified by ‘file_name’ in your constructor
    # you will find the Image.open method useful here
    def open_image(self):
        return Image.open(self.file_name)

    # calls open_image()
    # converts the image to a 2D array of R, G, B triples
    # you will find the Image.load method useful here
    def pixelate(self):
        image = self.open_image()
        loaded_image = image.load()
        pixels = []
        for h in range(image.size[0]):
            for w in range(image.size[1]):
                # Populate list with the image pixel values
                pixels.append(loaded_image[w, h])
        return pixels

    # encrypts the 2D pixelated “image” returned from pixelate()
    # returns the encrypted 2D array
    # you will find the binary XOR operator useful here
    def encrypt(self):
        image_pixels = self.pixelate()
        encrypted_image_pixels = []
        for pixel in image_pixels:
            temp_pixel = []
            for color in pixel:
                self.lfsr.step()
                # Use string representation to get the lfsr value
                # Convert binary to integer using int base=2
                temp_pixel.append(color ^ int(self.lfsr.__str__(), base=2))

            encrypted_image_pixels.append(tuple(temp_pixel))

        return encrypted_image_pixels

    # converts the encrypted 2D pixelated image into an image
    # and names it <file_name>_transform.png
    # you will find the Image.save method useful here
    def save_image(self, file_name: str):
        encrypted_image_pixels = self.encrypt()
        image = Image.new('RGB', (225, 225))
        image.putdata(encrypted_image_pixels)
        image.save(f"{file_name}_transform.png")


# your executable code that invokes ImageEncrypter and encrypts/decrypts an # image and saves the result to a file
def main():
    image = ImageEncrypter(LFSR('10011010', 5), 'football.png')
    image.save_image('football')

    image = ImageEncrypter(LFSR('10011010', 5), 'football_transform.png')
    image.save_image('football_transform')


if __name__ == '__main__':
    main()
