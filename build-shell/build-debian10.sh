apt update -y
apt install gcc g++ make flex bison xserver-xorg-dev unzip p7zip-full vim
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
cd /root/BDX/
wget https://minecraft.azureedge.net/bin-win/bedrock-server-1.14.60.5.zip
unzip bedrock-server-1.14.60.5.zip
wget https://github.com/Sysca11/BedrockX-bin/blob/master/20200425_delta.7z
unzip 20200425_delta.7z
wget .zip
unzip .zip
rm -rf bedrock-server-1.14.60.5.zip 20200425_delta.7z