import csv
from statistics import mean, median
from unicodedata import name 
scores = []
with open("exercises/scores/scores.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        scores.append({
            "name": row["name"],
            "score":  int(row["score"])
        })

        values = [score["score"] for score in scores]
        print(f"Mean: {mean(values):.2f}")
        print(f"Median: {median(values)}")

        top = max(scores, key=lambda score: score["score"])
        bottom = min(scores, key=lambda score: score["score"])

        print(f"Top Score: {top['name']} with {top['score']}")
        print(f"Bottom Score: {bottom['name']} with {bottom['score']}")