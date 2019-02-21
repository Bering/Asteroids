import os
os.system("pyinstaller --add-data Fonts/*.ttf;Fonts --add-data Images/*.png;Images --add-data Sounds/*.ogg;Sounds --noconsole __main__.py")

# TODO:
# * Rename the folder in the dist folder
# * Zip the folder in the dist folder
# * Delete the build folder
# * Delete the __main__ folder from the dist folder (keep the zip)
# * Zip the source (exclude .git, pycache and dist folders)
# * Upload both zips to ringlogic.com
