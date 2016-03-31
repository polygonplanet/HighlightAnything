HighlightAnything
=================

**[README (English)](README.md)**

指定した文字を常に強調(アウトライン)表示する [Sublime Text 2](http://www.sublimetext.com/2) と [3](http://www.sublimetext.com/3) 用のプラグインです。

例えば、全角スペースなどの強調表示が可能です。

![全角スペースの強調表示の例](https://raw.github.com/wiki/polygonplanet/HighlightAnything/images/highlight-anything-fullwidth-space.png)

## 導入

### 1. レポジトリの追加

* **"コマンドパレット (Command Pallet)"** を開きます。 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (OSX の場合 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd>) で開けます。
* **"Package Control: Add Repository"** を選択します。
* 下のほうにでる入力欄に、このレポジトリの URL `https://github.com/polygonplanet/HighlightAnything` を入力し決定します。

### 2. パッケージのインストール

* **"コマンドパレット (Command Pallet)"** を開きます。 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> (OSX の場合 <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd>) で開けます。
* **"Package Control: Install Package"** を選択します。
* **HighlightAnything** を選択するとインストールされます。

## オプション

いくつかのオプションがプラグインの動作をカスタマイズするために利用可能です。  
これらの設定は、JSON として設定ファイルに保存されます。

"`Preferences` / `Package Settings` / `HighlightAnything` / `Settings - User`" から設定できます。

### highlight_anything_enabled

*Default: `true`*

強調表示を有効にするかどうか。  
`true` にすると有効になり、`false` にすると無効になります。

### highlight_anything_regexp

*Default: `"[\u3000]+"`*

任意の文字を強調表示するための正規表現パターン。  
デフォルトでは、全角スペースを強調表示します。

**例:**

```javascript
{
  // 強調表示を有効にする
  "highlight_anything_enabled": true,

  // 全角スペースと全角英数字を強調表示
  "highlight_anything_regexp": "[　０-９Ａ-Ｚａ-ｚ]+"
}
```

## クレジット

このパッケージは以下の記事を参考にしています。

[Sublime Text 2で全角スペースをハイライト表示するプラグインを作る - Qiita](http://qiita.com/kuronekomichael/items/865e1a6605b1146d4341)

