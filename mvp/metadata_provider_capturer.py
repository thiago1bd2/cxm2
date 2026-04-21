import subprocess
import json

exif_binary_name = 'exiftool'

file_target = '/home/tela-mx/Downloads/Warpinator/IMG-20200418-WA0010_1.jpg'

result = subprocess.run(['exiftool', '-j', '-FileName', '-ModifyDate','/home/tela-mx/Downloads/Warpinator/*.jpg'], capture_output=True)

binary_output = result.stdout

text_output = result.stdout.decode('utf-8')

# data = json.loads(text_output)

print(text_output)



