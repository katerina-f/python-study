import yaml

with open("levels.yml") as levels:
    Lebels = yaml.load(levels, Loader=yaml.Loader)

print(Lebels)
