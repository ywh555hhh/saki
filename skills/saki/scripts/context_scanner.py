
import os
import json
import sys
import re

def analyze_readme(root_dir):
    """
    Scans README.md for keywords to mitigate missing package files.
    """
    readme_path = os.path.join(root_dir, "README.md")
    keywords = []
    description = ""
    
    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
                description = content[:200].replace("\n", " ").strip()
                
                # Heuristic keyword extraction
                triggers = {
                    "django": "django", "flask": "flask", "fastapi": "fastapi",
                    "react": "react", "vue": "vue", "next.js": "nextjs", "nextjs": "nextjs",
                    "pytorch": "pytorch", "tensorflow": "tensorflow",
                    "docker": "docker", "kubernetes": "kubernetes",
                    "rust": "rust", "tokio": "tokio", "actix": "actix",
                    "go": "go", "gin": "gin", "chi": "chi"
                }
                
                normalized_content = content.lower()
                for key, val in triggers.items():
                    if key in normalized_content:
                        keywords.append(val)
        except Exception:
            pass
            
    return list(set(keywords)), description

def scan_context(root_dir="."):
    context = {
        "files": [],
        "tech_stack": [],
        "frameworks": [],
        "description": "",
        "package_manager": "unknown",
        "is_git_repo": os.path.isdir(os.path.join(root_dir, ".git"))
    }
    
    try:
        files = os.listdir(root_dir)
        context["files"] = [f for f in files if f not in [".git", "node_modules", ".venv", "__pycache__", "target", "dist", "build"]]
        
        # 1. Node.js
        if "package.json" in files:
            context["tech_stack"].append("node")
            try:
                with open(os.path.join(root_dir, "package.json"), "r") as f:
                    pkg = json.load(f)
                    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
                    
                    if "react" in deps: context["frameworks"].append("react")
                    if "next" in deps: context["frameworks"].append("nextjs")
                    if "vue" in deps: context["frameworks"].append("vue")
                    if "typescript" in deps: context["tech_stack"].append("typescript")
                    if "tailwindcss" in deps: context["frameworks"].append("tailwindcss")
                    
            except:
                pass
            
            if "yarn.lock" in files: context["package_manager"] = "yarn"
            elif "pnpm-lock.yaml" in files: context["package_manager"] = "pnpm"
            elif "package-lock.json" in files: context["package_manager"] = "npm"

        # 2. Python
        if any(f in files for f in ["requirements.txt", "pyproject.toml", "setup.py", "Pipfile"]):
            context["tech_stack"].append("python")
            
            # Simple content check for common frameworks
            py_indicators = {
                "django": ["manage.py", "wsgi.py"],
                "flask": ["app.py", "wsgi.py"],
                "fastapi": ["main.py"]
            }
            
            for fw, indicators in py_indicators.items():
                if any(ind in files for ind in indicators):
                    context["frameworks"].append(fw)

        # 3. Rust
        if "Cargo.toml" in files:
            context["tech_stack"].append("rust")
            try:
                with open(os.path.join(root_dir, "Cargo.toml"), "r", encoding="utf-8") as f:
                    content = f.read()
                    if "tokio" in content: context["frameworks"].append("tokio")
                    if "actix" in content: context["frameworks"].append("actix")
                    if "axum" in content: context["frameworks"].append("axum")
                    if "tauri" in content: context["frameworks"].append("tauri")
            except:
                pass

        # 4. Go
        if "go.mod" in files:
            context["tech_stack"].append("go")
            try:
                with open(os.path.join(root_dir, "go.mod"), "r", encoding="utf-8") as f:
                    content = f.read()
                    if "gin-gonic" in content: context["frameworks"].append("gin")
                    if "gofiber" in content: context["frameworks"].append("fiber")
            except:
                pass
        
        # 5. README Analysis (Augmentation)
        readme_keywords, readme_desc = analyze_readme(root_dir)
        context["description"] = readme_desc
        
        # Merge README keywords into frameworks if not already present
        for kw in readme_keywords:
            if kw not in context["frameworks"] and kw not in context["tech_stack"]:
                context["frameworks"].append(kw)

    except Exception as e:
        context["error"] = str(e)

    # De-duplicate
    context["tech_stack"] = list(set(context["tech_stack"]))
    context["frameworks"] = list(set(context["frameworks"]))
    
    return context

if __name__ == "__main__":
    result = scan_context(os.getcwd())
    print(json.dumps(result, indent=2))
