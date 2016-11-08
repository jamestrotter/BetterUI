/*
 * View model for OctoPrint-Betterui
 *
 * Author: James Trotter
 * License: AGPLv3
 */
$(function() {
    function BetteruiViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push([
        BetteruiViewModel,

        // e.g. loginStateViewModel, settingsViewModel, ...
        [ /* "loginStateViewModel", "settingsViewModel" */ ],

        // e.g. #settings_plugin_BetterUI, #tab_plugin_BetterUI, ...
        [ /* ... */ ]
    ]);
});
