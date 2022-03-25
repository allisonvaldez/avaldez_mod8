"""
Import the LFSR class and Pillow code for use in ImageEncrypter, and any
other dependencies necessary.
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
        This function initializes the state of the an Image_Encrypter's object
        with LFSR as it's name, and an image filename.

        :param lfsr: The variable name given
        :param file_name: The image's file name
        """
        self.lfsr = lfsr
        self.file_name = file_name

    def open_image(self):
        """
        This function is in charge of opening the image (dictated by the
        filename).

        :return: The image retrieved by the function call
        """
        return Image.open(self.file_name)

    def pixelate(self):
        """
        This function executes the open_image function and converts the image
        into a 2D array of RGB triples.

        :return: Converted image that utilizes RGB triples
        """
        image = self.open_image()
        loaded_image = image.load()
        pixels = []
        for h in range(image.size[0]):
            for w in range(image.size[1]):

                # Appends to the list the image pixel value
                pixels.append(loaded_image[w, h])
        return pixels

    def encrypt(self):
        """
        This function is in charge of encrypting the returned pixelated image
        from the prior function, and will return an encrypted 2D array.

        :return: An encrypted 2D array
        """

        image_pixels = self.pixelate()
        encrypted_image_pixels = []
        for pixel in image_pixels:
            temp_pixel = []
            for color in pixel:
                self.lfsr.step()
                """
                Used string representation to get the LFSR value, 
                and converted from binary to integer (using int base=2)
                """
                temp_pixel.append(color ^ int(self.lfsr.__str__(), base=2))
            encrypted_image_pixels.append(tuple(temp_pixel))
        return encrypted_image_pixels

    def save_image(self, file_name: str):
        """
        This function converts the encrypted pixelated 2D image back into an
        image and names it <file_name>_transform.png.

        :param file_name:
        :return:
        """

        encrypted_image_pixels = self.encrypt()
        image = Image.new('RGB', (225, 225))
        image.putdata(encrypted_image_pixels)
        image.save(f"{file_name}_transform.png")


def main():
    """
    Required code to execute program as a script. It will invoke the
    ImageEncrypter class, encrypt (or decrypt) an image, and saves the output
    to a file.

    :return: The output of the function
    """

    image = ImageEncrypter(LFSR('10011010', 5), 'football.png')
    image.save_image('football')

    image = ImageEncrypter(LFSR('10011010', 5), 'football_transform.png')
    image.save_image('football_transform')


if __name__ == '__main__':
    main()
