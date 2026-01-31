
import os
import json
import re

LIBRARY_ROOT = r"d:\codeToGit\saki\library"
OUTPUT_FILE = r"d:\codeToGit\saki\skills\saki\knowledge\library_index.json"

def get_description(folder_path):
    """
    Tries to find a description from SKILL.md or README.md
    """
    for filename in ["SKILL.md", "README.md", "skill.md", "readme.md"]:
        file_path = os.path.join(folder_path, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read(1000) # Read first 1000 chars
                    
                    # Try to find 'description:' in frontmatter
                    match = re.search(r"description:\s*(.*)", content, re.IGNORECASE)
                    if match:
                        return match.group(1).strip()
                    
                    # Fallback: finding the first header or just text
                    lines = [l.strip() for l in content.split('\n') if l.strip()]
                    for line in lines:
                        if line.startswith("#"):
                            continue # Skip headers usually
                        if len(line) > 10:
                            return line
            except Exception:
                pass
    return "No description available."

def build_index():
    index = []
    
    print(f"Scanning {LIBRARY_ROOT}...")
    
    for root, dirs, files in os.walk(LIBRARY_ROOT):
        # We consider a directory a "Skill" if it's a leaf node or has specific files
        # Heuristic: if it has SKILL.md or README.md, it's definitely a skill.
        # Or if it has no subdirectories (leaf).
        
        rel_path = os.path.relpath(root, LIBRARY_ROOT)
        if rel_path == ".":
            continue
            
        has_docs = any(f.lower() in ["skill.md", "readme.md"] for f in files)
        is_leaf = len(dirs) == 0
        
        if has_docs or is_leaf:
            # Generate ID from path
            skill_id = rel_path.replace("\\", "/")
            
            # Generate tags from path parts
            path_parts = rel_path.split(os.sep)
            tags = []
            for part in path_parts:
                tags.extend(part.split('-'))
            
            # Remove duplicates and common words
            tags = list(set([t.lower() for t in tags if t.lower() not in ["skill", "and", "the"]]))
            
            desc = get_description(root)
            
            entry = {
                "id": skill_id,
                "desc": desc,
                "tags": tags,
                "path": rel_path # helper
            }
            index.append(entry)
            # print(f"Indexed: {skill_id}")

    print(f"Total skills indexed: {len(index)}")
    
    # Ensure dir exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"Index saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    build_index()
