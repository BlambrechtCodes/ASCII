# Imports
import cv2
import os

# Settings
SHOW_REAL_VIDEO = False   # Set this to True to get real camera video from cv2 in a side panel

def convert_row_to_ascii(row):
    """
    Convert a row of grayscale pixel values to ASCII characters.

    Args:
    - row: Tuple of integers representing grayscale pixel values.

    Returns:
    - Tuple of characters representing ASCII characters corresponding to the grayscale values.
    """
    ORDER = (' ', '.', "'", ',', ':', ';', 'c', 'l',
             'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N')
    return tuple(ORDER[int(x / (255 / 16))] for x in row)[::-1]


def convert_to_ascii(input_grays):
    """
    Convert a 2D array of grayscale pixel values to ASCII characters.

    Args:
    - input_grays: 2D array of integers representing grayscale pixel values.

    Returns:
    - Tuple of tuples representing ASCII characters corresponding to the grayscale values.
    """
    return tuple(convert_row_to_ascii(row) for row in input_grays)


def print_array(input_ascii_array):
    """
    Clear the console and print the ASCII representation of an array.

    Args:
    - input_ascii_array: 2D array of ASCII characters to be printed.
    """
    os.system("clear")
    print('\n'.join((''.join(row) for row in input_ascii_array)), end='')


cap = cv2.VideoCapture(0)

while(cv2.waitKey(1) & 0xFF != ord('q')):
    
    # Get screensize for reduction
    screen_height, screen_width = os.popen('stty size', 'r').read().split()

    # Get and Read in image data
    ret, frame = cap.read()

    # Convert data to grayscale using cv2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reduce grayscale array to proper resolution
    reduced = cv2.resize(gray, (int(screen_width), int(screen_height)))

    # Plug in reduced resolution numpy array for ascii converter func
    converted = convert_to_ascii(reduced)
    print_array(converted)

    # Display the resulting frame
    if SHOW_REAL_VIDEO:
        cv2.imshow('frame', reduced)

# When the program is terminated, release the capture on cap
cap.release()
cv2.destroyAllWindows()