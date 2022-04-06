#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**<u>Yönetici Komutları:</u>**

**c** stands for channel play.

/pause or /cpause - Çalan müziği duraklat.
/resume or /cresume- Duraklatılan müziği devam ettir.
/mute or /cmute- Çalan müziğin sesini kapatın.
/unmute or /cunmute- Sessiz müziğin sesini açın.
/skip or /cskip- Çalmakta olan müziği atla.
/stop or /cstop- Çalan müziği durdur.
/shuffle or /cshuffle- Sıraya alınmış çalma listesini rastgele karıştırır.
/seek or /cseek - İleri Müziği sürenize göre arayın
/seekback or /cseekback - Geriye Müziği sürenize göre arayın
/restart - Sohbetiniz için botu yeniden başlatın .


✅<u>**Spesifik Atlama:**</u>
/Atla or /catla [Number(example: 3)] 
    - Müziği belirtilen sıraya alınmış numaraya atlar. Örnek: /atla 3, müziği sıraya alınan üçüncü müziğe atlar ve sıradaki 1 ve 2 müziği yok sayar.

✅<u>**Döngü Oynat:**</u>
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - Etkinleştirildiğinde, bot sesli sohbette çalmakta olan müziği 1-10 kez döngüye alır. Varsayılan olarak 10 kez.

✅<u>**Yetkili Kullanıcılar:**</u>
Yetkilendirme Kullanıcıları, sohbetinizde yönetici hakları olmadan yönetici komutlarını kullanabilir.

/auth [Username] - Grubun YETKİLİ LİSTESİ'ne bir kullanıcı ekleyin.
/unauth [Username] - Bir kullanıcıyı grubun YETKİLİ LISTESİ'inden kaldırın.
/authusers - Grubun YETKİLİ LİSTESİ'ni kontrol edin."""


HELP_2 = """✅<u>**Komutları Oynat:**</u>

Available Commands = play , vplay , cplay ,oynat

ForcePlay Commands = playforce , vplayforce , cplayforce

**c** kanal oynatma anlamına gelir.
**v** video oynatma anlamına gelir.
**force** kuvvet oyunu anlamına gelir.

/play veya /vplay veya /cplay veya /oynat - Bot, verilen sorguyu sesli sohbette veya Sesli sohbetlerde Canlı bağlantı akışında oynatmaya başlar.

/playforce or /vplayforce or /cplayforce -  **Force Play**, sesli sohbette çalmakta olan parçayı durdurur ve sırayı bozmadan/temizlemeden aranan parçayı anında çalmaya başlar.

/channelplay [Sohbet kullanıcı adı veya kimliği] veya [Devre dışı bırak] - Kanalı bir gruba bağlayın ve grubunuzdan kanalın sesli sohbetinde müzik akışı yapın.


✅**<u>Bot'un Sunucu Oynatma Listeleri:</u>**
/playlist  - Sunucularda Kaydedilmiş Oynatma Listenizi Kontrol Edin.
/deleteplaylist - Çalma listenizde kayıtlı tüm müzikleri silin
/play  - Sunuculardan Kaydedilmiş Oynatma Listenizi oynatmaya başlayın."""


HELP_3 = """✅<u>**Bot Komutları:**</u>

/stats - En İyi 10 Parçayı Alın Global İstatistikler, Botun En İyi 10 Kullanıcısı, Botta En İyi 10 Sohbet, Sohbette Oynanan En İyi 10 vb..

/sudolist - Yukki Music Bot'un Sudo Kullanıcılarını Kontrol Edin

/lyrics [Müzik Adı] - Web'de belirli bir Müziğin Sözlerini arar.

/song [Parça Adı] veya [YT Bağlantısı] - youtube'dan herhangi bir parçayı mp3 veya mp4 formatında indirin.

/player -  Etkileşimli bir Oynatma Paneli edinin.

**c** kanal oynatma anlamına gelir.

/queue or /cqueue- Müzik Sıra Listesini Kontrol Edin."""

HELP_4 = """✅<u>**Ekstra Komutlar:**</u>
/start - Müzik Botunu Başlatın.
/help  - Komutların ayrıntılı açıklamalarını içeren Komutlar Yardımcı Menüsü Alın.
/ping- Bot'a ping atın ve Bot'un Ram, Cpu vb istatistiklerini kontrol edin.

✅<u>**Grup Ayarları:**</u>
/settings - Satır içi düğmelerle eksiksiz bir grubun ayarlarını alın

🔗 **Ayarlardaki Seçenekler:**

1️⃣ Sesli sohbette yayınlamak istediğiniz **Ses Kalitesini** ayarlayabilirsiniz.

2️⃣ Sesli sohbette yayınlamak istediğiniz **Video Kalitesini** ayarlayabilirsiniz.

3️⃣ **Yetkilendirme Kullanıcıları**:- Yönetici komutları modunu buradan herkese veya yalnızca yöneticilere değiştirebilirsiniz. Herkes, grubunuzdaki herkes yönetici komutlarını kullanabilecekse (/atla,/bitir vb. gibi))

4️⃣ **Temiz Mod:** Etkinleştirildiğinde, sohbetinizin temiz ve iyi kalmasını sağlamak için 5 dakika sonra botun mesajlarını grubunuzdan siler.

5️⃣ **Komut Temizleme** : Etkinleştirildiğinde, Bot yürütülen komutları (/oynat, /durdur, /shuffle, /bitir vb.) hemen siler..

6️⃣ **Oynatma ayarları:**

/playmode - Grubunuzun oyun ayarlarını yapabileceğiniz düğmeler içeren eksiksiz bir oyun ayarları paneli edinin. 

<u>Oynatma modundaki seçenekler:</u>

1️⃣ **Arama Modu** [Doğrudan veya Satır İçi] - Siz /oynat modu verirken arama modunuzu değiştirir. 

2️⃣ **Yönetici Komutları** [Herkes veya Yöneticiler] - Grubunuzda bulunan herkes, herkes yönetici komutlarını kullanabilir (/atla, /bitir vb. gibi))

3️⃣ **Oynat Türü** [Herkes veya Yöneticiler] - Yöneticilerse, yalnızca grupta bulunan yöneticiler sesli sohbette müzik çalabilir."""

HELP_5 = """🔰**<u>SUDO KULLANICILARINI EKLE VE KALDIR :</u>**
/addsudo [Kullanıcı adı veya bir kullanıcıya yanıt]
/delsudo [Kullanıcı adı veya bir kullanıcıya yanıt]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Botunuzu yeniden başlatın. 
/update - Botu Güncelle.
/speedtest - Sunucu hızlarını kontrol edin
/maintenance [enable / disable] 
/logger [enable / disable] - Bot, logger grubunda aranan sorguları günlüğe kaydeder.
/get_log [Number of Lines] - Heroku veya vps'den botunuzun günlüğünü alın. Her ikisi için de çalışır.
/autoend [enable|disable] - Hiç kimse dinlemiyorsa 3 dakika sonra Otomatik akışı sonlandır seçeneğini etkinleştirin.

📈**<u>STATS KOMUTLAR:</u>**
/activevoice - Botta aktif sesli sohbetleri kontrol edin.
/activevideo - Botta aktif görüntülü görüşmeleri kontrol edin.
/stats - Bot İstatistiklerini Kontrol Edin

⚠️**<u>KARA LİSTE SOHBET FONKSİYONU:</u>**
/blacklistchat [CHAT_ID] - Music Bot kullanarak herhangi bir sohbeti kara listeye alın
/whitelistchat [CHAT_ID] - Music Bot'u kullanarak kara listeye alınmış herhangi bir sohbeti beyaz listeye alın
/blacklistedchat - Kara listeye alınan tüm sohbetleri kontrol edin.

👤**<u>ENGELLİ FONKSİYON:</u>**
/block [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcının bot komutlarını kullanmasını engeller.
/unblock [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un Engellenenler Listesinden kaldır.
/blockedusers - Engellenen Kullanıcı Listelerini Kontrol Edin

👤**<u>GBAN FONKSİYONU:</u>**
/gban [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı botun sunduğu sohbetten Gban ve botunuzu kullanmasını durdurun.
/ungban [Kullanıcı adı veya bir kullanıcıyı yanıtla] - Bir kullanıcıyı Bot'un gbanlı Listesinden çıkarın ve onun botunuzu kullanmasına izin verin
/gbannedusers - Gbanlı Kullanıcı Listelerini Kontrol Edin

🎥**<u>VİDEO ÇAĞRISI İŞLEVİ:</u>**
/set_video_limit [Sohbet Sayısı] - Bir seferde Görüntülü Aramalar için izin verilen maksimum Sohbet Sayısını ayarlayın. Varsayılan olarak 3 sohbet.
/videomode [download|m3u8] - İndirme modu etkinleştirilirse Bot, videoları M3u8 biçiminde oynatmak yerine indirecektir. Varsayılan olarak M3u8'e. Herhangi bir sorgu m3u8 modunda oynatılmadığında indirme modunu kullanabilirsiniz..

⚡️**<u>ÖZEL BOT FONKSİYONU:</u>**
/authorize [CHAT_ID] - Botunuzu kullanmak için bir sohbete izin verin.
/unauthorize [CHAT_ID] - Bir sohbetin botunuzu kullanmasına izin vermeyin.
/authorized - Botunuzun izin verilen tüm sohbetlerini kontrol edin.

🌐**<u>YAYIN FONKSİYONU:</u>**
/reklam [Mesaj veya Bir Mesaja Cevap Ver] - Herhangi bir mesajı Bot'un Sunulan Sohbetlerine yayınlayın.

<u>yayın seçenekleri:</u>
**-pin** : Bu, mesajınızı sabitleyecektir 
**-pinloud** : Bu, mesajınızı yüksek sesli bildirimle sabitleyecektir
**-user** : Bu, mesajınızı botunuzu başlatan kullanıcılara yayınlayacaktır..
**-assistant** : Bu, mesajınızı botunuzun asistan hesabından yayınlayacaktır..
**-nobot** : Bu, botunuzu mesaj yayınlamamaya zorlar

**Örnek:** `/reklam -user -assistant -pin Merhaba Test'

"""
