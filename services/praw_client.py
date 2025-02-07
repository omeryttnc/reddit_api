import os
import praw
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class RedditPRAWClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )

    def comment_on_post(self, post_id, comment_text):
        """Verilen post'a yorum yapar."""
        submission = self.reddit.submission(id=post_id)
        submission.reply(comment_text)
        print(f"✅ Yorum yapıldı: {comment_text}")
    
    def print_last_10_post(self, subreddit_name):
        """Verilen subreddit'teki son 1 postu yazdırır."""
        subreddit = self.reddit.subreddit(subreddit_name)
        posts=[]
        for submission in subreddit.new(limit=10):  # Son 10 post
            print(f"Başlık: {submission.title}")
            print(f"Link: {submission.url}")
            print(f"id: {submission.id}")
            print(f"Yorum Sayısı: {submission.num_comments}")
            print("-" * 50)
            posts.append((submission.id, submission.title))
        return posts
    
    def return_last_post_id_title(self, subreddit_name):
        """Verilen subreddit'teki son 1 postu döndürür."""
        subreddit = self.reddit.subreddit(subreddit_name)
        submission = next(subreddit.new(limit=1))
        return submission.id,submission.title
            

# Test etmek için
if __name__ == "__main__":
    client = RedditPRAWClient()
    print(f"Bot giriş yaptı: {client.reddit.user.me()}")


for post_id,post_title in client.print_last_10_post("python"):
    print(f"Post ID: {post_id}")
    print(f"Post Başlık: {post_title}")
    client.comment_on_post(post_id,"commnet test")
    print("-" * 50)
