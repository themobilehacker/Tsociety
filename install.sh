

clear
echo '
         <Tsociety toolkit>
     <made by themobilehacker>
               ___
              |   |
             _|___|_
            /#######\ 
           |-+-###-+-|
           |#########|
            \#\___/#/
             \#####/
'
echo -n '***installing tsociety toolkit...***'
echo ''
chmod +x main.py
TSOCIETY="alias tsociety='python3 ${PWD}/main.py'"
KITCRACK="alias kitcrack='python2 ${PWD}/tools/kitcrack.py'"
HTTPSLOW="alias httpslowreq='python3 ${PWD}/tools/httpslowreq.py'"
FR="alias frain='python2 ${PWD}/tools/FR.py'"
HULK="alias frain='python2 ${PWD}/tools/DOS.py'"
echo $TSOCIETY >> ~/.bashrc
echo $TSOCIETY >> ~/.bash_profile
echo $TSOCIETY >> ~/.zshrc
echo $TSOCIETY >> ~/.zsh_profile
echo $KITCRACK >> ~/.bashrc
echo $KITCRACK >> ~/.bash_profile
echo $KITCRACK >> ~/.zshrc
echo $KITCRACK >> ~/.zsh_profile
echo $HTTPSLOW >> ~/.bashrc
echo $HTTPSLOW >> ~/.bash_profile
echo $HTTPSLOW >> ~/.zshrc
echo $HTTPSLOW >> ~/.zsh_profile
echo $FR >> ~/.bashrc
echo $FR >> ~/.bash_profile
echo $FR >> ~/.zshrc
echo $FR >> ~/.zsh_profile

pip install -r requirements.txt
pip3 install -r requirements.txt
echo '***done installing***'