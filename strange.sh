if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MrMKN/Doctor_Strange-BOT.git /Doctor_Strange-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Doctor_Strange-BOT
fi
cd /Doctor_Strange-BOT
pip3 install -U -r requirements.txt
echo "Starting Κα΄α΄α΄ π±πΎππ....π₯π₯"
python3 bot.py
