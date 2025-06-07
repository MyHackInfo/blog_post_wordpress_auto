import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, LlmAgent, SequentialAgent
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Load credentials
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")
GEMINI_MODEL="gemini-2.0-flash"

# def upload_post_with_image(title="title---narsi", description="description---test", image_path=""):
#     # Auth
#     auth = (WP_USERNAME, WP_APP_PASSWORD)

#     # # Step 1: Upload the image
#     # media_url = f"{WP_URL}/wp-json/wp/v2/media"
#     # headers = {
#     #     "Content-Disposition": f"attachment; filename={os.path.basename(image_path)}"
#     # }
#     # with open(image_path, "rb") as img:
#     #     media_response = requests.post(media_url, headers=headers, auth=auth, files={"file": img})
    
#     # if media_response.status_code != 201:
#     #     raise Exception(f"Image upload failed: {media_response.text}")

#     # media_id = media_response.json()["id"]

#     media_id = 595

#     # Step 2: Create the blog post with image
#     post_url = f"{WP_URL}/wp-json/wp/v2/posts"
#     post_data = {
#         "title": title,
#         "content": description,
#         "status": "draft",  # Or 'draft'
#         "featured_media": media_id
#     }
#     post_response = requests.post(post_url, auth=auth, json=post_data)

#     if post_response.status_code != 201:
#         raise Exception(f"Post upload failed: {post_response.text}")

#     post = post_response.json()
#     print(f"✅ Post published: {post['link']}")
#     return post["link"]


# Blog Title Generator Agent
blog_title_agent = LlmAgent(
    name="BlogTitleAgent",
    model=GEMINI_MODEL,
    instruction="""You are an expert in SEO blog writing.
    Your task is to generate a catchy, SEO-optimized title for a blog post.

    If the user input is a topic, write a title based on it.
    If the input is a URL, analyze the content and write an updated, engaging, and unique blog title.

    Respond only with the title, no explanation.
    """,
    description="Generates a blog post title from a topic or website URL.",
    output_key="generated_title"
)

# Blog Description Generator Agent
blog_description_agent = LlmAgent(
    name="BlogDescriptionAgent",
    model=GEMINI_MODEL,
    instruction="""You are an AI assistant trained to write SEO-friendly blog descriptions.

    **Input:**
    - Title: {generated_title}

    **Task:**
    Write a compelling, AI-discoverable blog post description that:
    1. Is between 40-60 words
    2. Highlights the key value of the content
    3. Includes relevant SEO keywords naturally
    4. Is unique and engaging for search engines and users

    Respond only with the description.
    """,
    description="Generates a SEO and AI-optimized blog description.",
    output_key="generated_description"
)

# # Image Prompt Generator Agent
# image_prompt_agent = LlmAgent(
#     name="ImagePromptAgent",
#     model=GEMINI_MODEL,
#     instruction="""You are an AI image prompt writer for DALL-E or Midjourney.

#     **Input:**
#     - Blog Title: {generated_title}
#     - Blog Description: {generated_description}

#     **Task:**
#     Write a vivid, descriptive image prompt that could be used to generate an illustration for this blog post.
#     Make it imaginative, AI-friendly, and highly visual.

#     Respond only with the prompt, no explanation.
#     """,
#     description="Generates an AI-illustration image prompt based on the title and description.",
#     output_key="image_prompt"
# )


# --- 2. Create the SequentialAgent ---
# This agent orchestrates the pipeline by running the sub_agents in order.
seo_blog_pipeline_agent = SequentialAgent(
    name="SeoBlogPipelineAgent",
    sub_agents=[blog_title_agent, blog_description_agent],
    description="Generates blog title, description and image prompt based on topic or URL input.",
)

# For ADK tools compatibility, the root agent must be named `root_agent`
root_agent = seo_blog_pipeline_agent