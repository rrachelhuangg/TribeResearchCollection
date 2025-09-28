<img width="1710" height="562" alt="Screenshot 2025-09-28 at 9 33 43 AM" src="https://github.com/user-attachments/assets/5714dd0e-6aa2-46d7-bffb-77ecc2ee28e5" />

## Inspiration
The Tribe Research Collection was inspired by the release of the Firecrawl web-scraper in 2024.

## What it does
The Tribe Research Collection is a web app intended to help users learn about the recent research projects that William & Mary professors have published. Each project description is linked to the published paper so that users can easily learn more about the research.

## How we built it
The displayed data is web-scraped from William & Mary faculty websites, and then passed to the OpenAI GPT-4o API for summarization. The summarized information for each project is then rendered with HTML, served with Flask, and deployed with Vercel.

## Challenges we ran into
The amount of data that was able to be scraped and processed for this project was constrained by the Firecrawl API limits that determined the speed and number of websites that could be processed during the hackathon.

## Accomplishments that we're proud of
Building and deploying a web app with a new web-scraper tool, as well as integrating with the OpenAI API and building a clean UI to display the processed data.

## What we learned
Firecrawl is a very powerful web-scraper that is able to return extremely clean data from websites, so that minimal processing is needed to clean the website content afterwards.

## What's next for The Tribe Research Collection
Finding a way to surpass the Firecrawl API limits so that more project data can be scraped at one time. Implement a refresh button that can rescrape and reprocess data when the user wants to make sure that the displayed data is the most up-to-date.
