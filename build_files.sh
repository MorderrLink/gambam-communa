
echo " BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
pip3.9 install --disable-pip-version-check --target
--upgrade -r /vercel/path0/requirements.txt
echo " BUILD END"