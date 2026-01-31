
import json
import sys
import os

INDEX_FILE = r"d:\codeToGit\saki\skills\saki\knowledge\library_index.json"

def search(query):
    if not os.path.exists(INDEX_FILE):
        print(f"Error: Index file not found at {INDEX_FILE}")
        return

    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index = json.load(f)
    except Exception as e:
        print(f"Error loading index: {e}")
        return

    keywords = query.lower().split()
    results = []

    for item in index:
        score = 0
        text = (item.get("id", "") + " " + item.get("desc", "") + " " + " ".join(item.get("tags", []))).lower()
        
        matches = 0
        for kw in keywords:
            if kw in text:
                matches += 1
                # Higher score for ID match
                if kw in item.get("id", "").lower():
                    score += 3
                # Higher score for tag match
                if kw in item.get("tags", []):
                    score += 2
                else:
                    score += 1
        
        if matches > 0:
            results.append((score, item))

    # Sort by score descending
    results.sort(key=lambda x: x[0], reverse=True)

    # Return top 5
    print(json.dumps([r[1] for r in results[:5]], indent=2, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_index.py <query>")
    else:
        search(" ".join(sys.argv[1:]))
