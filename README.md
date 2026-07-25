# 🌍 GitHub Repo Translator

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/kullaniciadi/repo-translator/graphs/commit-activity)

**GitHub Repo Translator**, herhangi bir GitHub deposunu (repository) git kurmanıza gerek kalmadan ZIP olarak indiren, `.md` ve `.txt` dosyalarındaki belgeleri **kod bloklarına (` ``` `) ve satır içi kodlara asla dokunmadan** istediğiniz hedef dile otomatik olarak çeviren güçlü bir açık kaynak araçtır.

---

## ✨ Özellikler

* **Akıllı Kod Koruması:** Kod bloklarını (` ``` `) ve değişkenleri algılar; çeviri sırasında kodların bozunmasını önler.
* **Git Bağımlılığı Yok:** `git` aracına ihtiyaç duymadan doğrudan GitHub arşiv bağlantıları üzerinden hızlıca çalışır.
* **Çoklu Dil Desteği:** Türkçe (`tr`), İngilizce (`en`), Fransızca (`fr`), Rusça (`ru`), İspanyolca (`es`) veya Google Translate tarafından desteklenen **herhangi bir dil koduna** çeviri yapabilir.
* **Hız Sınırı Koruması (Rate-Limit):** API engellemelerine ve `429` hatalarına karşı akıllı bekleme mekanizması barındırır.
* **Mobil Uyumluluk:** Bilgisayarın yanı sıra **Pydroid 3** veya **Termux** gibi Android tabanlı Python ortamlarında da sorunsuz çalışır.
Olabildiğince Kütüphane Kullanılmıştır.
---

## 📦 Kurulum

Projeyi yerel cihazınıza klonlayın veya ZIP olarak indirin:

```bash
git clone [https://github.com/kullaniciadi/repo-translator.git](https://github.com/kullaniciadi/repo-translator.git)
cd repo-translator
Komut Dosyasını çalıştırın:
python translator.py
