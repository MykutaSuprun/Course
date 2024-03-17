import requests

def search_gifs(search_query, api_key, limit=5):
    url = f"https://api.giphy.com/v1/gifs/search"
    params = {
        "q": search_query,
        "api_key": api_key,
        "limit": limit,
        "lang": "en"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        gifs = data["data"]
        for gif in gifs:
            gif_url = gif["images"]["original"]["url"]
            print(gif_url)
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    search_term = input("Enter the search term to find GIFs: ")
    api_key = "GIPHY_API_KEY"  # Використайте реальний апі ключа(в мене не вийшло його отримати,але по ідеї все повинно працювати)
    search_gifs(search_term, api_key)

main()