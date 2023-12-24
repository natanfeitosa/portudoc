registrar_lexer:
	poetry run python ./registrar_lexer.py

serve:
	poetry run mkdocs serve

instala:
	poetry install

.PHONY: registrar_lexer serve instala
