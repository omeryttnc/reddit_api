from services.praw_client import RedditPRAWClient

def main():
    post_id = "your_post_id"  # Gerçek bir post ID kullan
    comment_text = "Bu, bot tarafından yapılan bir yorumdur!"

 
    # PRAW Kullanarak
    praw_client = RedditPRAWClient()
    praw_client.comment_on_post('1iqr3qj', 'it is too cute')                                              # id si verilen posta yorum yapar
    # print(praw_client.return_last_10_post_in_specificic_community_with_special_key("cat","cat"))        # belirli bir communitydeki aranan kelimeye gore
    #print(praw_client.return_last_10_post_in_all_community("cat"))                                       # all communitydeki aranan kelimeye gore son 10 postu döndürür
    # print(praw_client.return_last_post_in_community("cat"))                                             # communitydeki son postu döndürür

if __name__ == "__main__":
    main()
