Optional Flow 

""" Optical flow is the pattern of apparent motion of image objects between two consecutive frames caused
 by the movement of object or camera."""

"""" Optical Flow analysis has a few assumptions:

- The pixel intensities of an object do not changes between consecutive frames.
- Neighbouring pixels have similar motion."""

""" The optical flow methods in OpenCv will first take in a given set of points and a frame.
Then it well attempt to find those points in the next frame.

it is up to the user to supply the points yo track."""

""" The Lucas-Kanade computes optical flow for a sparse feature set.
- Meaning only the points it was told to track.

But what idf we wanted to track all the points in a video ?"""

""" We can use gunner farneback's algorithm (also built in to openCV) to calculate 
flow for all points in an image.
it will color them black if no flow (no movement) is detected."""

""" The Lucause-Kanade computes optical flow for a sparse feature set.
- Meaning only the points it was told to track.

Bt what if we wanted to track all the points in a video?"""

""" We can use Gunner Franeback's algorithm (also built in to OpenCV) to calculate flow
for all points in an image.

it will color them black if no flow (no movement) is detected."""