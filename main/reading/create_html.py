import pandas as pd
import webbrowser
import os

def create_html_text(df):
    """Convert analyzed text components into HTML with color coding"""
    html_parts = []
    
    # Add HTML header with CSS
    html_parts.append("""
    <html>
    <head>
        <style>
            body { 
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 40px 350px;  /* top/bottom: 40px, left/right: 200px */
            }
            .word {
                cursor: pointer;
            }
            .word:hover {
                background-color: #f0f0f0;
            }
            .green { color: green; }
            .blue { color: blue; }
            .orange { color: orange; }
            .red { color: red; }
            .black { color: black; }
            .verse-number {
                font-size: 0.8em;
                vertical-align: super;
                color: #666;
                margin-right: 2px;
            }
        </style>
    </head>
    <body>
    """)
    
    # Convert each component to HTML
    for _, row in df.iterrows():
        if row['is_word']:
            # Add hover title with rank and translation info if it's a known word
            rank_info = f" (rank: {row['rank']})" if pd.notna(row['rank']) else ""
            translation_info = f"\nTranslation: {row['translation']}" if pd.notna(row['translation']) else ""
            html_parts.append(
                f'<span class="word {row["color"]}" title="{row["lemma"]}{rank_info}{translation_info}">'
                f'{row["component"]}</span>'
            )
        else:
            # Check if it's a verse number marker
            component = row['component']
            if component.startswith('^'):
                html_parts.append(f'<span class="verse-number">{component[1:]}</span>')
            else:
                # Other non-word components (punctuation, spaces) just get added as-is
                html_parts.append(component)
    
    # Close HTML
    html_parts.append("</body></html>")
    
    return "".join(html_parts)

def save_and_display_html(df, output_path='main/Texts/matthew_analyzed.html'):
    """Save the analyzed text as a color-coded HTML file and open in browser"""
    html_content = create_html_text(df)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"\nSaved color-coded text to: {output_path}")
    
    # Convert to absolute path and open in browser
    abs_path = os.path.abspath(output_path)
    webbrowser.open('file://' + abs_path)

if __name__ == '__main__':
    from process_text import process_bible_text
    df = process_bible_text()
    save_and_display_html(df) 