Emmy Kalaji (Section 82)
Jeffrey Leeburn (Section 81)
Allison Valdez (Section 82)
March 25, 2022

Module Information:
Module 8: Linear Feedback Shift Registers (Group Project).

Approach:
(Part 1: Building an LFSR)
Our group declared a LFSR class to organize and contain our methods. Within
the class, we initialized an __init__ method that declared the attributes and
behavior of our class object. Next, our bit function returned a specific bit
based off of a predetermined tap number (previously given in the assignment).
Our step function executes only one step of the LFSR iteration (as per the lab
guidelines) and utilizes the XOR operator to do so. Next, we utilized the
__str__ function to return the LFSR string obtained in the previous function.
Towards the end of the code, our group included a __main__ method to execute the
file as a script. Within our __main__ method, we provide the program with the
needed seeds as a list along with the tap number required. Lastly, we included a
for loop that iterated over the list of seeds, and performed the LFSR step
function which eventually printed our results.

(Part 2: Encrypting an Image)
Our group declared a ImageEncrypter class to organize and contain our methods.
As in Part 1, we created an __init__ method that initializes the state of the
ImageEncrypter object with a name and a file name. Next we declare a method
called open_image that will open our image file. The pixelate method returns the
previously opened image and converts it into a 2D array of RGB triples. The
encrypt method encrypts the previously obtained pixelated image and returns an
encrypted 2D array. The save_image method saves the encrypted 2D image into the
filename and format we specified. Lastly in our main method calls our
ImageEncrypter class and save_image method to convert the images to their
encrypted and decrypted forms.

Known Bugs:
No known bugs are in our code.

Partner Collaboration:
The partners for this group assignment were Emmy Kalaji (Section 82) and Jeffrey
Leeburn (Section 81) and Allison Valdez (Section 82). In the beginning, it
was initially Emmy and Allison in the group, and Jeffrey was a great addition
later on. Allison and Emmy provided the code's documentation, comments,
and troubleshooting. Allison also provided version control on Github. Both
Allison and Emmy wrote the initial LSFR class code (from Part 1), but Emmy's
version was ultimately used for the project's implementation. Jeffrey and Emmy
wrote the ImageEncrypter class code (for Part 2). Emmy's version of the code was
ultimately used and converted the proper syntax.