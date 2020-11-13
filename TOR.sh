if [$(id -u) -ne 0]; then
	echo "You must run this script as root ya dipshit!"
	exit 1
fi
echo "INSTALLING TORGHOST..."
git clone https://github.com/SusmithKrishnan/torghost.git
cd torghost
chmod +x build.sh
./build.sh
echo "TORGHOST HAS BEEN INSTALLED! :)"
echo "type: torghost -h for any help needed!"
echo "Here are the commands: torghost -s to start || torghost -x to stop || torghost -r to get a new tor exit node"
