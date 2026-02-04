import asyncio
import telethon
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
import os
from PIL import Image

apiId = 123456
apiHash = "YOUR_API_KEY"

#Photos
path = "pfp.jpg"
pathRotated = "pfpRotated.jpg"


async def main():
    async with telethon.TelegramClient("session", apiId, apiHash) as client:
        while True:
            now = datetime.now()
            nextHour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            await asyncio.sleep((nextHour - now).total_seconds())
            hour = datetime.now().hour
            degrees = -((hour * 30) % 360)
            img = Image.open(path)
            img = img.rotate(degrees)
            img.save(pathRotated)
            current = await client.get_profile_photos("me", limit=1)
            if current:
                await client(DeletePhotosRequest(current))

            uploaded = await client.upload_file(pathRotated)
            await client(UploadProfilePhotoRequest(file=uploaded))

asyncio.run(main())
