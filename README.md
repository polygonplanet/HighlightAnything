HighlightAnything
=================

**[日本語はこちら](README.ja.md)**

Always highlight your specified character in [Sublime Text 2](http://www.sublimetext.com/2) and [3](http://www.sublimetext.com/3).

For example, this plugin can highlight the invisible ideographic space (Japanese full-width space) etc.

![Highlight the invisible ideographic space](https://raw.github.com/wiki/polygonplanet/HighlightAnything/images/highlight-anything-fullwidth-space.png)

## Installation

### 1. Add Repository

* Open **"Command Pallet"** `Ctrl + Shift + p` (`Cmd + Shift + p` in OS X)
* Select **"Package Control: Add Repository"**
* Enter this repository URL `https://github.com/polygonplanet/HighlightAnything` 

### 2. Install Package

* Open **"Command Pallet"** `Ctrl + Shift + p` (`Cmd + Shift + p` in OS X)
* Select **"Package Control: Install Package"**
* Select **HighlightAnything**

## Options

Several options are available to customize the plugin's behavior.  
Those settings are stored in a configuration file, as JSON.

Go to "`Preferences` / `Package Settings` / `HighlightAnything` / `Settings - User`" to add your custom settings.

### highlight_anything_enabled

*Default: `true`*

Whether to enable the Highlight Anything.

### highlight_anything_regexp

*Default: `"[\u3000]+"`*

A regular expression pattern to highlight any character.  
By default, highlight ideographic space (Japanese fullwidth space).

**Example:**

```javascript
{
  // Enable highlighting
  "highlight_anything_enabled": true,

  // Highlight ideographic space (Japanese full-width space)
  //  and full-width alphanumeric
  "highlight_anything_regexp": "[　０-９Ａ-Ｚａ-ｚ]+"
}
```

## Credits

This package is based the following article.

[Sublime Text 2で全角スペースをハイライト表示するプラグインを作る - Qiita](http://qiita.com/kuronekomichael/items/865e1a6605b1146d4341)

