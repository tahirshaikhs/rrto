# app/instagram.py
import instaloader
from .config import SESSION_FILE, INSTAGRAM_USERNAME

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_comments=False,
    save_metadata=False,
    quiet=True,
)

L.load_session_from_file(INSTAGRAM_USERNAME, SESSION_FILE)

def fetch_posts(keyword, limit=5):
    hashtag = instaloader.Hashtag.from_name(L.context, keyword)
    posts = []

    for post in hashtag.get_posts():
        posts.append(post.shortcode)
        if len(posts) >= limit:
            break

    return posts
