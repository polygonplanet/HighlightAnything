import sublime
import sublime_plugin

REGION_KEY = "HighlightAnything_Highlight"
SETTINGS_KEY = "HighlightAnything.sublime-settings"

st3 = True if int(sublime.version()) >= 3000 else False

class HighlightAnything(sublime_plugin.EventListener):

  def highlight(self, view):
    regexp = self.load_settings().get("highlight_anything_regexp")
    if regexp:
      view.erase_regions(REGION_KEY)
      if st3:
        view.add_regions(REGION_KEY, view.find_all(regexp), "invalid", "", sublime.DRAW_OUTLINED)
      else:
        view.add_regions(REGION_KEY, view.find_all(regexp), "invalid", sublime.DRAW_OUTLINED)

  def render(self, view):
    enabled = self.load_settings().get("highlight_anything_enabled")
    if enabled:
      self.highlight(view)
    else:
      view.erase_regions(REGION_KEY)

  def load_settings(self):
    return sublime.load_settings(SETTINGS_KEY)

  # Called when the file is finished loading.
  def on_load(self, view):
    self.render(view)

  # Called after changes have been made to a view.
  def on_modified(self, view):
    self.render(view)

  # Called when a view gains input focus.
  def on_activated(self, view):
    self.render(view)
