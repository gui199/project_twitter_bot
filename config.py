#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tweepy-bots/bots/config.py
import tweepy
import logging
from environs import Env
from pathlib import Path

path = Path().absolute()
env = Env()
env.read_env(path.joinpath(path, '.env'))


logger = logging.getLogger()

def create_api():
    CONSUMER_KEY=env.str('API_KEY')
    CONSUMER_SECRET=env.str('API_SECRET_KEY')
    ACCESS_TOKEN=env.str('ACCESS_KEY')
    ACCESS_TOKEN_SECRET=env.str('ACCESS_TOKEN')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api