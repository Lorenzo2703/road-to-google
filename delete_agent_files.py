import os

files_to_delete = [
    r"role-specific/adk-preparation.md",
    r"role-specific/agent-engineering.md",
    r"role-specific/portfolio-projects.md",
    r"role-specific/enterprise-ai.md",
    r"system-design/agent-systems.md"
]

for f in files_to_delete:
    if os.path.exists(f):
        try:
            os.remove(f)
            print(f"Successfully deleted {f}")
        except Exception as e:
            print(f"Error deleting {f}: {e}")
    else:
        print(f"File does not exist: {f}")
