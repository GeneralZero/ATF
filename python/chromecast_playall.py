#!/usr/bin/env python

import time, optparse, mimetypes
import select
from urllib.parse import urljoin, urlparse, parse_qsl
import pychromecast
from pychromecast.controllers.youtube import YouTubeController


last_status = dict()

def play_video_cc(mc, urlinfo):
	cast = None
	def callback(chromecast):
		nonlocal cast
		cast = chromecast
		stop_discovery()

	stop_discovery = pychromecast.get_chromecasts(blocking=False, callback=callback)

	while True:
		if cast:
			polltime = 0.1
			can_read, _, _ = select.select([cast.socket_client.get_socket()], [], [], polltime)
			if can_read:
				#received something on the socket, handle it with run_once()
				cast.socket_client.run_once()
			do_actions(cast, mc, urlinfo)
		else:
			print("=> Waiting for cast discovery...")
		time.sleep(1)

def do_actions(ccast, mc, urlinfo):
	update_status(ccast, mc, urlinfo)
	if last_status[ccast.device.friendly_name].media_session_id == None:
		print("Playing {} on {}".format(urlinfo, ccast.device.friendly_name))
		#print(last_status[ccast.device.friendly_name])
		play_new_file(ccast, mc, urlinfo)
		time.sleep(500)

def update_status(ccast, mc, urlinfo):
	if ccast.device.friendly_name not in last_status or last_status[ccast.device.friendly_name] != ccast.media_controller.status:
		#New Update to Chrome Cast Device
		last_status[ccast.device.friendly_name] = ccast.media_controller.status
		print("New Status [{}]: {}".format(ccast.device.friendly_name, ccast.media_controller.status))

		#Switch on new status

def play_new_file(ccast, mc, urlinfo):
	if type(mc) is YouTubeController:
		ccast.register_handler(mc)
		mc.play_video(urlinfo)

	else:
		mtype = mimetypes.guess_type(urlinfo)[0]
		mc = ccast.media_controller
		mc.play_media(urlinfo, mtype)

def find_chromecasts():
	# Ignore CEC on all devices
	pychromecast.IGNORE_CEC.append('*')  

	#Find Chrome Casts
	chromecasts = pychromecast.get_chromecasts()
	if len(chromecasts) == 0:
		print("No Chromecasts were found.")
		exit()
	return chromecasts

if __name__ == '__main__':
	parser = optparse.OptionParser(usage='usage: %prog --link [URL]')
	parser.add_option(
		"--link", help="Specify the link to be sent to the chromecasts")
	(options, args) = parser.parse_args()

	chromecasts = find_chromecasts()
	print([cast.media_controller.status for cast in chromecasts])

	if options.link is None:
		for cc in chromecasts:
			#Print out chromecasts on network
			print("Found chromecast {}".format(cc.device.friendly_name))
			cc.quit_app()

		parser.error('Specify the URL that you want to get the links from')

	else:
		link = urlparse(options.link)

		mc = None
		if link.netloc.find("youtube.com") != -1:
			query = dict(parse_qsl(link.query))
			if 'v' in query:
				mc = YouTubeController()
				urlinfo = query["v"]
			else:
				raise ValueError("Invalid video paramater")
		else:
			mc = None
			urlinfo = link.geturl()
		
		play_video_cc(mc, urlinfo)
