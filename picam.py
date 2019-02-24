import picamera
import aiohttp
from aiohttp import web
from io import BytesIO
from time import sleep
from picamera import PiCamera


async def handle_base(request):
    return web.json_response({"status":"pong"})

async def handle_capture(request):
    # Create an in-memory stream
    #my_stream = BytesIO()
    #camera = PiCamera()
    #camera.start_preview()
    # Camera warm-up time
    #sleep(1)
    #camera.capture(my_stream, 'jpeg')

    my_file = open('tmp.jpg', 'wb')
    camera = PiCamera()
    camera.start_preview()
    sleep(2)
    camera.capture(my_file)
    # At this point my_file.flush() has been called, but the file has
    # not yet been closed
    my_file.close()
    camera.close()
    #return web.json_response({"image": str(bytes)})
    return web.Response(body=open("tmp.jpg", "rb").read(), content_type='image/jpeg')

app = web.Application()
app.add_routes([web.get('/ping', handle_base),
                web.get('/capture', handle_capture)])
web.run_app(app)
