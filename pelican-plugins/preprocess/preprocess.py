from bs4 import BeautifulSoup
from pelican import signals

def preprocess_content(instance):
    if hasattr(instance, 'content') and instance.content:
        content = instance.content
        soup = BeautifulSoup(content, 'html.parser')
        output_content = ''
        remaining_content = ''
        h1_h2_count = 0

        # Use a flag to start capturing remaining content after the second <h1> or <h2>
        capture_remaining = False

        for tag in soup.children:
            if tag.name in ['h1', 'h2']:
                h1_h2_count += 1
                if h1_h2_count == 2:
                    capture_remaining = True

            if capture_remaining:
                remaining_content += str(tag)
            else:
                output_content += str(tag)

        # Assign the split content back to the instance
        instance.processed_content = output_content
        instance.remaining_content = remaining_content

def register():
    signals.content_object_init.connect(preprocess_content)