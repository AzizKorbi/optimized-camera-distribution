# optimized-camera-distribution

This project focuses on developing an advanced algorithm for determining the best camera placements on architectural plans to ensure optimal coverage. The system is designed to analyze architectural plans, simulate camera coverage, and visualize camera placements.

## Table of Contents


- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)


## Features

- **Architectural Plan Analysis:** Analyze architectural plans to identify key areas and obstructions.
- **Camera Placement Algorithm:** Calculate the optimal placement for cameras to ensure maximum coverage.
- **Image Processing:** Use computer vision techniques to detect key areas such as doors, windows, and obstructions.
- **Coverage Simulation:** Simulate and validate the coverage area of each camera.
- **Visualization:** Visualize the camera placements and their fields of view on the architectural plan.


## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Virtual Environment
- Git

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AzizKorbi/optimized-camera-distribution.git
   cd optimized-camera-distribution



## Usage
### Upload Architectural Plans:

Start the Flask application.
Navigate to the homepage and upload an architectural plan (in PNG format).
### Image Processing:

The system processes the uploaded image, detecting key areas and obstructions.
### Camera Placement:

Enter the number of cameras and their characteristics.
The system calculates the optimal placement for the cameras and visualizes the coverage.

### Technology Stack
Backend: Python, Flask
Computer Vision: OpenCV, NumPy, YOLO 
Visualization: Matplotlib
Tools: CAD software, GIS tools
