# openCV_VehicleDetection
Vehicle Detection Project
This project implements a vehicle detection system using computer vision and machine learning techniques. The primary goal is to accurately identify and locate vehicles in images and video streams.

Features
Real-time Vehicle Detection: Detects cars, trucks, and other vehicles in real-time using a pre-trained deep learning model.
Video Stream Processing: Processes video streams from files or live feeds to identify and highlight vehicles.
Image Processing: Analyzes static images for vehicle detection.
Bounding Box Visualization: Draws bounding boxes around detected vehicles for clear visualization.
Customizable Parameters: Allows tuning of detection parameters to balance accuracy and performance.
Installation
Clone the repository:
sh
Copy code
git clone https://github.com/PrakXPoseidon/openCV_VehicleDetection.git
Navigate to the project directory:
sh
Copy code
cd openCV_VehicleDetection
Install the required dependencies:
sh
Copy code
pip install -r requirements.txt
Usage
Detecting Vehicles in an Image
Place your image in the images directory.
Run the detection script:
sh
Copy code
python detect_image.py --image images/your_image.jpg
Detecting Vehicles in a Video
Place your video file in the videos directory.
Run the detection script:
sh
Copy code
python detect_video.py --video videos/your_video.mp4
Live Video Stream Detection
Connect your webcam or use an IP camera.
Run the live detection script:
sh
Copy code
python detect_live.py
Models
The project uses a pre-trained model based on YOLO (You Only Look Once), which provides a good balance between speed and accuracy. The model can be downloaded from this link.

Configuration
You can adjust various parameters in the config.py file to fine-tune the detection process, such as confidence thresholds, non-maxima suppression settings, and more.

Results
The results of the detection are saved in the output directory, with bounding boxes drawn around detected vehicles in images and videos.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
YOLO: Real-Time Object Detection
OpenCV
