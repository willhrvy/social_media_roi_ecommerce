# Social Media Ecommerce ROI
## Investigating the impact of social media marketing on e-commerce performance and what industry competitors' reviews tell us about their performance.

## Motivation

With marketing budgets under increasing scrutiny, understanding the return on investment (ROI) from social media campaigns is vital for e-commerce businesses. This project aims to quantify the impact of consistent posting on Instagram on online store performance.

The central question is: How does social media marketing activity correlate with traffic and sales in an e-commerce context?

This project is particularly motivated by real-world business experience running an online store, where anecdotal evidence suggests strong links between certain social media actions and spikes in store metrics. The goal is to validate this with data and determine which types of social engagement provide the most value.

The second part of my research is to find areas that my business can find a competitve advantage by analysing what our competitors are doing well and not so well.

## Method

### Prerequisites
- Python 3.8+
- Required Python packages (install via `pip install -r requirements.txt`):

scrapfly-sdk>=0.8.23

pandas>=1.5.0

numpy>=1.24.0

matplotlib>=3.7.0

beautifulsoup4>=4.12.0

requests>=2.28.0

jupyter>=1.0.0

nbconvert>=7.0.0


### Execution Order
 
 1. run notebooks/insta_scraping.py 
 (This requires a valid Scrapfly API key, please make your own account and insert your key in Line 7 to replace mine - mine won't work; you can use their free trial https://scrapfly.io/ ).
 I used Scfraply's "How to scrape Instagram in 2025" blog to learn how to write this code. (Ališauskas, 2025)

 2. run python notebooks/clean_merge_data.py
 Processes raw data from Shopify, Instagram, and Klaviyo into data/processed/master_data.csv.

 3. Run notebooks/plot_session_sales.ipynb to:
Analyzes relationship between Instagram posts and sales/sessions
Generates visualizations in the visuals directory

4. Run cells in notebooks/trust_pilot_scrapers.ipynb to:
Scrapes Trustpilot reviews for competitors
Saves to respective CSV files in data/raw/

5. Review Analysis:
Run notebooks/reviews_analysis.ipynb to:
Performs sentiment analysis on competitor reviews
Generates word frequency visualizations


## Results

Instagram Posting Impacts Sales
Days with Instagram posts generated ~£5 higher daily net sales on average.

Posting on 3 consecutive days led to a 2x+ increase in average daily net sales — typically aligned with seasonal campaign launches.

Posts that went viral (e.g., one with 447k views and 20k likes) amplified both engagement and revenue, showing the power of timely, high-quality content.

Strategic Takeaway: Consistent posting, especially around campaigns, is a reliable sales driver. Hiring a part-time content creator to maintain this momentum could yield compounding returns.

Competitor Review Analysis Reveals Brand Gaps
Using sentiment analysis of customer reviews on Trustpilot:

Rebecca Udall: Exceptional positive-to-negative word ratio (~126:1), suggesting consistent fulfilment and high satisfaction.

Abask: Strong ratio (~53:1), but recurring complaints about delivery issues and technical usability.

Mrs Alice: High volume of both praise and criticism; worst positive-to-negative ratio (~23:1), with repeated complaints about damaged products and delays.

Strategic Takeaway: The main opportunity lies in owning the space of consistency — positioning as a brand known for reliable fulfilment, premium packaging, and stress-free service. This differentiates us from competitors with operational weaknesses, particularly Mrs Alice.


## Repository overview

This repository is structured as follows:

├── gitignore

    ├── .gitignore

├── data

    ├── processed

        ├── master_data.csv

    ├──raw

        ├── instagram_posts.csv

        ├── klavyio_report.csv

        ├── sessions_by_refferer_device_type_and_day.csv

        ├── total_sales_over_time.csv

        ├── trustpilot_reviews_abask.csv

        ├── trustpilot_reviews_mrsalice.csv

        ├── trustpilot_reviews_rebecca_udall.csv

├── notebooks

    ├── clean_merge_data.py

    ├── insta_scraping.py

    ├── plot_session_sales.ipynb

    ├── reviews_analysis.ipynb

    ├── trust_pilot_scrapers.ipynb

└── visuals

    ├── avg_sales_post_days_vs_non_post_days.png

    ├── negative_word_use_reviews.png

    ├── positive_word_use_reviews.png

    ├── sales_by_recent_posts.png
    
├── README.md

## Link to final blog post containing full analysis and insights

https://functional-impulse-7c7.notion.site/From-Posts-to-Profits-How-Social-Content-and-Trustpilot-Reviews-Shape-Performance-Across-Brands-1d98ece032558017b81ef6d7ec135195
