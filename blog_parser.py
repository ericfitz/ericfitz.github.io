import os
import re
from datetime import datetime
from typing import List, Dict

def parse_date(date_line: str) -> str:
    """
    Parse a date from a line like '> Published on Apr 23, 2025' 
    and return it in YYYY-MM-DD format
    """
    # Extract the date portion after "Published on"
    date_match = re.search(r'Published on\s+(.+)', date_line.strip())
    if not date_match:
        return ""
    
    date_str = date_match.group(1).strip()
    
    # Try to parse common date formats
    date_formats = [
        "%b %d, %Y",  # Apr 23, 2025
        "%B %d, %Y",  # April 23, 2025
        "%m/%d/%Y",   # 4/23/2025
        "%Y-%m-%d"    # 2025-04-23 (already in correct format)
    ]
    
    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            continue
    
    return ""

def parse_markdown_file(filepath: str) -> Dict[str, str]:
    """
    Parse a markdown file and extract filename, title, and date
    """
    result = {
        'filename': os.path.basename(filepath),
        'title': '',
        'date': ''
    }
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            
            # Look for title (H1 starting with single #)
            if line.startswith('# ') and not result['title']:
                result['title'] = line[2:].strip()
            
            # Look for publication date (line starting with >)
            elif line.startswith('> Published on') and not result['date']:
                result['date'] = parse_date(line)
                
            # Stop once we have both title and date
            if result['title'] and result['date']:
                break
                
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    
    return result

def markdown_to_html(markdown_content: str, title: str) -> str:
    """
    Convert markdown content to HTML with basic formatting
    """
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: sans-serif;
            max-width: 800px;
            margin: 40px auto;
            line-height: 1.6;
            padding: 0 20px;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        h1 {{ font-size: 2em; }}
        h2 {{ font-size: 1.5em; }}
        h3 {{ font-size: 1.25em; }}
        p {{ margin-bottom: 15px; }}
        blockquote {{
            border-left: 4px solid #ddd;
            margin: 0 0 15px 0;
            padding-left: 15px;
            color: #666;
            font-style: italic;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: monospace;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        a {{
            color: #0066cc;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        ul, ol {{
            margin-bottom: 15px;
            padding-left: 30px;
        }}
        li {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
"""
    
    lines = markdown_content.split('\n')
    in_code_block = False
    code_block_content = []
    
    for line in lines:
        # Handle code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                # End of code block
                html_content += '<pre><code>' + '\n'.join(code_block_content) + '</code></pre>\n'
                code_block_content = []
                in_code_block = False
            else:
                # Start of code block
                in_code_block = True
            continue
        
        if in_code_block:
            code_block_content.append(line)
            continue
        
        # Handle headers
        if line.startswith('#'):
            level = len(line) - len(line.lstrip('#'))
            if level <= 6:
                text = line[level:].strip()
                html_content += f'<h{level}>{text}</h{level}>\n'
                continue
        
        # Handle blockquotes
        if line.strip().startswith('>'):
            text = line.strip()[1:].strip()
            html_content += f'<blockquote>{text}</blockquote>\n'
            continue
        
        # Handle unordered lists
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            text = line.strip()[2:]
            html_content += f'<ul><li>{text}</li></ul>\n'
            continue
        
        # Handle ordered lists
        if re.match(r'^\d+\.\s', line.strip()):
            text = re.sub(r'^\d+\.\s', '', line.strip())
            html_content += f'<ol><li>{text}</li></ol>\n'
            continue
        
        # Handle links [text](url)
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', line)
        
        # Handle inline code `code`
        line = re.sub(r'`([^`]+)`', r'<code>\1</code>', line)
        
        # Handle bold **text**
        line = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', line)
        
        # Handle italic *text*
        line = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', line)
        
        # Regular paragraph or empty line
        if line.strip():
            html_content += f'<p>{line}</p>\n'
    
    html_content += """</body>
</html>"""
    
    return html_content

def convert_markdown_file_to_html(filepath: str):
    """
    Convert a markdown file to HTML and save it with .html extension
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        
        # Extract title from first H1 or use filename
        title = os.path.splitext(os.path.basename(filepath))[0]
        lines = markdown_content.split('\n')
        for line in lines:
            if line.strip().startswith('# '):
                title = line[2:].strip()
                break
        
        # Convert to HTML
        html_content = markdown_to_html(markdown_content, title)
        
        # Write HTML file
        html_filename = os.path.splitext(filepath)[0] + '.html'
        with open(html_filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        print(f"Converted {filepath} -> {html_filename}")
        
    except Exception as e:
        print(f"Error converting {filepath}: {e}")

def generate_html(blog_posts: List[Dict[str, str]]) -> str:
    """
    Generate HTML content for the blog posts
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>efitz Blog</title>
    <style>
        body {
            font-family: sans-serif;
            margin: 40px;
        }
        h1 {
            margin-bottom: 30px;
        }
        table {
            border-collapse: collapse;
            width: 100%;
        }
        td {
            padding: 8px 16px;
            vertical-align: top;
        }
        .date-column {
            white-space: nowrap;
            width: 120px;
        }
        a {
            text-decoration: none;
            color: #0066cc;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>efitz Blog</h1>
    <p>All new posts will be on a new Blogspot blog <a href="https://efitz-thoughts.blogspot.com/">"Stuff I'm thinking about"</a>.</p>
    <table>
"""
    
    for post in blog_posts:
        if post['title'] and post['date']:
            # Change .md extension to .html
            html_filename = os.path.splitext(post['filename'])[0] + '.html'
            html_content += f"""        <tr>
            <td class="date-column">{post['date']}</td>
            <td><a href="{html_filename}">{post['title']}</a></td>
        </tr>
"""
    
    html_content += """    </table>
</body>
</html>"""
    
    return html_content

def main():
    """
    Main function to process all markdown files in the current directory
    """
    blog_posts = []
    
    # Get all .md files in current directory
    for filename in os.listdir('.'):
        if filename.endswith('.md'):
            filepath = os.path.join('.', filename)
            post_info = parse_markdown_file(filepath)
            blog_posts.append(post_info)
            
            # Convert markdown file to HTML
            convert_markdown_file_to_html(filepath)
    
    # Sort by date (most recent first)
    blog_posts.sort(key=lambda x: x['date'], reverse=True)
    
    # Generate HTML
    html_content = generate_html(blog_posts)
    
    # Write HTML file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated index.html with {len(blog_posts)} blog posts")

if __name__ == "__main__":
    main()