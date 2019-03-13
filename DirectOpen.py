import sublime, sublime_plugin

settings = {}

def plugin_loaded():
    global settings

    # if user-setting file is empty, load default setting into user-setting file
    defaultFile = 'DirectOpen ({}).sublime-settings'.format(sublime.platform())
    userFile = 'DirectOpen.sublime-settings'

    userSettings = sublime.load_settings(userFile)
    if userSettings.get('files') is None:
        default = sublime.load_settings(defaultFile)
        userSettings.set('files', default.get('files'))
        sublime.save_settings(userFile)

    settings = userSettings


class DirectOpenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        files = settings.get('files')
        options = []
        self.paths = []

        for f in files:
            options.append(f['title'])
            self.paths.append(f['location'])

        self.view.window().show_quick_panel(options, on_select = self.openFile)

    def openFile(self, index):
        if index != -1:
            self.view.window().open_file(self.paths[index])
