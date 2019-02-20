#import subprocess
#subprocess.run(["pyinstaller", "--add-data Fonts/*.ttf;Fonts --add-data Images/*.png;Images --add-data Sounds/*.ogg;Sounds --noconsole __main__.py"])

import os
os.system("pyinstaller --add-data Fonts/*.ttf;Fonts --add-data Images/*.png;Images --add-data Sounds/*.ogg;Sounds --noconsole __main__.py")

# TODO: rename and zip the folder in the dist folder

# TODO: also make a zip for the source
