import requests
import base64
import pandas as pd
import os
import Levenshtein

# Konfigurasi API LMStudio
API_URL = "http://localhost:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}

PROMPT = "What is the license plate number shown in this image? Respond only with the plate number."

# Load data label
df = pd.read_csv("labels.csv")

def calculate_cer(ground_truth, prediction):
    if not isinstance(ground_truth, str) or not isinstance(prediction, str):
        return 1.0
    return Levenshtein.distance(ground_truth.strip(), prediction.strip()) / max(len(ground_truth.strip()), 1)

results = []

for i, row in df.iterrows():
    img_path = os.path.join("test", row["image"])
    
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        continue

    with open(img_path, "rb") as img_file:
        base64_img = base64.b64encode(img_file.read()).decode("utf-8")

    payload = {
        "model": "llava-v1.5-7b",
        "messages": [
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"}},
                {"type": "text", "text": PROMPT}
            ]}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        prediction = response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error on {row['image']}: {e}")
        prediction = ""

    cer = calculate_cer(row['ground_truth'], prediction)
    results.append({
        "image": row["image"],
        "ground_truth": row["ground_truth"],
        "prediction": prediction,
        "CER_score": cer
    })

# Simpan hasil
output = pd.DataFrame(results)
output.to_csv("hasil_prediksi.csv", index=False)
print("Hasil disimpan ke hasil_prediksi.csv")
