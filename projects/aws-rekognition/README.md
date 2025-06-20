# AWS Rekognition Project - Image Detection and Labeling

<p align="center">
  <img src="./assets/screenshot.png" alt="Vista previa" width="600"/>
</p>


## Project Overview
This project uses Amazon Rekognition to analyze images stored in an AWS S3 bucket and detect objects present, generating labels with confidence scores. The processed image is saved with visible bounding boxes and labels, making it easier to visually interpret the analysis.

## Technologies Used
- **AWS S3:** Secure storage for images.
- **Amazon Rekognition:** Automatic image recognition and labeling service.
- **Python:** Main programming language, using libraries:
  - `boto3` (AWS SDK)
  - `Pillow` (image manipulation and drawing)
  - `matplotlib` (image visualization and saving)
- **AWS CLI and IAM:** Credentials and permissions management for secure resource access.

## How It Works
1. An image is uploaded to an AWS S3 bucket.
2. The Python script downloads the image from the bucket and runs Rekognition to detect labels and objects with their bounding boxes.
3. The image is processed by drawing red boxes around detected objects and adding text with the label name and confidence score.
4. The result is displayed on screen and saved locally as `processed_image.png` for future reference or presentation.

## How to Use

### Prerequisites
- AWS credentials configured (via AWS CLI or environment variables).
- Python 3.x installed.
- Required libraries installed:

```bash
pip install boto3 pillow matplotlib
