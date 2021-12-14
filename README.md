Our Project has been split into five parts:
1. Taking a video as input.
2. Splitting the Video into frames.
3. Drawing a Box around the hand to eliminate the background.
4. Mapping the Hand gestures to the respective English Characters.
5. Translation from English text to Sign Language.

To execte the code:
I) Splitting video into frames and mapping the hand gestures: 
	1. Make sure you have the following packages installed:
		a. numpy
		b. keras
		c. tensorflow
		d. opencv-python
		e. torch
	2. The parts 1,2 and 4 have been combined into one part(Copy of final_predict.ipynb).
	3. Execute the above file (Copy of final_predict.ipynb) on Google colab taking demo_video as the input video.

II) Drawing a Box around the hand to eliminate the background:
	1. Take an image from the ISL dataset as input.
	2. Run the file haddetection.py on colab.

III) Translation from English text to Sign Language:
	1. Execute the file Copy of final_reverse.ipynb oon google colab.
