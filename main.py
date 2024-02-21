import json
import textwrap
import os
import util.pinataAnalytics as pinataAnalytics

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def home(request: Request):
    return HTMLResponse(
        status_code=200,
        content=textwrap.dedent(
            f"""
            <!DOCTYPE html>
            <html>
                <head>
                    <title>{os.environ.get('TITLE')}</title>
                    <meta property="og:title" content="{os.environ.get('TITLE')}" />
                    <meta property="fc:frame:image" content="{os.environ.get('INITIAL_IMAGE_URL')}" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:button:1" content="Begin" />
                    <meta property="fc:frame:post_url" content="{os.environ.get('PROJECT_URL')}/view?frame=1" />
                </head>
                <body>
                    <h1>{os.environ.get('TITLE')} on Farcaster!</h1>
                    <div>
                        <img src="{os.environ.get('INITIAL_IMAGE_URL')}" alt="{os.environ.get('TITLE')}">
                    </div>
                    <div>
                        <a href="https://pinata.cloud" target="_blank">Powered by Pinata</a>
                    </div>
                </body>
            </html>
        """
        ),
    )

@app.post("/view")
@app.get("/view")
async def view(request: Request):
    try :
        body = await request.body()
        body_str = body.decode('utf-8')
        pinataAnalytics.send_post_request(json.loads(body_str))
    except Exception as e:
        print(f"Error: {e}")
    frame_index = request.query_params.get("frame")
    next_frame = int(frame_index) + 1 
    imgCount = int(os.environ.get('NUMBER_OF_IMAGES'))
    if int(frame_index) == imgCount:
        return HTMLResponse (
            status_code=200,
            content=textwrap.dedent(
                f"""<!DOCTYPE html><html><head>
                    <title>This is frame {frame_index}</title>
                    <meta property="og:title" content="Frame" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:image" content="{os.environ.get('GATEWAY_URL')}/ipfs/{os.environ.get('FOLDER_CID')}/{frame_index}.jpg" />
                    <meta property="fc:frame:button:1" content="{os.environ.get('TITLE')}" />
                    <meta property="fc:frame:button:1:action" content="link" />
                    <meta property="fc:frame:button:1:target" content="{os.environ.get('EXTERNAL_URL')}" />
                    <meta property="fc:frame:button:2" content="Built With..." />
                    <meta property="fc:frame:button:2:action" content="link" />
                    <meta property="fc:frame:button:2:target" content="https://pinata.cloud" />
                    </head></html>"""
            )
        )    
    else:
        return HTMLResponse (
            status_code=200,
            content=textwrap.dedent(
                f"""<!DOCTYPE html><html><head>
                    <title>This is frame {frame_index}</title>
                    <meta property="og:title" content="Frame" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:image" content="{os.environ.get('GATEWAY_URL')}/ipfs/{os.environ.get('FOLDER_CID')}/{frame_index}.jpg" />
                    <meta property="fc:frame:button:1" content="Next" />
                    <meta property="fc:frame:post_url" content="{os.environ.get('PROJECT_URL')}/view?frame={next_frame}" />
                    </head></html>"""
            )
        )
