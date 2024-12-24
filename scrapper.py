import requests
from bs4 import BeautifulSoup
import csv

#Scrapes the image URLs you want to source, and outputs them as a CSV that will be readable by grabber. You'll need to modify this code if you're using anything but a Wordpress Gallery.


def scrape_image_data(url, output_csv):

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["URL", "Caption"])  # Write header row

            #From here, we grab Wordpress Gallery information. THIS IS THE SECTION TO CHANGE IF YOU'RE USING A DIFFERENT SITE!
            image_figures = soup.find_all('figure', class_='wp-block-image')
            for figure in image_figures:
                img_tag = figure.find('img')
                if img_tag and 'data-orig-file' in img_tag.attrs:
                    image_url = img_tag['data-orig-file']
                    figcaption_tag = figure.find('figcaption', class_='wp-element-caption')
                    caption = figcaption_tag.get_text(strip=True) if figcaption_tag else ""

                    csv_writer.writerow([image_url, caption])
    
    
    except requests.exceptions.RequestException as e:
      print(f"Error: Could not access the page at {url}: {e}")
    except Exception as e:
       print(f"Error scraping the page: {e}")

# Example usage:
url = "https://jacob-robinson.com/style/"  # Replace with your URL
output_csv = "style_images.csv"            # Path to output

scrape_image_data(url, output_csv)
print(f"Image data has been written to {output_csv}")