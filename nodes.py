from io import BytesIO
from PIL import Image
import numpy as np
import requests

def send_image_to_discord_webhook(image, webhook_url):
    
    try:
        
        image_np = image.cpu().numpy().squeeze()
    
        image_np = np.clip(255. * image_np, 0, 255).astype(np.uint8)
        
        image = Image.fromarray(image_np)

        buffer = BytesIO()
        
        image.save(buffer, format = 'png')
        
        buffer.seek(0)
        
        data = {
            'username': 'Alper'
        }
        
        files = {
            'file': ('image.png', buffer, 'image/png')
        }

        response = requests.post(webhook_url, data = data, files = files)
        
        if response.status_code != 200:
            
            print(f'[ERROR] | response.text = {response.text}')
            print(f'[ERROR] | response.status_code = {response.status_code}')
        
    except Exception as exception:
        
        print(f'[ERROR] | {str(exception)}')

class Node_1:
    
    @classmethod
    def INPUT_TYPES(cls):
        
        return {
            
            'required': {
                
                'image': ('IMAGE',),
                'webhook_url': ('STRING', {'multiline': False, 'default': ''}),
                'send': (['yes', 'no'],),  
                                     
            }
            
        }
        
    RETURN_TYPES = ('IMAGE', )
    
    FUNCTION = 'execute'
    
    CATEGORY = 'Ahmet Alper'
    
    def execute(self, image, webhook_url, send):
        
        if send == 'yes':
                
            send_image_to_discord_webhook(image, webhook_url)
        
        return (image, )
