## (Siteleaf) Liquid support for Sublime Text

This is a fork of the [shopify-liquid](https://bitbucket.org/granteagon/shopify-liquid) syntax, which was based off of the Djaniero package for Django.

## Installation

1. Clone this repo
2. Put the contents of this repo directly inside:

 - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
 - Windows: %APPDATA%/Sublime Text 2/Packages/
 - Linux: ~/.config/sublime-text-2/Packages

Or use PackageControl.

You might need to switch to the syntax mode. (`shift + cmd + p`, search for Liquid, "Set Syntax: HTML (Liquid)")

## Autocomplete

To show the autocomplete suggestions, your cursor must be within a tag markup or output marker wrapper (`{% %}` or `{{ }}`)

Then press `ctrl + spacebar`, or add the following to your user settings file:

```
"auto_complete_selector": "source - comment, text.html.liquid punctuation.output.liquid, text.html.liquid punctuation.tag.liquid"
```

## Snippets

Some handy snippets:

**IF statement**

```
if + tab >>>

{% if $1 %}
  $2
{% endif %}
```

**Tag markup**

```
% + tab >>>

{% $1 %}
```

For a full list, check out the "Snippets" folder.