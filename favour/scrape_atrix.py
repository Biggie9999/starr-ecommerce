import requests
from bs4 import BeautifulSoup
import re

def get_distributors(base_url="https://www.atrix.com/distributors/"):
    # This is a hypothetical scraping script as the site structure is not fully accessible to the agent.
    # We would scrape the category links first, then each category for distributor names.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    }
    
    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Hypothetical: finding category links
        category_links = []
        for link in soup.find_all('a', href=True):
            if 'product-category' in link['href'] or 'distributors/' in link['href']:
                category_links.append(link['href'])
                
        distributors = set()
        
        # Scraping each category
        for cat_link in set(category_links):
            if not cat_link.startswith('http'):
                cat_link = "https://www.atrix.com" + cat_link
            
            try:
                cat_resp = requests.get(cat_link, headers=headers)
                cat_soup = BeautifulSoup(cat_resp.text, 'html.parser')
                
                # Hypothetical: extracting distributor names
                for h3 in cat_soup.find_all('h3', class_='distributor-name'):
                    distributors.add(h3.get_text(strip=True))
            except Exception as e:
                print(f"Error scraping category {cat_link}: {e}")
                
        return list(distributors)

    except Exception as e:
        print(f"Error accessing the main page: {e}")
        return []

if __name__ == "__main__":
    distributors = get_distributors()
    print(f"Found {len(distributors)} distributors.")
    for d in distributors:
        print(d)
