import instaloader
from .config import SESSION_FILE, INSTAGRAM_USERNAME

L = instaloader.Instaloader(
    download_pictures=False,
    download_videos=False,
    download_video_thumbnails=False,
    download_comments=False,
    save_metadata=False,
)

# Load session
try:
    L.load_session_from_file(INSTAGRAM_USERNAME, SESSION_FILE)
except Exception:
    raise RuntimeError(
        "Instagram session expired. Login locally and upload new session file."
    )

def fetch_posts(keyword, limit):
    posts = []
    hashtag = instaloader.Hashtag.from_name(L.context, keyword)

    for post in hashtag.get_posts():
        posts.append(f"https://www.instagram.com/p/{post.shortcode}/")
        if len(posts) >= limit:
            break

    return posts
