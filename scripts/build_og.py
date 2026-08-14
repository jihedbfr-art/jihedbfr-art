import os
from PIL import Image, ImageDraw, ImageFont

def build_og_image():
    width, height = 1280, 640
    
    # Create dark background
    image = Image.new('RGB', (width, height), color='#0a1420')
    draw = ImageDraw.Draw(image)
    
    # We will try to use a default font if a specific one isn't available
    try:
        # Try to load a standard sans-serif font
        font_title = ImageFont.truetype("arial.ttf", 80)
        font_subtitle = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        
    # Draw simple gold accent line at the top
    draw.rectangle([(0, 0), (width, 10)], fill='#d4af37')
    
    # Add text
    title = "J.BFR"
    subtitle = "JIHED AI LABS"
    
    # Center text manually
    title_bbox = draw.textbbox((0, 0), title, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) / 2
    
    sub_bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    sub_width = sub_bbox[2] - sub_bbox[0]
    sub_x = (width - sub_width) / 2
    
    draw.text((title_x, height/2 - 60), title, font=font_title, fill="#d4af37")
    draw.text((sub_x, height/2 + 40), subtitle, font=font_subtitle, fill="#4fc0ff")
    
    # Draw simple circuit lines
    draw.line([(100, height/2), (title_x - 50, height/2)], fill="#2f9bd6", width=3)
    draw.line([(width - 100, height/2), (title_x + title_width + 50, height/2)], fill="#2f9bd6", width=3)
    
    os.makedirs('assets/social', exist_ok=True)
    image.save('assets/social/og-preview.png')
    print("Generated assets/social/og-preview.png (1280x640)")

if __name__ == "__main__":
    build_og_image()
