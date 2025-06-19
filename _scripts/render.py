import yaml
from jinja2 import Environment, FileSystemLoader

with open("cv.yaml", "r") as f:
    data = yaml.safe_load(f)

env = Environment(loader=FileSystemLoader("_scripts"))
template = env.get_template("template.html")

output = template.render(**data)

with open("cv.html", "w") as f:
    f.write(output)

print("✅ Rendered cv.html")
