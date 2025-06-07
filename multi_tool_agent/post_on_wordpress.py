import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load credentials
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

def upload_post_with_image(title="title---narsi", description="description---test", image_path=""):
    # Auth
    auth = (WP_USERNAME, WP_APP_PASSWORD)

    # # Step 1: Upload the image
    # media_url = f"{WP_URL}/wp-json/wp/v2/media"
    # headers = {
    #     "Content-Disposition": f"attachment; filename={os.path.basename(image_path)}"
    # }
    # with open(image_path, "rb") as img:
    #     media_response = requests.post(media_url, headers=headers, auth=auth, files={"file": img})
    
    # if media_response.status_code != 201:
    #     raise Exception(f"Image upload failed: {media_response.text}")

    # media_id = media_response.json()["id"]

    media_id = 595

    # Step 2: Create the blog post with image
    post_url = f"{WP_URL}/wp-json/wp/v2/posts"
    post_data = {
        "title": title,
        "content": description,
        "status": "draft",  # Or 'draft'
        "featured_media": media_id
    }
    post_response = requests.post(post_url, auth=auth, json=post_data)

    if post_response.status_code != 201:
        raise Exception(f"Post upload failed: {post_response.text}")

    post = post_response.json()
    print(f"✅ Post published: {post['link']}")
    return post["link"]

if __name__ == "__main__":
    upload_post_with_image()

