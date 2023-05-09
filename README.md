# Accident Detection System

**Last Updated: *10/05/2023 ***

1. What is Accident Detection System?
2. Prerequisites
3. Getting Started- How to use it?
4. Description
5. Future Work



## 1. What is Accident Detection System?

An accident Detection System is designed to detect accidents via video or CCTV footage. Road accidents are a significant problem for the whole world. Many people lose their lives in road accidents. We can minimize this issue by using CCTV accident detection. This repository majorly explores how CCTV can detect these accidents with the help of Deep Learning.

## 3. Prerequisites

- To use this project Python Version > 3.6and Raspberrypi3 or greater version is needed
- To contribute to this project, knowledge of basic python scripting, Machine Learning, and Deep Learning will help.

## 4. Getting Started - How to use it?

### Clone this repository

To install all the packages required to run this python program
`pip install -r requirements.txt`

**Note:** This project requires a camera. So make sure you have a connected camera to your device. You can also use a downloaded video if not using a camera.

### Run
Before running the program, you need to run the `Model training classification.ipynb` file which will create the `model_weights.h5` file. Then, to run this python program, you need to execute the `main.py` python file.

## 5. Description

This program includes 4 things.

1. `data`: Kaggle dataset on [Accident Detection from CCTV footage](https://www.kaggle.com/code/mrcruise/accident-classification/data).
2. `Model Training classification.ipynb`: This is a jupyter notebook that generates a model to classify the above data. This file generates two important files `model.json` and `model_weights.h5`.
3. `detection.py`: This file loads the Accident Detection system with the help of `model.json` and `model_weights.h5` files.
4. `camera.py`: It packs the camera and executes the `detection.py` file on the video dividing it frame by frame and displaying the percentage of the prediction in the accident (if present) in the frame.
5. `api.py`:Basically twilio is used here to transfer messages to nearby authority.
6. `buzzer.py`: It is used as alarm system to nearest police station. The buzzer will triggered whenever accident will occur when probability of accident>90.

## 6. Future Work

We can use Gps Module to locate the real time location in form of coordinates to nearby emergency services, police station so that they can reach that place at earliest.
