
import os
import json
import shutil
import sys
from pathlib import Path

# Dynamic Paths
# Assumes this script is in .../skills/saki/scripts/
SCRIPT_DIR = Path(__file__).resolve().parent
SAKI_ROOT = SCRIPT_DIR.parent  # .../skills/saki/
LIBRARY_DIR = SAKI_ROOT / "library"
TEMPLATES_DIR = SAKI_ROOT / "templates"

def get_context(scanner_output):
    """
    Parses context_scanner output or simulates it.
    """
    if not scanner_output:
        return []
    # Simplified: scanner should return a list of tags
    return scanner_output.get("tags", [])

def find_best_match(tag, index_data):
    """
    Finds the best skill in the library index for a given tag.
    """
    best_match = None
    best_score = -1
    
    for item in index_data:
        # Simple keyword matching for now
        score = 0
        if tag in item["tags"]:
            score += 10
        if tag in item["id"]:
            score += 5
            
        if score > best_score and score > 0:
            best_score = score
            best_match = item
            
    return best_match

def bootstrap(target_dir):
    """
    Main bootstrap logic.
    """
    print(f"🚀 Saki Bootstrap initiated...")
    print(f"📂 Target: {target_dir}")
    
    context_scanner_path = SCRIPT_DIR / "context_scanner.py"
    if not context_scanner_path.exists():
        print(f"❌ Error: context_scanner.py not found at {context_scanner_path}")
        return

    # 1. Run Context Scanner
    # Add current dir to sys.path to import sibling script
    sys.path.append(str(SCRIPT_DIR))
    try:
        import context_scanner
        scan_result = context_scanner.scan_context(str(Path(target_dir).resolve()))
        print(f"DEBUG: Scan Result: {scan_result}") # Visual feedback
        
        # Merge stacks and frameworks into tags
        detected_tags = scan_result.get("tech_stack", []) + scan_result.get("frameworks", [])
        
        # Add package manager as a tag if known
        pm = scan_result.get("package_manager", "unknown")
        if pm != "unknown":
            detected_tags.append(pm)
            
        # Fallback if empty
        if not detected_tags:
            detected_tags = ["git"]
            
    except Exception as e:
        print(f"⚠️ Scanner failed: {e}")
        detected_tags = ["git"]
    
    print(f"🔍 Detected Context: {detected_tags}")
    
    # 2. Load Index
    index_path = SAKI_ROOT / "knowledge" / "library_index.json"
    if not index_path.exists():
         print(f"⚠️ Index not found at {index_path}. Skipping library lookup.")
         index_data = []
    else:
        with open(index_path, "r", encoding="utf-8") as f:
            index_data = json.load(f)

    # 3. Forge Skills
    generated_skills = []
    
    for tag in detected_tags:
        match = find_best_match(tag, index_data)
        if match:
            skill_id = match['id']
            skill_name = skill_id.split("/")[-1]
            source_path = LIBRARY_DIR / skill_id
            dest_path = Path(target_dir) / skill_name
            
            if dest_path.exists():
                print(f"  [Skip] {skill_name} (already exists)")
                continue
                
            print(f"  [Install] {skill_name} from {skill_id}...")
            try:
                shutil.copytree(source_path, dest_path)
                generated_skills.append(skill_name)
            except Exception as e:
                print(f"  ❌ Failed to copy {skill_name}: {e}")
                
    if not generated_skills:
        print("✨ No new skills needed (or no matches found).")
    else:
        print(f"✨ Bootstrapped {len(generated_skills)} skills: {', '.join(generated_skills)}")

if __name__ == "__main__":
    # Default to installing skills in the parent directory of 'saki'
    # e.g. if saki is in .cursor/skills/saki, install to .cursor/skills
    default_target = SAKI_ROOT.parent
    target = sys.argv[1] if len(sys.argv) > 1 else str(default_target)
    bootstrap(target)
