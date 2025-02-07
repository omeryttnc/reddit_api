https://www.reddit.com/prefs/apps

REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_USER_AGENT=MyRedditBot/0.1 by MyRedditBot

📌 1. Reddit API’ye Kayıt Ol ve Uygulama Oluştur
Öncelikle Reddit’in API hizmetlerini kullanabilmek için Reddit'te bir uygulama oluşturman gerekiyor.

🔹 Adım 1: Reddit Developer Portal'a Git
https://www.reddit.com/prefs/apps

Tarayıcında Reddit Apps sayfasını aç.
Eğer giriş yapmadıysan, Reddit hesabınla giriş yap.
🔹 Adım 2: Yeni Uygulama (Bot) Oluştur
1️⃣ Sayfanın en altına git ve "Developed Applications" bölümünde "Create App" veya "Create another app" butonuna tıkla.
2️⃣ Açılan formda şu bilgileri doldur:

Name → Uygulamanın adı (Örneğin: RedditBot)
App Type → Script seç
Description → (Boş bırakabilirsin)
About URL → (Boş bırakabilirsin)
Permissions → "script" seçtiğimiz için otomatik ayarlanıyor
Redirect URI → http://localhost:8080 yaz (Önemli! Reddit API bu URL'yi zorunlu kılıyor)
✅ Formu doldurduktan sonra "Create App" butonuna bas.

🔹 Adım 3: API Kimliklerini Al
Uygulaman oluşturulduktan sonra, sayfada aşağıdaki bilgileri bulacaksın:

Client ID → Uygulamanın adının altında yazan alfanumerik kod (Örnek: XxYyZzAAbbCc)
Client Secret → "secret" yazan uzun bir gizli anahtar (Örnek: a1b2c3d4e5f6g7h8)
Bu bilgileri bir yere kaydet çünkü birazdan .env dosyasına ekleyeceğiz.
