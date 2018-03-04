from pypy:3-slim

run echo 'deb http://cdn-fastly.deb.debian.org/debian unstable main' > /etc/apt/sources.list
#run echo 'deb http://cdn-fastly.deb.debian.org/debian testing-updates main' > /etc/apt/sources.list
 

run apt-get clean
run apt-get update
run apt-get install -y libfreetype6-dev
run apt-get install -y libpng12-dev
run pip install pydub
run pip install matplotlib
run pip install pil
run pip install numpy

run rm -rf /root/.cache
run rm -rf /root/build

run mkdir -p /root/src
add *.py /root/src/
add *.ini /root/src/

volume ["/root/src/data"]

expose 80

workdir /root/src
