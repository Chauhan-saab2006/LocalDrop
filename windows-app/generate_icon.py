import os
from PIL import Image, ImageDraw, ImageColor

# Settings
size = 1024
radius = 200
bg_color = ImageColor.getrgb("#1E1E1E")
border_color = ImageColor.getrgb("#333333")
border_width = 8 # scaled up to be visible in 1024x1024, if 1px is desired literally, change to 1
arrow_color = ImageColor.getrgb("#E5E5E5")
bar_color = ImageColor.getrgb("#9CA3AF")

# Create image with alpha channel
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw rounded square (background)
draw.rounded_rectangle([border_width, border_width, size - border_width, size - border_width], radius=radius, fill=bg_color, outline=border_color, width=border_width)

# Center of image
cx, cy = size // 2, size // 2

# Draw horizontal bar/pill shape below
bar_width = 400
bar_height = 60
bar_y = cy + 160
draw.rounded_rectangle([cx - bar_width // 2, bar_y, cx + bar_width // 2, bar_y + bar_height], radius=bar_height // 2, fill=bar_color)

# Draw downward arrow
arrow_w = 80
arrow_h = 320
arrow_top_y = cy - 260
# Arrow shaft
draw.rectangle([cx - arrow_w // 2, arrow_top_y, cx + arrow_w // 2, cy], fill=arrow_color)
# Arrow head
arrow_head_w = 260
arrow_head_h = 160
draw.polygon([
    (cx - arrow_head_w // 2, cy),
    (cx + arrow_head_w // 2, cy),
    (cx, cy + arrow_head_h)
], fill=arrow_color)

# Save
os.makedirs("src-tauri/icons", exist_ok=True)
img.save("src-tauri/icons/source-icon.png")
print("Icon created successfully.")
