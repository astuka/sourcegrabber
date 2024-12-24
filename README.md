# Astukari's Source Grabber

Are you a curator? Do you have a massive gallery of images that you've been sharing to the masses? Do you now have said masses breathing down your neck, saying you're not crediting the creator, and are now panicking to find the credits to thousands of images you just downloaded off the internet without a second thought?

Source Grabber uses SerpAPI's Google Reverse Image Search to find source credits at scale. Worry no longer!

# Requirements

You'll need an account with SerpAPI: https://serpapi.com/

For free users, SerpAPI only allows 100 free requests a month, so if you aren't paying make sure your CSV file is 100 rows or less.

Everything else is in requirements.txt.

# How it works

You'll need an input CSV titled "style_images.csv" with the image URLs that you need sourced in the first column. In the repo is a scrapper I used for my own purposes which you can modify for use. Read the code comments on the scrapper to figure out how it works. 

Once you get your csv in the sourcegrabber folder, run grabber.py. Your output will be at source_results.csv. It will grab up to the first five Google Image search results for your image. Usually the source will be either in the title or snippet, but the URLs are also there in case you want to dive deeper. 

# Known Issues/Restrictions

In terms of reverse image searching, Google is currently the best we've got. Unfortunately, its far from perfect. 

As a rule, the more obscure your image is, the less likely Google will pop out with a correct answer. If you input Starry Night by Van Gogh it will almost certainly give you the right results, but if you are trying to get an artist from Twitter or a still from a movie, it's more likely to give you a nonsense answer.

For my own curation purposes, I usually just kill off and delete images that I can't find a source too, just to save me the headache. You could use further image searchers like iqdb or Yandex, but Source Grabber currently doesn't have the capabilities to use these. 