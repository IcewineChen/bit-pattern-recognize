#add items into requirements.txt
#form : dependency==version
#if haven't installed pip
#uncommment the command under this line
#wget "https://pypi.python.org/packages/source/p/pip/pip-1.5.4.tar.gz#md5=834b2904f92d46aaa333267fb1c922bb" --no-check-certificate

for req in $(cat requirements.txt)
do
  pip install $req
done

