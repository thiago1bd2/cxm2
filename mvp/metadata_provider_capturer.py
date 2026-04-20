import subprocess
import json

exif_binary_name = 'exiftool'

file_target = '/home/tela-mx/Downloads/Warpinator/IMG-20200418-WA0010_1.jpg'

result = subprocess.run(['exiftool', '-j', '-FileName', '-ModifyDate',file_target], capture_output=True)

binary_output = result.stdout

text_output = result.stdout.decode('utf-8')

data = json.loads(text_output)

# print(data[0]['ModifyDate'])

modify_date = data[0]['ModifyDate']
file_name = data[0]['FileName']

print(f'{modify_date}')
print(f'{file_name}')

