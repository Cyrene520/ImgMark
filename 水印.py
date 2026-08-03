import math
import os
from PIL import Image, ImageDraw, ImageFont


def add_watermark(
    input_folder,
    output_folder,
    watermark_text,
    font_file_path,
    text_size,
    spacing,
    alpha,
    angle=45,
):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    input_files = [
        f
        for f in os.listdir(input_folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    for input_file in input_files:
        input_path = os.path.join(input_folder, input_file)
        output_path = os.path.join(output_folder, input_file)

        image = Image.open(input_path).convert("RGBA")
        width, height = image.size

        # Calculate the diagonal to ensure the canvas is not empty at the corners
        diagonal = int(math.hypot(width, height)) * 2

        # Create an overlay layer with a larger size than the original image
        text_layer = Image.new("RGBA", (diagonal, diagonal), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)

        font = ImageFont.truetype(font_file_path, size=text_size)
        bbox = font.getbbox(watermark_text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Large-scale canvas tiling
        for x in range(0, diagonal, text_width + spacing):
            for y in range(0, diagonal, text_height + spacing):
                draw.text(
                    (x, y), watermark_text, font=font, fill=(255, 153, 213, alpha) #Text color with alpha transparency (0-255) - (black to white)
                )

        # Rotate the overlay layer by the specified angle (expand=False to keep the original center)
        rotated_text_layer = text_layer.rotate(
            angle, resample=Image.BICUBIC, expand=False
        )

        # Crop the rotated overlay back to the correct size at the center of the original image
        left = (diagonal - width) // 2
        top = (diagonal - height) // 2
        cropped_text_layer = rotated_text_layer.crop(
            (left, top, left + width, top + height)
        )

        # Merge the watermark with the original image
        merged = Image.alpha_composite(image, cropped_text_layer)
        merged = merged.convert("RGB")
        merged.save(output_path)


if __name__ == "__main__":
    input_folder_path = "C"
    output_folder_path = "Cyrene"
    watermark_text = "Cyrene"
    font_file_path = "C"
    text_size = 50
    spacing = 50
    alpha = 20
    angle = 45

    add_watermark(
        input_folder_path,
        output_folder_path,
        watermark_text,
        font_file_path,
        text_size,
        spacing,
        alpha,
        angle,
    )