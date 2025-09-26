from PIL import Image, ImageEnhance
import os

def split_and_enhance_panorama(image_path, output_folder):
    # Target dimensions for Instagram post
    target_width = 1080
    target_height = 1291
    num_posts = 6

    # Load the panorama image
    img = Image.open(image_path)
    img_width, img_height = img.size
    print(f"Original image size: {img_width}x{img_height}")

    # Calculate the width for each split
    slice_width = img_width // num_posts

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
# csv
    for i in range(num_posts):
        # Crop the slice
        left = i * slice_width
        right = (i + 1) * slice_width if i < num_posts - 1 else img_width
        cropped = img.crop((left, 0, right, img_height))

        # Resize using high-quality filter
        resized = cropped.resize((target_width, target_height), resample=Image.LANCZOS)

        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(resized)
        enhanced = enhancer.enhance(1.2)  # 1.2 = 20% sharper than original

        # File base name
        base_name = os.path.join(output_folder, f"insta_post_{i+1}")

        # Save as JPEG
        # enhanced.save(base_name + ".jpg", format="JPEG", , subsampling=0)

        # Save as PNG
        enhanced.save(base_name + ".png", format="PNG",quality=100, optimize=True,compress_level=0)

        print(f"✅  {base_name}.png")

    print(f"\n🎉 All {num_posts} posts saved in both JPG and PNG format at '{output_folder}'.")

# Example usage
split_and_enhance_panorama("123.png", "output_posts")
