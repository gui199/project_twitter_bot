#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 00:09:04 2021

@author: gui
"""
import tweepy
import logging
from config import create_api
import time
from  pickle_read_save import ReadSaveDate
from datetime import datetime
import shutil
from pathlib import Path
import pandas as pd

# Configs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
FILENAME = 'since_id.bin'
FPATH='./templatesmemes/'
path = Path().absolute()
# if templatesmemes folder dont exist make one
if not path.joinpath(path, FPATH).is_dir():
    path.joinpath(path, FPATH).mkdir() 
# check if sinceid exist or make a copy of origin_id
if not  path.joinpath(path, FILENAME).is_file():
    shutil.copy2("origin_id.bin", FILENAME)

# changed pickle to csv to store values
dataset = pd.read_csv('/media/veracrypt1/estudar/Tweepy/project_twit/memelist.csv', sep=',', header=None, index_col=None )
dict1 = {dataset.loc[x][0]:dataset.loc[x][1:].to_list() for x in range(len(dataset))}


def check_mentions(api,  since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,  since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        
        #metodo para encontrar item da lista um na lista dois
        fileimg = [x for x, y in dict1.items() if any(item in "nazaré".lower().split(" ") for item in y) ]
        print(fileimg)
        if fileimg:
            logger.info(f"Answering to {tweet.user.name}")           
            api.update_with_media(FPATH+fileimg[0], status="Aqui vai.", in_reply_to_status_id=tweet.id,)            
        else:
            logger.info(f"Answering to {tweet.user.name}") 
            api.update_status(status="Eu não entendi o seu pedido.", in_reply_to_status_id=tweet.id,)
            
    return new_since_id

def main(since_id):
    api = create_api()
    since_id = since_id
    while True:
        new_since_id = check_mentions(api,  since_id)
        now = datetime.now()
        logger.info("Waiting... "+now.strftime("%H:%M:%S"))
        if new_since_id != since_id:
            ReadSaveDate.savePickle(FILENAME, new_since_id)
            since_id = new_since_id
        time.sleep(60)

if __name__ == "__main__":
    since_id0 = ReadSaveDate.readPickle(FILENAME) 
    main(since_id0)
