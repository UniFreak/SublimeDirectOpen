import sublime, sublime_plugin

class DirectEditCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings('DirectEdit.sublime-settings')

        files = settings.get('files')
        options = []
        self.paths = []
        platform = sublime.platform()

        for f in files:
            options.append(f['title'])
            self.paths.append(f['location'][platform])

        self.view.window().show_quick_panel(
            options,
            on_select = self.openFile,
            )

    def openFile(self, index):
        if index != -1:
            self.view.window().open_file(self.paths[index])