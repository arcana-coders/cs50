import re

def main():
    html = input("HTML: ")
    answer = parse(html)
    print(answer)

def parse(html):
    fullhtml = r'<iframe.*?youtube\.com\/embed\/([a-zA-Z0-9_-]+)'
    match = re.search(fullhtml, html)
    if match:
        video_id = match.group(1) 
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
