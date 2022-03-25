"""
Import the LFSR class and Pillow code for use in ImageEncrypter
"""
from PIL import Image
from lfsr import LFSR


class ImageEncrypter:
    """
    This class is in charge of organizing and creating the functions
    necessary for our LFSR project to run.
    """

    def __init__(self, lfsr: LFSR, file_name: str):
        """
        This function initializes the state of the an ImageEncrypter
        object with the LFSR name (as its name) and proper image filename.

        :param lfsr: The variable name given
        :param file_name: The image file name
        """
        self.lfsr = lfsr
        self.file_name = file_name

    def open_image(self):
        """
        This function is in charge of opening the image (dictated by the
        filename).

        :return: The image retreived by the function call
        """
        return Image.open(self.file_name)

    def pixelate(self):
        """
        This function executes open_image() converts the image to a 2D array
        of R, G, B triples you will find the Image.load method useful here

        :return:
        """
        image = self.open_image()
        loaded_image = image.load()
        pixels = []
        for h in range(image.size[0]):
            for w in range(image.size[1]):
                # Populate list with the image pixel values
                pixels.append(loaded_image[w, h])
        return pixels

    def encrypt(self):
        """
        encrypts the 2D pixelated “image” returned from pixelate() returns
        the encrypted 2D array you will find the binary XOR operator useful here

        :return:
        """
        image_pixels = self.pixelate()
        encrypted_image_pixels = []
        for pixel in image_pixels:
            temp_pixel = []
            for color in pixel:
                self.lfsr.step()
                """
                Use string representation to get the lfsr value Convert 
                binary to integer using int base=2
                """
                temp_pixel.append(color ^ int(self.lfsr.__str__(), base=2))
            encrypted_image_pixels.append(tuple(temp_pixel))
        return encrypted_image_pixels

    def save_image(self, file_name: str):
        """
        # converts the encrypted 2D pixelated image into an image and names
        it <file_name>_transform.png you will find the Image.save method
        useful here

        :param file_name:
        :return:
        """
        encrypted_image_pixels = self.encrypt()
        image = Image.new('RGB', (225, 225))
        image.putdata(encrypted_image_pixels)
        image.save(f"{file_name}_transform.png")


def main():
    """
    your executable code that invokes ImageEncrypter and encrypts/decrypts an
    image and saves the result to a file

    :return:
    """
    image = ImageEncrypter(LFSR('10011010', 5), 'football.png')
    image.save_image('football')

    image = ImageEncrypter(LFSR('10011010', 5), 'football_transform.png')
    image.save_image('football_transform')


if __name__ == '__main__':
    main()
