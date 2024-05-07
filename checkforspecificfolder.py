import os
import time
def check_picture_exists(folder_path, picture_name):
    # Construct the full path to the picture file
    picture_path = os.path.join(folder_path, picture_name)
    
    # Check if the file exists
    if os.path.exists(picture_path):
        return True
    else:
        return False

# Example usage

folder_path = "Camera"
count = 0
numLEDs= 10
while(count != numLEDs-1):
    picture_name = "frame_" + str(count)+ ".jpg"
    if(check_picture_exists(folder_path, picture_name)):
        print(picture_name + " is here")
        count = count + 1
        
        
    else:
        print( "Cant find" + picture_name)
        time.sleep(2)
        

