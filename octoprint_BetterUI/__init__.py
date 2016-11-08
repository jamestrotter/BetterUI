# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class BetteruiPlugin(octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin,
                     octoprint.plugin.TemplatePlugin):

	##~~ SettingsPlugin mixin

	def get_settings_defaults(self):
		return dict(
			# put your plugin's default settings here
		)

	##~~ AssetPlugin mixin

	def get_assets(self):
		# Define your plugin's asset files to automatically include in the
		# core UI here.
		return dict(
			js=["js/BetterUI.js"],
			css=["css/BetterUI.css"],
			less=["less/BetterUI.less"]
		)

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			BetterUI=dict(
				displayName="Betterui Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="you",
				repo="OctoPrint-Betterui",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/you/OctoPrint-Betterui/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "Betterui"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = BetteruiPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

