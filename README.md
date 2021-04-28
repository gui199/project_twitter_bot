# Twitter Bot Meme Reply

Esse projeto tem o  objetivo de criar um bot do twitter para enviar aos usuários a imagem/reaction do meme desejado.
---
## Esse trabalho teve como base:  
[RealPython Twitter Bot ](https://realpython.com/twitter-bot-python-tweepy/)
---
## Imagem:  
![Imagem from twitter](memereply.png)
---
## Rodando o aplicativo  
Crie um arquivo `.env` com as variaveis de ambiente requisitadas da API(key e tokens) do Twitter.  
```bash
#git clone repo
git clone https://thisprojectgit/project_twitter_bot
#change directory
cd project_twitter_bot/
#create virtual enviroment
virtualenv -p python3 env
#active venv
source env/bin/activate
#install requiriments in venv
pip install -r requirements.txt
#rename the binary
mv origin_id.bin since_id.bin 
#ajust the images/meme you have and put into 'templatesmemes/'
mkdir templatesmemes
#ajust the csv to it
memelist.csv
#create .env and ajust it
nano env_example
cp env_example .env
#run
$ python memereply.py
```
---
## Site Twitter:  
[https://twitter.com/meme_reply_bot](https://twitter.com/meme_reply_bot)
