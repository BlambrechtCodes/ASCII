# Welcome To ASCII

This Program uses the OpenCV library (`cv2`) to capture video from a camera and display it as ASCII art in the console. Here's a breakdown of the key components:

1. **Imports**: The code imports the `cv2` library for computer vision and the `os` library for operating system-related functions.

2. **Settings**: The `SHOW_REAL_VIDEO` variable is a boolean flag that, when set to `True`, displays the real camera video in a side panel. When set to `False`, only the ASCII art representation is displayed in the console.

3. **Function Definitions**:
   - `convert_row_to_ascii(row)`: Converts a row of grayscale pixel values to ASCII characters.
   - `convert_to_ascii(input_grays)`: Converts a 2D array of grayscale pixel values to ASCII characters using the `convert_row_to_ascii` function.
   - `print_array(input_ascii_array)`: Clears the console and prints the ASCII representation of a 2D array of ASCII characters.

4. **Main Loop**:
   - Initializes a video capture object (`cap`) using `cv2.VideoCapture(0)` to capture video from the default camera (index `0`).
   - Enters a `while` loop that continues until the user presses the 'q' key.
   - Gets the screen size for reducing the video resolution.
   - Reads a frame from the camera (`cap.read()`) and converts it to grayscale using `cv2.cvtColor`.
   - Resizes the grayscale frame to match the screen resolution using `cv2.resize`.
   - Converts the resized frame to ASCII art using `convert_to_ascii` and prints it using `print_array`.
   - Optionally, displays the real video frame if `SHOW_REAL_VIDEO` is `True`.
   - Releases the video capture object (`cap.release()`) and closes all OpenCV windows (`cv2.destroyAllWindows()`) when the program is terminated.

Overall, the program continuously captures video from the camera, converts it to ASCII art, and displays it in the console or in a side panel, depending on the `SHOW_REAL_VIDEO` setting.
