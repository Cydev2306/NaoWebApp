#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time
import pygst
pygst.require("0.10")
import gst


def onSendMessage(bus, message,pipeline):
  t = message.type
  if t == gst.MESSAGE_ERROR:
    pipeline.set_state(gst.STATE_NULL)
    err, debug = message.parse_error()
    print "Error: %s" % err, debug

def main(nom):
	#pipeline pour le format ogg
	#PIPELINE = "filesrc location=\"test.avi\" ! decodebin ! ffmpegcolorspace ! theoraenc quality=32 ! oggmux ! filesink name=sortie"

	#pipeline pour le format mp4
	PIPELINE = "filesrc location=\"/var/www/Nao-App/public/videoNao/record.avi\" ! decodebin ! ffmpegcolorspace ! x264enc ! ffmux_mp4 ! filesink name=sortie"

	#pipeline à lancer dans le terminal pour la meme chose format ogg
	#"gst-launch filesrc location=\"test.avi\" ! decodebin ! ffmpegcolorspace ! theoraenc quality=32 ! oggmux ! filesink location=\"test.ogg\""

	FICHIER = "/home/matthieu/nao/public/videoNao/"+nom
	pipeline = gst.parse_launch(PIPELINE)
	filesink = pipeline.get_by_name("sortie")
	filesink.set_property("location", FICHIER)
	bus = pipeline.get_bus()
	bus.add_signal_watch()
	bus.connect( 'message', onSendMessage )
	pipeline.set_state(gst.STATE_PLAYING)
	time.sleep(5)

	pipeline.set_state(gst.STATE_NULL)
	print "c'est fini"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "convertVideo.py need a name file"
    else:
        nom = sys.argv[1]
        main(nom)
