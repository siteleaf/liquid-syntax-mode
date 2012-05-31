# Provide completions that match just after typing a class name

# just a test file - rolled back for now
class TagCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within liquid
        if not view.match_selector(locations[0], "text.html.liquid"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != 'collection':
            return []

        return ([
            ("collection.blah", "collection.blah"),
            ("collection.blab2", "collection.blab2")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
