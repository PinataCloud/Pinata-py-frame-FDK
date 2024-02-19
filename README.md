# A Simple Frame For Showcasing Content

This is a 102 line, 3 file Python project so you can get started with showcasing content on Farcaster.

## Project Variables
GATEWAY_URL=Your Pinata Gateway

PROJECT_URL=Your Server URL

TITLE=Title your project. This will appear in title sections of the project. This will also assist in your frame analytics, which this will also be your frame_id.

EXTERNAL_URL=A url that will be linked to a button on the last frame that will take users to an external url of your choosing.

INITIAL_IMAGE_URL=This is a url that will be the first image people see. This should not change as Farcaster clients cache this.

FOLDER_CID=The CID hash that you want to showcase in your frame.

NUMBER_OF_IMAGES=The number of images in your folder.

IMAGE_TYPE=What type of image are you using, jpg, png... this is the 3 letter suffix of your types, must be the same.

PINATA_JWT=This is your Pinata JWT that will be used so you can get frame analytics on your frame.

PORT=8000 use this port in your cloud services

## Python 3.12.1

## Build Command:
pip install -r requirements.txt

## Deploy Command:
uvicorn main:app --host 0.0.0.0 --port $PORT
