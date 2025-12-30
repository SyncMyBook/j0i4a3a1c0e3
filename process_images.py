from PIL import Image
import sys
import os

images_list = os.environ.get('IMAGES', '').strip().split('\n')
imgs = []
for img_path in images_list:
    if img_path:
        try:
            imgs.append(Image.open(img_path))
        except Exception as e:
            print(f"Error opening image {img_path}: {e}")

if not imgs:
    print("No valid images found.")
    sys.exit(0)

widths, heights = zip(*(i.size for i in imgs))
total_height = sum(heights)
max_width = max(widths)

new_im = Image.new('RGB', (max_width, total_height))

y_offset = 0
for im in imgs:
    new_im.paste(im, (0, y_offset))
    y_offset += im.size[1]

new_im.save(os.environ.get('OUTPUT_IMAGE', 'output.png'))
print(f"Image saved as {os.environ.get('OUTPUT_IMAGE', 'output.png')}")
