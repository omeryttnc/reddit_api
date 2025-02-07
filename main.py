from services.praw_client import RedditPRAWClient

def main():
    post_id = "your_post_id"  # Gerçek bir post ID kullan
    comment_text = "Bu, bot tarafından yapılan bir yorumdur!"

 
    # PRAW Kullanarak
    praw_client = RedditPRAWClient()
    praw_client.comment_on_post(post_id, comment_text)

if __name__ == "__main__":
    main()
