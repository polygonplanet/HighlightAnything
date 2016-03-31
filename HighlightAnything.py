import sublime
import sublime_plugin

REGION_KEY = "HighlightAnything_Highlight"
SETTINGS_KEY = "HighlightAnything.sublime-settings"

DEFAULT_ENABLED = True
DEFAULT_REGEXP = "[\u3000]+"
DEFAULT_MAX_FILE_SIZE = 1048576
DEFAULT_DELAY = 200

st3 = True if int(sublime.version()) >= 3000 else False


class Preferences:
  def load(self, settings):
    self.enabled = bool(settings.get("highlight_anything_enabled", DEFAULT_ENABLED))
    self.regexp = settings.get("highlight_anything_regexp", DEFAULT_REGEXP)
    self.max_size = settings.get("highlight_anything_max_file_size", DEFAULT_MAX_FILE_SIZE)
    self.delay = settings.get("highlight_anything_delay", DEFAULT_DELAY)

Pref = Preferences()


def plugin_loaded():
  settings = sublime.load_settings(SETTINGS_KEY)
  Pref.load(settings)
  settings.add_on_change("reload", lambda: Pref.load(settings))


def highlight(view):
  if view.size() > Pref.max_size:
    return

  if not Pref.regexp:
    return

  view.erase_regions(REGION_KEY)
  if st3:
    view.add_regions(REGION_KEY, view.find_all(Pref.regexp), "invalid", "", sublime.DRAW_OUTLINED)
  else:
    view.add_regions(REGION_KEY, view.find_all(Pref.regexp), "invalid", sublime.DRAW_OUTLINED)


class HighlightAnything(sublime_plugin.EventListener):
  def __init__(self):
    self.pending = 0

  def render(self, view):
    self.pending = self.pending - 1
    if self.pending > 0:
      return
    highlight(view)

  def on_modified(self, view):
    if Pref.enabled:
      self.pending = self.pending + 1
      if self.pending == 1:
        sublime.set_timeout(lambda: self.render(view), 1)
      else:
        sublime.set_timeout(lambda: self.render(view), Pref.delay)

  def on_activated(self, view):
    if Pref.enabled:
      highlight(view)

  def on_load(self, view):
    if Pref.enabled:
      highlight(view)


if not st3:
  plugin_loaded()
