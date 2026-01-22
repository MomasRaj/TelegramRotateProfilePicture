import asyncio
import telethon
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
import os
from PIL import Image

apiId = 123456
apiHash = "Your api apiHash"

#The name of your photos, put them on a folder called photos.
path = "pfp.jpg"
pathRotated = "pfpRotated.jpg"

async def main():
    hour = datetime.now().hour
    degrees = -((hour*30)%360)
    img = Image.open(path)
    img = img.rotate(degrees, expand=True)
    img.save(pathRotated)
    
    async with telethon.TelegramClient("session", apiId, apiHash) as client:
        current = await client.get_profile_photos("me", limit=1)
        if current:
            await client(DeletePhotosRequest(current))
        uploaded = await client.upload_file(pathRotated)

        await client(UploadProfilePhotoRequest(file=uploaded))

asyncio.run(main())