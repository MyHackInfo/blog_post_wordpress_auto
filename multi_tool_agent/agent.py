import os
import requests
from dotenv import load_dotenv
from google.adk.agents import LlmAgent, SequentialAgent

load_dotenv()

# Load WordPress credentials
WP_URL = os.getenv("WP_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

GEMINI_MODEL = "gemini-2.0-flash"

# ---- ADK Tool to Upload Blog Post ----
def upload_wordpress_post(generated_title: str, meta_description: str, slug: str, image_prompt: str, blog_content: str, category_id: str, focus_keyphrase: str) -> dict:
    """
    Uploads a blog post to WordPress with full SEO fields.
    """
    auth = (WP_USERNAME, WP_APP_PASSWORD)
    post_url = f"{WP_URL}/wp-json/wp/v2/posts"
    post_data = {
        "title": generated_title,
        "content": blog_content,
        "excerpt": meta_description,
        "categories": [int(category_id)],
        "slug": slug,
        "status": "publish",
        "meta": {
            "image_prompt": image_prompt,
            "_yoast_wpseo_metadesc": meta_description,
            "_yoast_wpseo_title": generated_title,
            "_yoast_wpseo_focuskw": focus_keyphrase,

        }
    }
    response = requests.post(post_url, auth=auth, json=post_data)

    if response.status_code != 201:
        raise Exception(f"Post upload failed: {response.text}")

    post = response.json()
    print(f"✅ Post published: {post['link']}")
    return {"Success": True, "link": post["link"]}

# ---- Agent: Generate Blog Title ----
blog_title_agent = LlmAgent(
    name="BlogTitleAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are a senior software engineer with 15+ years of experience who also writes for high-authority blogs.

    Your task is to craft a **natural-sounding**, **SEO-optimized** blog title that:
    - Feels authentic and engaging, like written by an experienced developer.
    - Includes real-world search terms developers or learners would use.
    - Avoids robotic or AI-like tone.

    For Title word related please following this rule:
    -Blog Title
    -Ideal Length: 55–65 characters
    -Style: Informative + Technical

    Must Include:

    -Primary keyword at the beginning
    -A specific tech term or tool
    -Optional: version numbers, frameworks, or tools (Node.js, ArgoCD, Golang, etc.)

    Example Titles:

    ✅ “Deploy Node.js App with ArgoCD on DigitalOcean: Step-by-Step” (62 chars)
    ✅ “Top 10 Useful Linux Commands for Software Engineers in 2025” (61 chars)

    If input is a topic, create a fitting blog title.

    """,
    description="Crafts natural, SEO-rich blog titles with technical authority.",
    output_key="generated_title"
)

meta_description_agent = LlmAgent(
    name="MetaDescriptionAgent",
    model=GEMINI_MODEL,
    instruction="""
        Input:
        - Blog Title: {generated_title}

        Task:
        Write a meta description (140–160 characters) that:
        - Feels human-written
        - Is keyword-rich and helpful
        - Avoids AI-sounding phrases like “This blog post...”
        - Summarizes the post clearly

        Example:
            Learn how to deploy a Node.js app using ArgoCD with DigitalOcean, covering YAML setup, Redis, CI/CD, and live production best practices. (157 chars)


        Respond with only the meta description.
        """,
    description="Creates meta description for SEO.",
    output_key="meta_description"
)

slug_agent = LlmAgent(
    name="SlugAgent",
    model=GEMINI_MODEL,
    instruction="""
        Input:
        - Blog Title: {generated_title}

        Task:
        Create a clean, SEO-friendly URL slug:
        - Use hyphens (-) between words
        - All lowercase
        - Avoid stop words
        - Ideal: 30–50 characters

        Respond with only the slug (e.g., `deploy-nodejs-app-argocd`).
        """,
    description="Generates SEO slug from the blog title.",
    output_key="slug"
)

# ---- Agent: Generate Blog Description ----
blog_content_agent = LlmAgent(
    name="BlogContentAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are a 15-year experienced software engineer and technical blogger.

    Input:
    - Title: {generated_title}

    Your task is to write a compelling, keyword-rich blog post content that:
    1. Feels like it's written by a real human with deep tech experience.
    2. Uses real-world keywords for AI tools and human search.
    4. Avoids clichés like "This article will..." or "In this blog..."
    5. Summarizes the key value of the article clearly and naturally.

    Content Body
    -Ideal Word Count: 1,200–1,800 words 
    Ideal Character Count: 8,000–11,000 characters
    -Please not use unnecessary <br> tag for blog content ( p tag with <br> tag is not allowed).

    Why:
    -Google prefers in-depth content on technical topics.
    -Tech readers (and AI tools) search for full stack, logs, configurations, code explanations, etc.
    -Higher engagement with complete walkthroughs.

    ✅ Break it into:
    -Introduction (100–150 words / ~700 characters)
    -3–5 Sections (with H3 and H4, each 250–400 words)
    -Code Examples + Use Cases if needed
    -Conclusion + Internal Links + Top 3,5 FAQs based on requirements of blog content.

    Headings (H3)
    -H3s: 30–50 characters, each targeting sub-keywords (e.g. “Setting Up Redis with Docker Compose”)
    -H4s: Use for breakdowns (e.g. “Step 1: Create docker-compose.yml”)

    Your output must sound confident, expert-written, and not like a machine.
    Note: In wordpress we use SyntaxHighlighter plugin for programming code show on it. (The language syntax to highlight with. You can alternately just use that as the tag, such as [php]code[/php]. Available tags: as3, actionscript3, arduino, bash, shell, coldfusion, cf, clojure, clj, cpp, c, c-sharp, csharp, css, delphi, pas, pascal, diff, patch, erl, erlang, fsharp, go, golang, groovy, haskell, java, jfx, javafx, js, jscript, javascript, latex, tex, matlab, matlabkey, objc, obj-c, perl, pl, php, plain, text, ps, powershell, py, python, r, splus, rails, rb, ror, ruby, scala, sql, swift, vb, vbnet, xml, xhtml, xslt, html, yaml, yml.)
    Output: Blog body in valid HTML or Markdown format.
    """,
    description="Generates expert-sounding, AI-discoverable blog body content.",
    output_key="generated_content"
)

# ---- Agent: Generate Image Prompt + Upload ----
image_prompt_agent = LlmAgent(
    name="ImagePromptAgent",
    model=GEMINI_MODEL,
    instruction="""
    You are an AI illustrator prompt engineer for Midjourney or DALL·E.

    Inputs:
    - Blog Title: {generated_title}
    - Blog Content: {generated_content}

    Task:
    1. Write a descriptive, vivid, visually-inspiring image prompt for an illustration based on the blog content.
    2. Ensure the prompt feels creative and matches the blog's subject.
    3. Keep it clean, colorful, and realistic — no generic AI language.
    4. Based on the blog title, content, assign it to the correct WordPress category using the following IDs:
    - AI: 41
    - Gadgets: 24
    - MERN: 15
    - Shopify: 6
    - Wordpress: 5
    5. Based on the blog title, content, assign it to the correct WordPress focus keyphrase on 'focus_keyphrase'.

    Think carefully about the topic and return the right category ID.


    Then automatically call the tool `upload_wordpress_post` with:
    - generated_title
    - meta_description
    - slug
    - image_prompt
    - generated_content
    - category_id
    - focus_keyphrase
    """,
    description="Generates an illustration image prompt, classifies content, and publishes blog to WordPress.",
    tools=[upload_wordpress_post],
    output_key="image_prompt"
)

# ---- Sequential Workflow ----
seo_blog_pipeline_agent = SequentialAgent(
    name="SeoBlogPipelineAgent",
    sub_agents=[blog_title_agent, meta_description_agent, slug_agent, blog_content_agent, image_prompt_agent],
    description="Generates a blog title, content, meta description, slug, illustration prompt, and publishes it.",
)

# ---- Required Root Agent ----
root_agent = seo_blog_pipeline_agent
