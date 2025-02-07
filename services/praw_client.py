import os
import praw
from dotenv import load_dotenv
from enum import Enum

# .env dosyasını yükle
load_dotenv()
class RedditSort(Enum):
    RELEVANCE = "relevance"  # Varsayılan sıralama (alakaya göre)
    HOT = "hot"              # En popüler postlar
    TOP = "top"              # En çok upvote alanlar
    NEW = "new"              # En yeni postlar
    COMMENTS = "comments"    # En çok yorum alanlar

class RedditPRAWClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            username=os.getenv("REDDIT_USERNAME"),
            password=os.getenv("REDDIT_PASSWORD"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )
    # id si verilen posta yorum yapar
    def comment_on_post(self, post_id, comment_text):
        submission = self.reddit.submission(id=post_id)
        submission.reply(comment_text)
    
    #commmunitydeki son 10 postu yazdırır ve bize post id ve title döndürür
    def print_last_10_community(self, subreddit_name):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts=[]
        for submission in subreddit.new(limit=10):  # Son 10 post
            print(f"Başlık: {submission.title}")
            print(f"URL: {submission.url}")
            print(f"ID: {submission.id}")
            print(f"post icerigi: {submission.selftext}")
            print(f"Yazar: {submission.author}")
            print(f"Subreddit: {submission.subreddit}")
            print(f"Upvote Skoru: {submission.score}")
            print(f"Yorum Sayısı: {submission.num_comments}")
            print(f"Reddit Permalink: https://www.reddit.com{submission.permalink}")
            print(f"Eger varsa postun kucuk bir resmi {submission.thumbnail}")
            print(f"Post Tipi: {'Text' if submission.is_self else 'Link'}")
            print(f"NSFW İçerik mi?: {submission.over_18}")
            print("-" * 50)
            posts.append((submission.id, submission.title))
        return posts
    
    #aramasini verdigimiz son 10 postu yazdırır ve bize post id ve title döndürür
    def print_last_10_post(self, search_query):
        results = self.reddit.subreddit("all").search(search_query, limit=10, sort=RedditSort.NEW)
        posts=[]
        for submission in results:  # Son 10 post
            posts.append((submission.id, submission.title))
        return posts
    
    #verilen subredditteki son 10 postu yazdırır ve bize post id ve title döndürür
    def print_last_10_post_in_specific_community(self, subreddit_name,search_query):
        results = self.reddit.subreddit(subreddit_name).search(search_query, limit=10, sort=RedditSort.NEW)
        posts=[]
        for submission in results:  # Son 10 post
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


# for post_id,post_title in client.print_last_10_post("python"):
#     print(f"Post ID: {post_id}")
#     print(f"Post Başlık: {post_title}")
#     client.comment_on_post(post_id,"commnet test")
#     print("-" * 50)

    client.print_last_10_post("Turkish Cat")
