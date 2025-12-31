import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"


def fetch_data():
    response = requests.get(url)
    return response.json()


def extract_data(posts):
    result = []

    for post in posts[:5]:
        result.append({
            "id": post["id"],
            "title": post["title"],
            "userId": post["userId"]
        })

    return result


def save_json(data):
    with open("output.json", "w") as f:
        json.dump(data, f, indent=4)


def main():
    posts = fetch_data()              # raw API data
    processed = extract_data(posts)   # cleaned data

    print("Processed Data:")
    for item in processed:
        print(item)

    save_json(processed)


if __name__ == "__main__":
    main()
