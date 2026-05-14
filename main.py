import pandas as pd
import json
import time
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('API_KEY'),
    base_url="https://api.groq.com/openai/v1"
)

def analyze_sentiment(review_text):
    """
    Отправляет текст отзыва в LLM и получает JSON с результатом.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a sentiment analysis expert. Your task is to analyze the sentiment of user reviews. Classify each review as Positive, Negative, or Neutral. You must return the result ONLY as a valid JSON object with a single key 'sentiment'. Example format: {\"sentiment\": \"Positive\"}"
                },
                {
                    "role": "user",
                    "content": f"Classify the sentiment of the following review: \"{review_text}\""
                }
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )

        result_json = json.loads(response.choices[0].message.content)
        return result_json.get('sentiment', 'Error: No sentiment field')
    except Exception as e:
        print(f"Error processing review: {e}")
        return "Error"
ELS = 10

def main():
    print("Reading data from data.csv...")
    try:
        df = pd.read_csv('data.csv', nrows=ELS)
    except FileNotFoundError:
        print("Error: data.csv not found. Please ensure the dataset file is in the same directory.")
        return

    print(f"Starting sentiment analysis for {len(df)} reviews...")
    results = []
    for index, row in df.iterrows():
        review = row['review']
        true_label = row.get('sentiment', 'Unknown')
        print(f"Processing review {index + 1}/{len(df)}: \"{review[:50]}...\"")
        
        predicted_sentiment = analyze_sentiment(review)
        results.append({
            'review': review,
            'true_sentiment': true_label,
            'predicted_sentiment': predicted_sentiment
        })
        time.sleep(0.5)

    output_filename = 'sentiment_analysis_results.json'
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    
    print(f"Analysis complete. Results saved to {output_filename}")

if __name__ == "__main__":
    main()