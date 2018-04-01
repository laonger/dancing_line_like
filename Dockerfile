from pypy:3-slim

run echo 'deb http://mirrors.163.com/debian testing main non-free contrib' > /etc/apt/sources.list
run echo 'deb http://mirrors.163.com/debian oldstable main non-free contrib' > /etc/apt/sources.list
#run echo 'deb http://cdn-fastly.deb.debian.org/debian testing-updates main' > /etc/apt/sources.list
 

run apt-get clean
run apt-get update
run apt-get install -y apt-utils gcc
run apt-get install -y bzip2
run apt-get install -y libfreetype6-dev
run apt-get install -y libpng12-dev libjpeg-dev
run apt-get install -y zlib1g-dev zlib1g zlibc
run pip install --upgrade pip
run pip install pydub
run pip install pillow --force-reinstall --global-option="build_ext" --global-option="--disable-zlib" --global-option="--disable-jpeg"
run pip install numpy

run rm -rf /root/.cache
run rm -rf /root/build

run mkdir -p /root/src
add *.py /root/src/
#add *.ini /root/src/

volume ["/root/src/data"]

expose 80

workdir /root/src
