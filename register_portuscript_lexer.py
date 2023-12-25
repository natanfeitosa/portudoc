import shutil, sys, pygments, re

from pathlib import Path
from importlib import reload
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

pygments_path = sys.modules["pygments"].__path__[0]
pygments_path_lexers = Path(pygments_path) / "lexers"
pygments_map_lexers = pygments_path_lexers / "_mapping.py"

portuscript_original_file_lexer = (
    Path(__file__).absolute().parent / "lexers" / "portuscript_lexer.py"
)
portuscript_in_pygments = pygments_path_lexers / "portuscript.py"


def copy_portuscript_lexer():
    shutil.copyfile(portuscript_original_file_lexer, portuscript_in_pygments)

    try:
        get_lexer_by_name("ptst")
    except ClassNotFound:
        content = pygments_map_lexers.read_text()
        pygments_map_lexers.write_text(
            re.sub(
                r"(\})$",
                "'portuscript': ('pygments.lexers.portuscript', 'Portuscript', ('ptst', 'portuscript'), ('*.ptst',), ()),}",
                content,
            )
        )
    except Exception as e:
        print("[erro]: %s" % e)

    for cache in (pygments_path_lexers / "..").glob("./**/__pycache__/"):
        shutil.rmtree(cache.absolute())

    reload(pygments)


create = not portuscript_in_pygments.exists()
update = (
    not create
    and portuscript_original_file_lexer.stat().st_mtime
    > portuscript_in_pygments.stat().st_mtime
)
if create or update:
    copy_portuscript_lexer()
