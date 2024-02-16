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
                    <title>Lyte Cycles</title>
                    <meta property="og:title" content="Lyte Cycles" />
                    <meta property="fc:frame:image" content="https://www.lytecycle.com/ipfs/QmXJmFJxRELU2KT7NSYqLcnqGaGbFftD3vtkb9fa28YWv1" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:button:1" content="Begin" />
                    <meta property="fc:frame:post_url" content="{os.environ.get('PROJECT_URL')}/view?frame=1" />
                </head>
                <body>
                    <h1>Lyte Cycles</h1>
                    <div>
                        <img src="{os.environ.get('GATEWAY_URL')}/ipfs/{os.environ.get('FOLDER_CID')}/mc1.jpg" alt="Lyte Cycles Image">
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
def view(request: Request):
    try :
        pinataAnalytics.send_post_request(request)
    except Exception as e:
        print(f"Error: {e}")
    #body = request.body()
    
    #buttonIndex = body.data.untrusted
    #print(f"Button {buttonIndex} was clicked")
    frame_index = request.query_params.get("frame")
    next_frame = int(frame_index) + 1
    
    if int(frame_index) == 9:
        return HTMLResponse (
            status_code=200,
            content=textwrap.dedent(
                f"""<!DOCTYPE html><html><head>
                    <title>This is frame {frame_index}</title>
                    <meta property="og:title" content="Frame" />
                    <meta property="fc:frame" content="vNext" />
                    <meta property="fc:frame:image" content="{os.environ.get('GATEWAY_URL')}/ipfs/{os.environ.get('FOLDER_CID')}/mc{frame_index}.jpg" />
                    <meta property="fc:frame:button:1" content="Built With..." />
                    <meta property="fc:frame:button:1:action" content="link" />
                    <meta property="fc:frame:button:1:target" content="https://pinata.cloud" />
                    <meta property="fc:frame:button:2" content="Lyte Cycles" />
                    <meta property="fc:frame:button:2:action" content="link" />
                    <meta property="fc:frame:button:2:target" content="https://www.lytecycle.com/ipfs/{os.environ.get('FOLDER_CID')}/mc1.jpg" />
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
                    <meta property="fc:frame:image" content="{os.environ.get('GATEWAY_URL')}/ipfs/QmZedFbSgdYsssqvhhoCswnjHC8Zd4Ade7s6wfQbwGVhtt/mc{frame_index}.jpg" />
                    <meta property="fc:frame:button:1" content="Next Page" />
                    <meta property="fc:frame:post_url" content="{os.environ.get('PROJECT_URL')}/view?frame={next_frame}" />
                    </head></html>"""
            )
        )