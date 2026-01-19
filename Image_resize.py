from PIL import Image


input_file = "vertical.png"       # replace with image filename
output_file = "verticalLogo.png"     # output filename
width_cm = 25                  # wanted width in cm
dpi = 300                      # wanted DPI

# cm to inches
width_inch = width_cm / 2.54

#opening the image
img = Image.open(input_file)

# maintain aspect ratio
pixel_width = int(width_inch * dpi)
w_percent = (pixel_width / float(img.width))
pixel_height = int((float(img.height) * float(w_percent)))

#resize
img_resized = img.resize((pixel_width, pixel_height), Image.LANCZOS)

# resize DPI
img_resized.save(output_file, dpi=(dpi, dpi))

print(f"Image saved as {output_file} at {dpi} DPI and {width_cm} cm width.")

from PIL import Image


input_file = "logoResized.png"       # replace with image filename
output_file = "horizontalLogo.png"     # output filename
width_cm = 25                  # wanted width in cm
dpi = 300                      # wanted DPI

# cm to inches
width_inch = width_cm / 2.54

#opening the image
img = Image.open(input_file)

# maintain aspect ratio
pixel_width = int(width_inch * dpi)
w_percent = (pixel_width / float(img.width))
pixel_height = int((float(img.height) * float(w_percent)))

#resize
img_resized = img.resize((pixel_width, pixel_height), Image.LANCZOS)

# resize DPI
img_resized.save(output_file, dpi=(dpi, dpi))

print(f"Image saved as {output_file} at {dpi} DPI and {width_cm} cm width.")