import os
import markdown2
import yaml
from datetime import datetime
import shutil


def parse_front_matter(content):
    """Parse YAML front matter from markdown content."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    front_matter = yaml.safe_load(parts[1])
    return front_matter, parts[2]


def convert_markdown_to_html(markdown_content):
    """Convert markdown content to HTML."""
    return markdown2.markdown(markdown_content, extras=["fenced-code-blocks", "tables"])


def generate_project_links(project):
    """Generate HTML for project links."""
    links = []
    if project.get("github"):
        links.append(f'<a href="{project["github"]}" class="link">GitHub →</a>')
    if project.get("demo"):
        links.append(f'<a href="{project["demo"]}" class="link">Live Demo →</a>')
    return "\n".join(links)


def process_posts(directory, output_dir):
    """Process all markdown files in a directory."""
    posts = []

    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename != "template.md":
            with open(os.path.join(directory, filename), "r") as f:
                content = f.read()

            front_matter, markdown_content = parse_front_matter(content)
            html_content = convert_markdown_to_html(markdown_content)

            # Create HTML file
            html_filename = filename.replace(".md", ".html")
            with open(os.path.join(output_dir, html_filename), "w") as f:
                f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{front_matter.get("title", "Untitled")}</title>
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/#projects">Projects</a></li>
                <li><a href="/#blog">Blog</a></li>
            </ul>
        </nav>
    </header>
    <main class="content">
        <article>
            <h1>{front_matter.get("title", "Untitled")}</h1>
            <div class="metadata">
                <time datetime="{front_matter.get("date", "")}">{front_matter.get("date", "")}</time>
            </div>
            {html_content}
        </article>
    </main>
    <footer>
        <p>© 2025 Rishav Katoch. All rights reserved.</p>
    </footer>
</body>
</html>""")

            posts.append(
                {
                    "title": front_matter.get("title", "Untitled"),
                    "date": front_matter.get("date", ""),
                    "description": front_matter.get("description", ""),
                    "url": f"/{output_dir}/{html_filename}",
                    "tags": front_matter.get("tags", []),
                    "technologies": front_matter.get("technologies", []),
                    "github": front_matter.get("github", ""),
                    "demo": front_matter.get("demo", ""),
                }
            )

    return sorted(posts, key=lambda x: x["date"], reverse=True)


def main():
    # Create output directories
    os.makedirs("_site/blog", exist_ok=True)
    os.makedirs("_site/projects", exist_ok=True)

    # Copy static files
    shutil.copy("styles.css", "_site/")
    shutil.copy("index.html", "_site/")
    shutil.copy("where-to-plant.html", "_site/")
    shutil.copy("CNAME", "_site/")

    # Process blog posts and projects
    blog_posts = process_posts("blog/_posts", "_site/blog")
    projects = process_posts("projects/_posts", "_site/projects")

    # Update index.html with latest posts and projects
    with open("index.html", "r") as f:
        index_content = f.read()

    # Update blog section
    blog_html = "\n".join(
        [
            f'<article class="blog-post">\n'
            f'    <h3><a href="{post["url"]}">{post["title"]}</a></h3>\n'
            f'    <p class="date">{post["date"]}</p>\n'
            f"    <p>{post['description']}</p>\n"
            f'    <a href="{post["url"]}" class="link">Read More →</a>\n'
            f"</article>"
            for post in blog_posts[:5]  # Show only 5 latest posts
        ]
    )

    # Update projects section
    projects_html = "\n".join(
        [
            f'<article class="project-card">\n'
            f'    <h3><a href="{project["url"]}">{project["title"]}</a></h3>\n'
            f"    <p>{project['description']}</p>\n"
            f'    <div class="project-links">\n'
            f'        <a href="{project["url"]}" class="link">View Details →</a>\n'
            f"        {generate_project_links(project)}\n"
            f"    </div>\n"
            f"</article>"
            for project in projects[:6]  # Show only 6 latest projects
        ]
    )

    # Replace placeholders in index.html
    index_content = index_content.replace("<!-- BLOG_POSTS -->", blog_html)
    index_content = index_content.replace("<!-- PROJECT_CARDS -->", projects_html)

    with open("_site/index.html", "w") as f:
        f.write(index_content)


if __name__ == "__main__":
    main()
