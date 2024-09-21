#!/bin/bash

bold() {
  echo -e "\e[1m$1\e[0m\n"
}

underline() {
    echo -e "\e[4m$1\e[0m"
}
  
bold_underline() {
    echo -e "\e[1m\e[4m$1\e[0m"
}
  
yellow() {
    echo -e "\e[33m$$1\e[0m"
}
  
bf_u_y() {
    echo -e "\e[1m\e[4m\e[33m$1\e[0m"
}

# Get the distributor information
distribution=$(lsb_release -a 2>/dev/null | grep Distributor | awk '{print $3}')

# Determine the package manager based on the distributor
case "$distribution" in
    Debian|Ubuntu)
        packagemanager="apt"
        ;;
    NobaraLinux)
        packagemanager="dnf"
        ;;
    #Arch) TODO: what is it called in arch and other distros?
    #    packagemanager="sudo pacman -S --noconfirm"
    #    ;;
    *)
        echo "Unsupported Linux distribution: $distribution"
        echo "Supported distributions are Debian, Ubuntu, NobaraLinux."
        exit 1
        ;;
esac

# Print the message with colored words
echo "Gefundene aktive Linux Distribution: $(bf_u_y $distribution)"

# install dependencies
echo "Führe Befehl aus:"
echo "$bold sudo $packagemanager install -y python3-pip python3-venv openjdk-11-jdk pdftk libxcb-cursor0 python3-lxml"
echo "Bitte gib dein Passwort ein, um die für Sephrasto erforderlichen Pakete zu installieren:"

sudo $packagemanager install python3-pip python3-venv openjdk-11-jdk pdftk libxcb-cursor0 python3-lxml

# download code from latest sephrasto release
# git clone https://github.com/Aeolitus/Sephrasto.git
echo "Lade Sephrasto (latest release)..."
curl -s https://api.github.com/repos/Aeolitus/Sephrasto/releases/latest \
| grep "tarball_url" \
| cut -d '"' -f 4 \
| xargs curl -L -o sephrasto_latest.tar.gz

# extract sephrasto
echo "Entpacke Sephrasto..."
mkdir -p Sephrasto
tar -xzf sephrasto_latest.tar.gz -C Sephrasto --strip-components=1
rm sephrasto_latest.tar.gz

INSTALL=$(pwd)/Sephrasto

# create and install virtual environment
# mkdir -p "$INSTALL/.venv"
echo "Installiere virtuelle Umgebung..."
python3 -m venv "$INSTALL/.venv"
source "$INSTALL/.venv/bin/activate"
pip install -r $INSTALL/requirements.txt


# Create desktop entry file (starter)
echo "Erstelle Starter..."
cat <<EOL > Sephrasto.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Sephrasto
Description=Heldengenerator für Ilaris
Comment=Heldengenerator für Ilaris
Exec=$INSTALL/.venv/bin/python $INSTALL/src/Sephrasto/Sephrasto.py
Icon=$INSTALL/src/Sephrasto/icon_large.png
Type=Application
Categories=Games;
EOL

# make desktop entry executable and found by desktop environemnt
chmod +x Sephrasto.desktop
mkdir -p ~/.local/share/applications/
mv Sephrasto.desktop ~/.local/share/applications/

echo ""
echo "Installation abgeschlossen."
echo ""
echo "Sephrasto wurde im Ordner $INSTALL installiert."
echo "Zum Updaten lösche diesen Ordner und führe den Installationsbefehl erneut aus."
echo "Helden, Regeln und Plugins liegen in separaten Ordnern und bleiben erhalten."
echo "Ein Starter wurde in ~/.local/share/applications/Sephrasto.desktop erstellt."
echo "Sephrasto kann nun über das Startmenü gestartet werden."