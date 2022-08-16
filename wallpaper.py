#I want to create a script that changes the wallpaper of a system

#Useful libraries that I would be working with -->
import os
import sys
import cv2 as cv
import urllib.request
import ctypes


#Declaring the functions
def change(link = None):
    try:
        imageUrl = str(link)
        # Go to specific url and download+save image using absolute path
        path = f'{os.getcwd()}\\background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
    except Exception as e:
        stat = f"Desktop Change File Selection Error: [{e}]"
        print(stat)
        return stat
    finally:
        try:
            SPI_SETDESKWALLPAPER = 20
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0) # Access windows dlls for funcionality eg, changing dekstop wallpaper
            stat = 'Changed Desktop background successfully!!'
            print(stat)
        except Exception as e:
            print(stat)
            stat = f"Desktop Change Background Error: [{e}]"
        finally:
            try:
                os.remove(path)
            except Exception as e:
                stat = f"Desktop Change File Deletion Error: [{e}]"
    return stat


if __name__ == "__main__":
    print("WALLPAPER CHANGER \n")

    link = "add-image-link-here"
    stat = change(link)
    print(f"Stat: {stat}")

    print("\nExecuted successfully!!")