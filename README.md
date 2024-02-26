# A Simple Frame For Showcasing Content

A no code solution for people who want to get a frame up with their content. This is a simple 3 file Python project so you can get started with showcasing content on Farcaster. All this requires a Pinata account, Github account and a Railway account.

## Project Variables
GATEWAY_URL=Your Pinata Gateway. Include https://, also do not have any slashes at the end, ex: https://mygateway.mypinata.cloud

PROJECT_URL=Your Server URL. Include https://, also do not have any slashes at the end, ex: https://myprojecturl.railway.app

TITLE=Title your project. This will appear in title sections of the project. This will also assist in your frame analytics, which will also be your frame_id. No spaces or special characters.

EXTERNAL_URL=A url that will be linked to a button on the last frame that will take users to an external url of your choosing.

INITIAL_IMAGE_URL=This is a url that will be the first image people see. This should not change as Farcaster clients cache this.

FOLDER_CID=The CID hash that you want to showcase in your frame.

NUMBER_OF_IMAGES=The number of images in your folder.

IMAGE_TYPE=What type of image are you using, jpg, png... this is the 3 letter suffix of your image file name, must be the same.

PINATA_JWT=This is your Pinata JWT that will be used so you can get frame analytics on your frame.

PORT=8000 use this port in your cloud services

### Example:

GATEWAY_URL=https://alienframeware.mypinata.cloud

PROJECT_URL=https://lyte-cycles.up.railway.app

TITLE=LyteCycles

EXTERNAL_URL=https://www.lytecycle.com

INITIAL_IMAGE_URL=https://www.lytecycle.com/ipfs/QmRx3pGZm6ebtFmudzH8x6cMTzm5ecGUYMr56tT78ka35Q

FOLDER_CID=QmdAi1v1quzrRjE2r97gmWuJpxJNAqn8gywcwrQq91gpoZ

NUMBER_OF_IMAGES=9

IMAGE_TYPE=jpg

PINATA_JWT=eyJhbSOMEJWTFROMPINATA

PORT=8000

## Python 3.12.1

## Build Command:
pip install -r requirements.txt

## Deploy Command:
uvicorn main:app --host 0.0.0.0 --port $PORT

## Repo Information:
Go to https://pinata.cloud to create a free account to set your GATEWAY_URL, FOLDER_CID, and PINATA_JWT.
I used Railway (https://railway.app/) my web server services, they also have a free trial for 30 days.

## Steps:
1. Set your variables, recommend putting them into a text doc.
2. Go to Pinata, get your gateway, folder CID and JWT.
3. Fork this repo to your github account.
4. Go to Railway and link your github account.
5. Create a web service in Railway.
6. Get your project URL under service settings (networking) by creating it.
7. In the variables, paste your variables into the raw editor.
8. Under your service setting, set the build command and set the deploy command.
9. Spin up the services and then cast your frame.
10. Let people view your frame.
11. View analytics at Pinata.
