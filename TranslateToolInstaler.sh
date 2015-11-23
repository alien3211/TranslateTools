#!/bin/bash

if [ -e /local/TranslateTool ] 
then
    rm -rf /local/TranslateTool
fi

if [ ! -e ~/.cshrc.user ] 
then
   touch ~/.cshrc.user 
fi

if [ ! -e ~/.bashrc ] 
then
   touch ~/.bashrc
fi

if [ ! -e ~/.bash_profile ] 
then
   touch ~/.bash_profile
fi

export ftp_proxy="172.23.0.100:8080" 
export http_proxy="172.23.0.100:8080" 
export https_proxy="172.23.0.100:8080" 

git clone https://github.com/alien3211/TranslateTools.git /local/TranslateTool

grep -i 'TranslateTool' ~/.bashrc || echo 'alias TranslateTool="python /local/TranslateTool/translateTool.py"
export ftp_proxy="172.23.0.100:8080" 
export http_proxy="172.23.0.100:8080" 
export https_proxy="172.23.0.100:8080" 
' >> ~/.bashrc

grep -i 'TranslateTool' ~/.cshrc.user || echo 'alias TranslateTool "python /local/TranslateTool/translateTool.py"
export ftp_proxy="172.23.0.100:8080" 
export http_proxy="172.23.0.100:8080" 
export https_proxy="172.23.0.100:8080" 
' >> ~/.cshrc.user

grep -i 'TranslateTool' ~/.bash_profile || echo 'cd /local/TranslateTool/
export ftp_proxy="172.23.0.100:8080" 
export http_proxy="172.23.0.100:8080" 
export https_proxy="172.23.0.100:8080" 
git clean -f -x
git stash
git pull
cd -' >> ~/.bash_profile
