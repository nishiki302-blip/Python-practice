import requests

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist}
            )
    
    except requests.RequestException:
        print("Sever not found.")
        return

    content = response.json()
    for artwork in content["data"]:
        print(f"# {artwork["title"]}")

main()