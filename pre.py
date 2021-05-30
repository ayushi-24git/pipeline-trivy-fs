
cd ~
cd $(params.path-scan)
pip freeze > requirements.txt
pipenv lock
