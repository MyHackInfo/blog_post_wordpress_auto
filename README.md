# WordPress Blog Post Automation

This project automates the process of creating and managing blog posts on WordPress.

## Features

- Automated blog post generation
- WordPress integration
- Content management tools
- Scheduled posting

## Prerequisites

- Python 3.7+
- WordPress installation with XML-RPC enabled
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd blog_post_wordpress_auto
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Copy `.env.example` to `.env` and update the configuration:
   ```
   GOOGLE_API_KEY=your-google-api-key
   GOOGLE_GENAI_USE_VERTEXAI=FALSE

   WORDPRESS_URL=your-wordpress-site-url
   WORDPRESS_USERNAME=your-username
   WORDPRESS_PASSWORD=your-password
   ```

## Usage

Run the main script:

```bash
adk web
```

## Project Structure

```
blog_post_wordpress_auto/
├── multi_tool_agent/
│   └── agent.py
├── .gitignore
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
