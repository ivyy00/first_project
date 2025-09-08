import cloudinary.uploader
from cloudinary.utils import cloudinary_url

def upload_image():
    upload_result = cloudinary.uploader.upload(
        "https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg",
        public_id="shoes"
    )
    return upload_result["secure_url"]

def get_optimized_url():
    return cloudinary_url("shoes", fetch_format="auto", quality="auto")[0]

def get_cropped_url():
    return cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")[0]
