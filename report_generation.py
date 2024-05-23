import requests
import json

def fetch_models():
    response = requests.get("https://huggingface.co/api/models?sort=downloads")
    if response.status_code == 200:
        models = response.json()
        top_models = models[:10]  
        return top_models
    else:
        print("Failed to fetch data from Hugging Face API")
        return []

def generate_report():
    top_models = fetch_models()
    report = "Top 10 Downloaded Models on Hugging Face are:\n\n"
    for i, model in enumerate(top_models, start=1):
        report = report + f"{i}. {model['modelId']} - {model['downloads']} downloads\n"

    with open("report.txt", "w") as file:
        file.write(report)
    print("Report generated successfully!")
    print(report)

if __name__ == "__main__":
    generate_report()