#!/usr/bin/env python

import random
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime
from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
from stepper import feed_rat
# import stepper

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, GPIO.PUD_UP)

messages = [
    "https://www.youtube.com/watch?v=L0swUc492hU",
    "https://www.youtube.com/watch?v=3uP-kOPirdg",
    "https://www.youtube.com/watch?v=jrp2UgbYJn4",
    "https://www.youtube.com/watch?v=0t2VPBF6Kp4",
    "https://www.youtube.com/watch?v=2OOs1l8Fajc",
    "https://www.youtube.com/watch?v=1rnL1l4kN3Y",
    "http://www.nytimes.com/2015/04/26/magazine/the-rat-paths-of-new-york.html?_r=0",
    "http://www.nytimes.com/2015/09/23/nyregion/pizza-rat-spurs-debate-on-how-to-clean-up-new-yorks-subway-system.html",
    "http://www.theguardian.com/science/2015/oct/08/complex-living-brain-simulation-replicates-sensory-rat-behaviour",
    "http://www.theguardian.com/commentisfree/2015/feb/25/rats-disgusting-people-world-thrive-mutually-dependent",
    "http://articles.chicagotribune.com/2014-01-15/news/ct-rats-empathy-study-met-0114-20140115_1_rats-albino-strain",
    "Hi!",
    "http://www.theguardian.com/environment/2015/oct/06/new-species-of-hog-nosed-rat-discovered-in-indonesia",
    "https://en.wikipedia.org/wiki/Rat",
    "http://www.atlasobscura.com/articles/this-is-what-happens-when-you-link-up-four-rat-brains",
    "https://www.youtube.com/watch?v=7g2rxtWu_FM",
    "https://www.youtube.com/watch?v=-LMgkGesoVI",
    "https://www.youtube.com/watch?v=j-admRGFVNM",
    "http://www.amazon.com/Rats-Observations-History-Unwanted-Inhabitants/dp/1582344779/ref=sr_1_1?ie=UTF8&qid=1447692717&sr=8-1&keywords=rats",
    "http://www.amazon.com/Mrs-Frisby-Rats-Robert-OBrien/dp/0689710682/ref=sr_1_9?s=books&ie=UTF8&qid=1447692782&sr=1-9&keywords=rats",
    "https://www.youtube.com/watch?v=z25aP6cPMM4",
    "https://www.youtube.com/watch?v=eh62Ri60lXI"
]

def main():
    with PiCamera() as camera:
         while True:
             GPIO.wait_for_edge(14, GPIO.FALLING)
             timestamp = datetime.now().isoformat()
             photo_path = '/home/pi/tampopo_tweets/photos/%s.jpg' % timestamp
             sleep(3)
             camera.capture(photo_path)

             with open(photo_path, 'rb') as photo:
                 message = random.choice(messages)
                 twitter.update_status_with_media(status=message, media=photo)
                 feed_rat()


if __name__ == '__main__':
    main()
