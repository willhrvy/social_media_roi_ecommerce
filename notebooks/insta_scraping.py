import json
import asyncio
from datetime import datetime
from scrapfly import ScrapeConfig, ScrapflyClient

#Add Scrapfy Key and user agent
SCRAPFLY = ScrapflyClient(key="scp-live-f7277159c7144b2785af67e458d579da")
BASE_CONFIG = {
    "asp": True,
    "country": "US",
    "headers": {
        "x-ig-app-id": "936619743392459",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
}

async def scrape_all_user_posts(username: str):
    """Scrape ALL posts with pagination"""
    next_max_id = None
    total_posts = 0
    
    while True:
        # Build URL with pagination
        url = f"https://www.instagram.com/api/v1/feed/user/{username}/username/?count=12"
        if next_max_id:
            url += f"&max_id={next_max_id}"
            
        result = await SCRAPFLY.async_scrape(
            ScrapeConfig(url, **BASE_CONFIG, method="GET")
        )
        
        data = json.loads(result.content)
        
        if not data.get("items"):
            print("No more posts or error occurred")
            break
            
        for item in data["items"]:
            total_posts += 1
            yield {
                "date": datetime.fromtimestamp(item["taken_at"]).strftime("%Y-%m-%d"),
                "shortcode": item["code"],
                "likes": item.get("like_count", 0),
                "comments": item.get("comment_count", 0)
            }
            
        # Get next page token
        next_max_id = data.get("next_max_id")
        if not next_max_id:
            break
            
        print(f"Scraped {total_posts} posts so far...")
        await asyncio.sleep(1)  # Be polite with rate limiting

async def main():
    username = "hens_and_hollyhocks"
    print(f"Scraping ALL posts from @{username}...")
    
    # Save to CSV
    import csv
    with open("instagram_posts.csv", "w", newline="") as csvfile:
        fieldnames = ["date", "shortcode", "likes", "comments"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        async for post in scrape_all_user_posts(username):
            writer.writerow(post)
            print(f"Date: {post['date']}, Shortcode: {post['shortcode']}")

    print("All posts saved to instagram_posts.csv")

if __name__ == "__main__":
    asyncio.run(main())