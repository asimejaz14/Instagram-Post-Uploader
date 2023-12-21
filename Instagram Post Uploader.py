import json
import os
from PIL import Image
from instabot import Bot
from resizeimage import resizeimage

import config
from security import safe_requests

data = ''

# replace eg.json with your own file name
with open('eg.json', encoding='utf-8') as file:
    data = file.read()

json_data = json.loads(data)

bot = Bot()

bot.login(username=config.USERNAME,
          password=config.PASSWORD)

for j_data in json_data.items():
    caption = j_data[1]['caption']

    for image_path in (j_data[1]['images']):
        print("Caption:", caption)
        print(image_path)
        response = safe_requests.get(image_path)
        file = open("1.jpg", "wb")
        file.write(response.content)
        file.close()
        fd_img = open('1.jpg', 'rb')
        img = Image.open(fd_img)
        img = resizeimage.resize_crop(img, [1080, 1080])
        img.save('1.jpg', img.format)
        fd_img.close()
        bot.upload_photo('1.jpg', caption=caption)
        os.remove("1.jpg.REMOVE_ME")
    print()
