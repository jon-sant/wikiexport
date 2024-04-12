import requests
from bs4 import BeautifulSoup
from weasyprint import HTML

# Function to extract content between specified headers
def extract_sections(markdown_content, start_header, end_header):
    start_index = markdown_content.find(start_header)
    end_index = markdown_content.find(end_header)
    if start_index == -1 or end_index == -1:
        return ""
    return markdown_content[start_index:end_index]

# Fetch wiki page from GitHub using the API
wiki_page = "testhome.md"  # Name of the wiki page
base_url = "https://raw.githubusercontent.com/jon-sant/wikiexport/main/"
print(f"{base_url}{wiki_page}")
markdown_content = requests.get(f"{base_url}{wiki_page}").text

# Define the header to start from
#start_header = "<h1 class=""heading-element"">Sodales dui porta</h1>"
start_header = "# Sodales dui porta"
# Define the header to end at (if you want to extract until the next header)
#end_header = "<h1 class=""heading-element"">Sapien volutpat</h1>"
end_header = "# Sapien volutpat"

# Extract sections between the specified headers
section_content = extract_sections(markdown_content, start_header, end_header)

# Convert Markdown to HTML
html_content = f"<html><body>{section_content}</body></html>"
with open("section.html", "w") as f:
    f.write(markdown_content)

# Convert HTML to PDF using WeasyPrint
pdf = HTML(string=html_content).write_pdf()

# Save PDF
with open("section.pdf", "wb") as f:
    f.write(pdf)
