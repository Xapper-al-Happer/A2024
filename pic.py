from PIL import Image, ImageGrab
import pyautogui

# Take a screenshot using Pillow
screenshot_pillow = ImageGrab.grab()

# Get the size of the screen
screen_width, screen_height = screenshot_pillow.size

# Define the dimensions for the crop (adjust as needed)
crop_width = 1800
crop_height = 600

# Calculate the coordinates for the crop
left = (screen_width - crop_width) // 2
top = (screen_height - crop_height) // 2
right = left + crop_width
bottom = top + crop_height

# Crop the image to the middle of the screen
cropped_image = screenshot_pillow.crop((left, top, right, bottom))

# Save or display the cropped image
cropped_image.save(r'1.png')
# was ("1.png")