import yaml
from pathlib import Path
from mkdocs.utils.yaml import get_yaml_loader

novo_mkdocs = Path('mkdocs.config.yml')

if __name__ == "__main__":
    with open(Path('mkdocs.yml'), 'rb') as fd:
        nf = yaml.load(fd, get_yaml_loader())

        if not novo_mkdocs.exists():
            novo_mkdocs.touch()
        
        novo_mkdocs.write_text(yaml.dump(nf))

