import os
import re
import shutil
import urllib.request
import zipfile
import time
from deep_translator import GoogleTranslator

def translate_text(text, target_lang='tr'):
    if not text.strip() or not re.search(r'[a-zA-Z0-9]', text):
        return text
    try:
        time.sleep(0.15)
        translated = GoogleTranslator(source='en', target=target_lang).translate(text)
        return translated if translated else text
    except Exception:
        return text

def translate_markdown_content(content, target_lang='tr'):
    code_blocks = []
    
    def preserve_code(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks) - 1}__"

    pattern = r"(```[\s\S]*?```|`[^`]+`)"
    processed_content = re.sub(pattern, preserve_code, content)

    lines = processed_content.split('\n')
    translated_lines = []

    for line in lines:
        if not line.strip() or "__CODE_BLOCK_" in line or line.startswith("http://") or line.startswith("https://"):
            translated_lines.append(line)
        else:
            if line.startswith("#"):
                hashes = re.match(r"^#+", line).group(0)
                text_to_translate = line[len(hashes):].strip()
                translated_text = translate_text(text_to_translate, target_lang)
                translated_lines.append(f"{hashes} {translated_text}")
            elif line.startswith("* ") or line.startswith("- "):
                bullet = line[:2]
                text_to_translate = line[2:].strip()
                translated_text = translate_text(text_to_translate, target_lang)
                translated_lines.append(f"{bullet}{translated_text}")
            else:
                translated_text = translate_text(line, target_lang)
                translated_lines.append(translated_text)

    final_content = "\n".join(translated_lines)

    for i, block in enumerate(code_blocks):
        final_content = final_content.replace(f"__CODE_BLOCK_{i}__", block)

    return final_content

def process_repository(repo_url, target_lang='tr', output_dir="./translated_repo"):
    zip_path = "./temp_repo.zip"
    extract_dir = "./temp_extracted"

    if repo_url.endswith(".git"):
        repo_url = repo_url[:-4]
    
    repo_url = repo_url.rstrip("/")
    
    zip_urls = [
        f"{repo_url}/archive/refs/heads/main.zip",
        f"{repo_url}/archive/refs/heads/master.zip"
    ]

    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(extract_dir, exist_ok=True)

    success = False
    print("Depo internet üzerinden ZIP olarak indiriliyor...")
    for z_url in zip_urls:
        try:
            print(f"Denenen bağlantı: {z_url}")
            urllib.request.urlretrieve(z_url, zip_path)
            success = True
            break
        except Exception:
            continue

    if not success:
        print("Hata: Depo indirilemedi. URL'yi kontrol et.")
        return

    print("İndirilen arşiv dosyadan çıkarılıyor...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    
    if os.path.exists(zip_path):
        os.remove(zip_path)

    extracted_subdirs = os.listdir(extract_dir)
    if extracted_subdirs:
        actual_source = os.path.join(extract_dir, extracted_subdirs[0])
        shutil.copytree(actual_source, output_dir)
    
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)

    print(f"Dosyalar taranıyor ve metinler '{target_lang}' diline çevriliyor...")
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith((".md", ".txt")):
                file_path = os.path.join(root, file)
                print(f"Çevriliyor: {file_path}")
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    translated_content = translate_markdown_content(content, target_lang)

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(translated_content)
                except Exception as e:
                    print(f"Dosya okuma/yazma hatası ({file_path}): {e}")

    print(f"İşlem tamamlandı! Çevrilen depo şu klasörde: {output_dir}")

if __name__ == "__main__":
    url = input("GitHub Depo URL'sini girin (örn. https://github.com/kullanici/repo): ")
    lang = input("Hedef dil kodunu girin (örn. tr, es, fr, de, ru): ").strip()
    if not lang:
        lang = 'tr'
    process_repository(url, target_lang=lang)
