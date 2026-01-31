
/**
 * Saki Context Scanner (Node.js Fallback)
 * Zero-dependency script to analyze project context.
 */
const fs = require('fs');
const path = require('path');

function scanContext(rootDir = process.cwd()) {
    const context = {
        files: [],
        tech_stack: [],
        frameworks: [],
        description: "",
        package_manager: "unknown",
        is_git_repo: fs.existsSync(path.join(rootDir, ".git"))
    };

    try {
        const files = fs.readdirSync(rootDir);
        const ignored = [".git", "node_modules", ".venv", "__pycache__", "target", "dist", "build"];
        context.files = files.filter(f => !ignored.includes(f));

        // 1. Node.js
        if (files.includes("package.json")) {
            context.tech_stack.push("node");
            try {
                const pkgPath = path.join(rootDir, "package.json");
                const pkg = JSON.parse(fs.readFileSync(pkgPath, 'utf8'));
                const deps = { ...pkg.dependencies, ...pkg.devDependencies };

                if (deps["react"]) context.frameworks.push("react");
                if (deps["next"]) context.frameworks.push("nextjs");
                if (deps["vue"]) context.frameworks.push("vue");
                if (deps["typescript"]) context.tech_stack.push("typescript");
                if (deps["tailwindcss"]) context.frameworks.push("tailwindcss");
            } catch (e) {}

            if (files.includes("yarn.lock")) context.package_manager = "yarn";
            else if (files.includes("pnpm-lock.yaml")) context.package_manager = "pnpm";
            else if (files.includes("package-lock.json")) context.package_manager = "npm";
        }

        // 2. Python
        const pyFiles = ["requirements.txt", "pyproject.toml", "setup.py", "Pipfile"];
        if (files.some(f => pyFiles.includes(f))) {
            context.tech_stack.push("python");
            if (files.includes("manage.py")) context.frameworks.push("django");
            if (files.includes("app.py")) context.frameworks.push("flask"); // Simple heuristic
            if (files.includes("main.py")) context.frameworks.push("fastapi"); // Simple heuristic
        }

        // 3. Rust
        if (files.includes("Cargo.toml")) {
            context.tech_stack.push("rust");
            try {
                const cargo = fs.readFileSync(path.join(rootDir, "Cargo.toml"), 'utf8');
                if (cargo.includes("tokio")) context.frameworks.push("tokio");
                if (cargo.includes("actix")) context.frameworks.push("actix");
                if (cargo.includes("tauri")) context.frameworks.push("tauri");
            } catch (e) {}
        }
        
        // 4. README Analysis
        if (files.includes("README.md")) {
            try {
                const readme = fs.readFileSync(path.join(rootDir, "README.md"), 'utf8');
                 context.description = readme.slice(0, 200).replace(/\n/g, " ").trim();
            } catch (e) {}
        }

    } catch (e) {
        context.error = e.message;
    }

    // Deduplicate
    context.tech_stack = [...new Set(context.tech_stack)];
    context.frameworks = [...new Set(context.frameworks)];

    console.log(JSON.stringify(context, null, 2));
}

// Run
scanContext();
