import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

# Open an image file
img = Image.open("LineFollower1.png")
# Convert image to PhotoImage
photo = ImageTk.PhotoImage(img)

img_label = tk.Label(root, image=photo)
img_label.pack()

root.mainloop()