from io import BytesIO
from PIL import Image
from tqdm import tqdm
import numpy as np
import requests
import os

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

            print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')
            
            print(f'[ ERROR ] | response.json() = {response.json()}\n')
            print(f'[ ERROR ] | response.status_code = {response.status_code}')

            print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')
        
    except Exception as exception:

        print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')
        
        print(f'[ ERROR ] | {str(exception)}')

        print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')

def download_file(url, download_path, filename, civitai_api_key, overwrite):

    print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')

    file_path = os.path.abspath(f'{download_path}/{filename}')

    if os.path.exists(file_path):

        if overwrite == 'no':

            print(f'[ WARNING ] | {filename} already exists in {file_path}.\n')
            print(f'[ INFO ] | If you want to overwrite it, set \'overwrite\' option to \'yes\'.')

            print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')

            return

    if url.startswith('https://civitai.com') and civitai_api_key != '':

        url = f'{url}?token={civitai_api_key}'

    print(f'[ INFO ] | url = {url}\n')
    print(f'[ INFO ] | filename = {filename}\n')
    print(f'[ INFO ] | download_path = {file_path}\n')

    try:

        response = requests.get(url, stream = True)

        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        with open(file_path, 'wb') as file, tqdm(desc = filename, total = total_size, unit = 'iB', unit_scale = True, unit_divisor = 1024) as progress_bar:

            for data in response.iter_content(chunk_size = 8192):
                
                size = file.write(data)
                
                progress_bar.update(size)

        print(f'\n[ INFO ] | {filename} successfully downloaded to {file_path}.')
        
        print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')
    
    except Exception as exception:

        print(f'[ ERROR ] | {str(exception)}')

        print('\n#------------------------------ << [ ahmetalper ] >> ------------------------------#\n')

class Node_1:
    
    @classmethod
    def INPUT_TYPES(cls):
        
        return {
            
            'required' : {
                
                'image' : ('IMAGE', {}),
                'discord_webhook_url' : ('STRING', {'default' : '', 'tooltip' : 'What is the URL of the Discord webhook you want to send the image to ?'}),
                'send' : (['yes', 'no'], {'tooltip' : 'Do you want to send the image to the Discord webhook ?'})
                                     
            }
            
        }
        
    RETURN_TYPES = ('IMAGE', )
    
    FUNCTION = 'execute'
    
    CATEGORY = 'ahmetalper'
    
    def execute(self, image, discord_webhook_url, send):
        
        if send == 'yes':
                
            send_image_to_discord(image, discord_webhook_url)
        
        return (image, )
    
class Node_2:

    @classmethod
    def INPUT_TYPES(cls):
        
        return {
            
            'required' : {
                
                'image' : ('IMAGE', {}),
                'url' : ('STRING', {'default' : '', 'tooltip' : 'What is the URL of the file you want to download ?'}),
                'download_path' : (['models/checkpoints', 'models/loras'], {'tooltip' : 'Where do you want to download the file ?'}),
                'filename' : ('STRING', {'default' : '', 'tooltip' : 'What do you want to name the downloaded file ?'}),
                'civitai_api_key' : ('STRING', {'default' : '', 'tooltip' : 'For private or login required models, you need to have a Civitai API key.'}),
                'overwrite' : (['yes', 'no'], {'tooltip' : 'If the file already exists, do you want to overwrite it ?'}),
                'download' : (['yes', 'no'], {'tooltip' : 'Do you want to download the file ?'})
                                     
            }
            
        }
    
    RETURN_TYPES = ('IMAGE', )
    
    FUNCTION = 'execute'
    
    CATEGORY = 'ahmetalper'

    def execute(self, image, url, download_path, filename, download, civitai_api_key, overwrite):
        
        if download == 'yes':
            
            download_file(url, download_path, filename, civitai_api_key, overwrite)
        
        return (image, )
