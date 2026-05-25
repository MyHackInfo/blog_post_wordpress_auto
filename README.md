# 🚀 AI Blog Post WordPress Automation

An advanced AI-powered blog generation and publishing system built using Google's Agent Development Kit (ADK) with multi-agent orchestration.

This project automates the complete blogging workflow — from generating SEO-optimized content using AI agents to automatically publishing posts on WordPress.

---

# ✨ Features

* 🤖 Multi-Agent AI Architecture
* 🔄 Sequential AI Workflow using `SequentialAgent`
* 🧠 AI Content Generation using `LlmAgent`
* 📝 SEO-Optimized Blog Creation
* 🖼️ AI Image Prompt Generation
* 🌐 Automatic WordPress Publishing
* ⚡ Modular & Scalable Agent Design
* 🔐 Environment Variable Configuration using `.env`
* 📦 Easy Integration & Customization
* 🚀 Production-Friendly Project Structure

---

# 🏗️ Built With

* Python
* Google ADK (Agent Development Kit)
* Gemini / LLM Models
* WordPress REST API
* Multi-Agent Orchestration
* Sequential Processing Pipelines

---

# 🔄 AI Agent Workflow

This project uses multiple specialized AI agents working together sequentially to automate the complete blog publishing process.

```text
Input Topic
    ↓
SEO Title Agent
    ↓
Meta Description Agent
    ↓
Slug Generator Agent
    ↓
Blog Content Writer Agent
    ↓
Image Prompt Generator Agent
    ↓
WordPress Publisher Agent
```

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/MyHackInfo/blog_post_wordpress_auto.git
cd blog_post_wordpress_auto
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key

WORDPRESS_URL=your_wordpress_url
WORDPRESS_USERNAME=your_wordpress_username
WORDPRESS_PASSWORD=your_wordpress_password
```

---

# ▶️ Run Project

```bash
python main.py
```

---

# 🧠 How It Works

The system accepts a blog topic as input and automatically performs the following tasks:

* Generates SEO-friendly titles
* Creates optimized meta descriptions
* Generates clean URL slugs
* Writes complete AI-generated blog content
* Creates AI image prompts
* Publishes content directly to WordPress

All tasks are managed through sequential AI agents using Google ADK.

---

# 📌 Use Cases

* Automated Blogging Systems
* AI Content Marketing
* SEO Content Pipelines
* WordPress Automation
* Multi-Agent AI Workflows
* AI Publishing Infrastructure
* ADK Learning Projects
* Content Generation Automation

---

# 🎯 Project Goal

The goal of this project is to demonstrate how multiple AI agents can collaborate together to automate real-world content creation and publishing workflows.

This repository serves as:

* A practical AI automation example
* A Google ADK multi-agent implementation
* An AI-powered publishing pipeline
* A scalable content generation architecture

---

# 🚀 Future Improvements

* ✅ AI Image Generation Support
* ✅ Social Media Auto Posting
* ✅ Blog Scheduling System
* ✅ Multi-Language Blog Generation
* ✅ WordPress Category & Tag Automation
* ✅ Analytics & Performance Tracking
* ✅ Human Approval Workflow
* ✅ Docker Deployment Support

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 🌟 Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

# 👨‍💻 Author

Developed by [MyHackInfo](https://github.com/MyHackInfo)
