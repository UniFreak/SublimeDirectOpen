import sublime, sublime_plugin

class DirectOpenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        fromSettingFile = 'DirectOpen.' + sublime.platform() + '.sublime-settings'
        settings = sublime.load_settings(fromSettingFile)

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