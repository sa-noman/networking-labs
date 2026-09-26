from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
LABS = [
    "01-static-routing",
    "02-rip-routing",
    "03-dhcp",
    "04-access-control-list",
    "05-telnet-remote-access",
    "06-subnetting",
    "07-network-troubleshooting",
]
required_headings = ["## Objective", "## Topology", "## Addressing / Planning", "## Verification", "## What I Learned"]

errors = []

if not (ROOT / "README.md").exists():
    errors.append("Missing root README.md")

for lab in LABS:
    path = ROOT / lab
    readme = path / "README.md"
    if not path.is_dir():
        errors.append(f"Missing lab directory: {lab}")
        continue
    if not readme.exists():
        errors.append(f"Missing README: {lab}/README.md")
        continue
    text = readme.read_text(encoding="utf-8")
    for heading in required_headings:
        if heading not in text:
            errors.append(f"{lab}: missing heading {heading}")

config_required = {
    "01-static-routing": ["R0.txt", "R1.txt"],
    "02-rip-routing": ["R0.txt", "R1.txt"],
    "03-dhcp": ["R0.txt"],
    "04-access-control-list": ["R0.txt"],
    "05-telnet-remote-access": ["R0.txt"],
    "07-network-troubleshooting": ["R0.txt"],
}

for lab, files in config_required.items():
    for filename in files:
        if not (ROOT / lab / "configs" / filename).exists():
            errors.append(f"Missing config: {lab}/configs/{filename}")

if errors:
    print("Validation FAILED")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Validation PASSED: {len(LABS)} labs checked.")
