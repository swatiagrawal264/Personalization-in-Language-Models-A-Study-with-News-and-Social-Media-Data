import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load FLAN-T5
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# Function to categorize an article
def categorize_article(article):
    prompt = f"Which category does this article relate to among the following categories? Just answer with the category name without further explanation. categories: [women, religion, politics, style & beauty, entertainment, culture & arts, sports, science & technology, travel, business, crime, education, healthy living, parents, food & drink] article: {article}"
    inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
    output_sequences = model.generate(input_ids=inputs["input_ids"], max_length=50, num_return_sequences=1)
    return tokenizer.decode(output_sequences[0], skip_special_tokens=True)

# Load your dataset
with open("/Users/medhagoel/Downloads/Compsci646/Final_project/dev_questions.json", "r") as file:
    dataset = json.load(file)

output_data = []

# Loop through the dataset and categorize each article
for item in dataset:
    article_text = item["input"]
    predicted_category = categorize_article(article_text)
    print(f"Article ID: {item['id']}, Predicted Category: {predicted_category}")



output_file_path = "/Users/medhagoel/Downloads/Compsci646/Final_project/predicted_categories_tweet.json"
with open(output_file_path, "w") as output_file:
    json.dump(output_data, output_file, indent=2)  # indent=2 for pretty formatting
    print(f"Predicted categories saved to {output_file_path}")


