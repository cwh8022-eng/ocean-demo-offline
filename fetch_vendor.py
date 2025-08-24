# 先決條件：連網一次，下載 JS 套件到 ./vendor/，之後即可完全離線使用
import os, urllib.request

urls = {
    "tf.min.js": "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@3.21.0/dist/tf.min.js",
    "teachablemachine-image.min.js": "https://cdn.jsdelivr.net/npm/@teachablemachine/image@0.8/dist/teachablemachine-image.min.js",
}
os.makedirs("vendor", exist_ok=True)
for fn, url in urls.items():
    print(f"Downloading {fn} ...")
    urllib.request.urlretrieve(url, os.path.join("vendor", fn))
print("Done. Files saved to ./vendor/")
