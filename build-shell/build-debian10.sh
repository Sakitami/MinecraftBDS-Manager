apt update -y
apt install -y gcc g++ make flex bison xserver-xorg-dev unzip p7zip-full vim
wget https://download.opensuse.org/repositories/Emulators:/Wine:/Debian/Debian_10/amd64/libfaudio0_20.01-0~buster_amd64.deb
dpkg -i libfaudio0_20.01-0~buster_amd64.deb
apt -f install
dpkg -i libfaudio0_20.01-0~buster_amd64.deb
wget https://dl.winehq.org/wine/source/5.x/wine-5.7.tar.xz
xz -d wine-5.7.tar.xz
tar -xvf wine-5.7.tar
cd wine-5.7
./configure --enable-win64 --without-freetype
make
Wine build complete
make install
cd /root/EZ/
wget https://github.com/Sakitami/MinecraftBDS-Manager/blob/master/Server/linuxbedrock-1.14.60.zip
unzip *.zip
rm -rf *.zip
apt install -y screen
screen -R EZ
wine EZ.bat