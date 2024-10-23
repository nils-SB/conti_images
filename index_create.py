import os

def generate_index_html(directory):
    # Start HTML structure
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Correlation Heatmap Index</title>
    </head>
    <body>
        <h1>Correlation Heatmaps</h1>
        <ul>
    """
    print(directory)
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "index.html":
            # Add a list item with a link for each HTML file
            html_content += f'            <li><a href="{filename}">{filename}</a></li>\n'

    # Close HTML structure
    html_content += """
        </ul>
    </body>
    </html>
    """

    # Write the index.html file
    with open(os.path.join(directory, 'index.html'), 'w') as file:
        file.write(html_content)

    print("index.html has been created successfully.")

# Specify the directory where the HTML files are stored
# You can change this to the path of your choice
directory = "Executed_trades/correlation_plots/conti_images/"  # Current directory, change if necessary
generate_index_html(directory)
