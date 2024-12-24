import serpapi
import csv

# The grabber. Takes a CSV file "style_images.csv" and uses SerpAPI to find the first five Google search results for your image.


def extract(source_csv, output_csv, api_key):


    sources = [] # Initialize an empty list of image URLs
    with open(source_csv, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader) # Skip the header row
        for row in csv_reader:
            if len(row) > 0:
                sources.append(row[0]) # Add the first column to the list of image URLs


    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Image", "Link 1 Title", "Link 1 URL", "Link 1 Snippet",
                             "Link 2 Title", "Link 2 URL", "Link 2 Snippet",
                             "Link 3 Title", "Link 3 URL", "Link 3 Snippet",
                             "Link 4 Title", "Link 4 URL", "Link 4 Snippet",
                             "Link 5 Title", "Link 5 URL", "Link 5 Snippet"])

        for source in sources:
            print(f"Processing: {source}...")
            try:
                # Perform reverse image search using SerpAPI
                params = {
                    "engine": "google_reverse_image",
                    "image_url": source,
                    "api_key": api_key
                }
                results = serpapi.search(params)

                # Extract the top 5 results
                row = [source]
                if "image_results" in results and results["image_results"]:
                    for i, result in enumerate(results["image_results"][:5]):
                        title = result.get("title", "N/A")
                        link = result.get("link", "N/A")
                        snippet = result.get("snippet", "N/A")
                        row.extend([title, link, snippet])

                # Pad the rest of the row with N/A if less than 5 results
                while len(row) < 16:
                    row.extend(["N/A", "N/A", "N/A"])

                csv_writer.writerow(row)


            except Exception as e:
                print(f"Error processing {source}: {e}")


source_csv = "style_images.csv"  # Path to the CSV file containing image URLs
output_csv = "source_results.csv" # Path to output
api_key = "YOUR SERPAPI KEY HERE"  # Replace with your SerpAPI key

extract(source_csv, output_csv, api_key)
print(f"CSV file has been generated at {output_csv}")


