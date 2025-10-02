import subprocess
import datetime

def run_tests():
    try:
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        subprocess.check_call(["pytest", "-q"])
        
        return "✅ " + fecha_hora + " Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ " + fecha_hora + " Tests fallidos"

def update_readme(status: str):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status + "\n")
            
    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def update_report(status: str):
    with open("report.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        new_lines.append(line)
    
    new_lines.append(status + "\n")

    with open("report.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
    update_report(status)
