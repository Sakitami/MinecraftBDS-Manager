apt update -y
apt install -y gcc g++ make flex bison xserver-xorg-dev unzip p7zip-full vim
wget https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/Debian_10/amd64/libfaudio0_20.01-0~buster_amd64.deb
apt -f -y install
dpkg -i -y libfaudio0_20.01-0~buster_amd64.deb
wget https://dl.winehq.org/wine/source/5.x/wine-5.12.tar.xz
xz -d wine-5.12.tar.xz
tar -xvf wine-5.12.tar
cd wine-5.12; ./configure --enable-win64 --without-freetype; make; make install
mkdir EZ; cd /root/EZ/; wget https://wl.lehinet.com/saki/linuxEZ1.16.0.2.zip
cd EZ; unzip *.zip; rm -rf *.zip
apt install -y screen