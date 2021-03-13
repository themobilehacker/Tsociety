

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
DIR="alias tsociety='python3 ${PWD}/main.py'"
echo $DIR >> ~/.bashrc
echo $DIR >> ~/.bash_profile
echo $DIR >> ~/.zshrc
echo $DIR >> ~/.zsh_profile
pip install -r requirements.txt
echo '***done installing***'