import shutil, sys, pygments, re, os

from pathlib import Path
from importlib import reload

pygments_path = sys.modules['pygments'].__path__[0]
pygments_path_lexers = Path(pygments_path) / 'lexers'
pygments_map_lexers = pygments_path_lexers / '_mapping.py'

portuscript_original_file_lexer = Path().absolute() / 'lexers' / 'portuscript_lexer.py'
portuscript_in_pygments = pygments_path_lexers / 'portuscript.py'

def copy_portuscript_lexer(create: bool):
    shutil.copyfile(
        portuscript_original_file_lexer,
        portuscript_in_pygments
    )
    
    if create:
        content = pygments_map_lexers.read_text()
        pygments_map_lexers.write_text(
            re.sub(r'(\})$', "'portuscript': ('pygments.lexers.portuscript', 'Portuscript', ('ptst', 'portuscript'), ('*.ptst',), ()),}", content)
        )
    
    for cache in (pygments_path_lexers / '..').glob('./**/__pycache__/**/*'):
        os.remove(str(cache.absolute()))

    reload(pygments)

create = not portuscript_in_pygments.exists()
update = not create and portuscript_original_file_lexer.stat().st_mtime > portuscript_in_pygments.stat().st_mtime
if create or update:
    copy_portuscript_lexer(create)