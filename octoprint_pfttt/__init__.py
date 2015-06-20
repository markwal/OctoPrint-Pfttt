# coding=utf-8
from __future__ import absolute_import

import requests

import octoprint.plugin

class PftttPlugin(octoprint.plugin.SettingsPlugin,
		octoprint.plugin.TemplatePlugin,
		octoprint.plugin.EventHandlerPlugin):

	def get_settings_defaults(self):
		return dict(maker_channel_key="")

	def get_template_configs(self):
		return [dict(type="settings", custom_bindings=False)]

	def on_event(self, event_name, payload):
		key = self._settings.get(['maker_channel_key']);
		if key is None or key == '':
			return
		event_body = { 'value1' : payload }
		r = requests.post("https://maker.ifttt.com/trigger/{event}/with/key/{key}".format(
			event=event_name, key=key), data=event_body)
		self._logger.info("IFTTT request returned %s" % r.text)

__plugin_name__ = "Pfttt"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = PftttPlugin()

	# global __plugin_hooks__
	# __plugin_hooks__ = {
	#    "some.octoprint.hook": __plugin_implementation__.some_hook_handler
	# }

