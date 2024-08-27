from io import BytesIO
from PIL import Image
import numpy as np
import requests

def send_image_to_discord(image, discord_webhook_url):
    
    try:
        
        image_np = image.cpu().numpy().squeeze()
    
        image_np = np.clip(255. * image_np, 0, 255).astype(np.uint8)
        
        image = Image.fromarray(image_np)

        buffer = BytesIO()
        
        image.save(buffer, format = 'png')
        
        buffer.seek(0)
        
        files = {
            'file' : ('image.png', buffer, 'image/png')
        }

        response = requests.post(discord_webhook_url, files = files)
                        
        if response.status_code not in [200, 204]:
            
            print(f'[ERROR] | response.json() | {response.json()}')
            print(f'[ERROR] | response.status_code | {response.status_code}')        
        
    except Exception as exception:
        
        print(f'[ERROR] | send_image_to_discord_webhook() | {str(exception)}')

class Node_1:
    
    @classmethod
    def INPUT_TYPES(cls):
        
        return {
            
            'required' : {
                
                'image' : ('IMAGE', ),
                'discord_webhook_url' : ('STRING', ),
                'send' : (['yes', 'no'], )
                                     
            }
            
        }
        
    RETURN_TYPES = ('IMAGE', )
    
    FUNCTION = 'execute'
    
    CATEGORY = 'ahmetalper/discord'
    
    def execute(self, image, discord_webhook_url, send):
        
        if send == 'yes':
                
            send_image_to_discord(image, discord_webhook_url)
        
        return (image, )
