# LBPH Face Recognition System

A custom implementation of the Local Binary Patterns Histograms (LBPH) Face Recognition algorithm built from scratch in Python. This project demonstrates the core concepts of computer vision, including feature extraction (LBP), dimensionality reduction (Histograms), and classification (Euclidean Distance), without relying on the built-in OpenCV `LBPHFaceRecognizer`.

## Author
**Rishad Harisdias Bustomi**  
Website: [busto.dev](https://busto.dev)

## Features

- **Custom LBPH Implementation**: Manual calculation of Local Binary Patterns and Histograms.
- **Automated Data Collection**: Web scraping capabilities to gather training data (via `getdata.py`).
- **Face Detection**: Uses Haar Cascades for detecting faces in images and video streams.
- **Model Training**: Generates and stores histogram models using pickle.
- **Real-time Recognition**: Identifies faces in real-time using a webcam.
- **Attendance Logging**: Sends recognition data (identity & timestamp) to a remote server.

## Prerequisites

Ensure you have Python installed. You will needs the following dependencies:

- `opencv-python`
- `numpy`
- `requests`
- `selenium`
- `beautifulsoup4`
- `pandas`

## Installation

1.  Clone the repository and navigate to the project directory.
2.  Install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: You may need a ChromeDriver for `selenium` if you intend to use the scraping feature, referencing the path in `getdata.py`.*

## Usage

### 1. Data Collection
To gather training data (images), you can use the `getdata.py` script which scrapes images based on a configuration.
*Note: Ensure you have the correct ChromeDriver path configured in the script.*

```bash
python getdata.py
```

Alternatively, place your dataset in a `dataset/` folder with the structure `dataset/NIM_Name/`.

### 2. Training the Model
Train the recognition model using the collected images. This script processes the images, calculates LBP histograms, and saves the model to `data.p`.

```bash
python train.py
```

### 3. Real-time Recognition
Run the main application to start real-time face recognition via your webcam.

```bash
python main-run.py
```

- A countdown (1-4) will appear on screen.
- Every 5 seconds, the system captures a frame and attempts to recognize the face.
- If recognized, it logs the attendance to the server.
- Press **'q'** to quit the application.

## Project Structure

- `function.py`: Core library containing the custom LBPH algorithm, Euclidean distance calculations, and face detection logic.
- `train.py`: Script to process images from the `dataset/` directory and generate the training model (`data.p`).
- `main-run.py`: The main execution script for real-time video capture and recognition.
- `getdata.py`: Utility script for scraping or gathering image data.
- `dataset/`: Directory to store training images (organized by folders named `NIM_Name`).
- `haarcascades/`: Contains the Haar Cascade XML files for face detection.
