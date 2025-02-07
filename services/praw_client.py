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
    
    def print_last_post(self, subreddit_name):
        """Verilen subreddit'teki son 1 postu yazdırır."""
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=1):  # Son 1 post
            print(f"Başlık: {submission.title}")
            print(f"Link: {submission.url}")
            print(f"Upvote Sayısı: {submission.id}")
            print(f"Yorum Sayısı: {submission.num_comments}")
            print("-" * 50)
            self.comment_on_post(submission.id, "Great post!")
    
    def return_last_post_id(self, subreddit_name):
        """Verilen subreddit'teki son 1 postu döndürür."""
        subreddit = self.reddit.subreddit(subreddit_name)
        submission_id = subreddit.new(limit=1).__next__().id
        print(f"Link: {subreddit.new(limit=1).__next__().url}")
        return submission_id
            

# Test etmek için
if __name__ == "__main__":
    client = RedditPRAWClient()
    print(f"Bot giriş yaptı: {client.reddit.user.me()}")

# deneme yapmak icin
    # client.print_last_post("python")

# konu olarak hypnotes yazıldı
    last_post_id = client.return_last_post_id("hypnosis")
    client.comment_on_post(last_post_id, "Great post!")

