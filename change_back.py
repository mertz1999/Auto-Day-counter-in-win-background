from datetime import date
import ctypes
import time
import cv2 

 
# function to find number of days remaining
def numOfDays(date1, date2):
    return (date2-date1).days
     
# Set times (today, end)
date1 = date.today()
date2 = date(2023, 1, 13)

#find number of days remaining
diff = numOfDays(date1, date2)

# Read image
img = cv2.imread("BACK.jpg")
img_shape = img.shape

# Setting for TEXT
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
org = (img_shape[1]-200, 50)
fontScale = 1
color = (0, 0, 0)
thickness = 2

# Write TEXT
image = cv2.putText(
		img, 
		str(diff)+" Days",
		org, 
		font, 
		fontScale, 
		color, 
		thickness, 
		cv2.LINE_AA, 
		False
		)

# Save and change background
cv2.imwrite("C:\\.......\\BACK_changed.jpg", image)
ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\.......\\BACK_changed.jpg" , 0)
