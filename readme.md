## Siteleaf Liquid support for Sublime Text

This is a fork of the [shopify-liquid](https://bitbucket.org/granteagon/shopify-liquid) syntax, which was based off of the Djaniero package for Django.

## Installation

**Suggested**: Install using [Package Control](https://packagecontrol.io/). Search for "Siteleaf Liquid Syntax".

**Or** install manually:

1. Clone this repo
2. Put the contents of this repo directly inside:

 - OS X: ~/Library/Application Support/Sublime Text 3/Packages/
 - Windows: %APPDATA%/Sublime Text 3/Packages/
 - Linux: ~/.config/sublime-text-3/Packages

**After installing:**

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

**Assign**

```
assign + tab >>>

{% assign $1 = $2 %}
```

**Capture**

```
capture + tab >>>

{% capture $1 %}$2{% endcapture %}
```

**Comment**

```
comment + tab >>>

{% comment %}$0{% endcomment %}
```

**Context variable**

```
va + tab >>>

{{ $1 }}
```

**Cycle**

```
cycle + tab >>>

{% cycle $1 %}
```

**Else**

```
else + tab >>>

{% else %}
```

**Elsif**

```
elsif + tab >>>

{% elsif $1 %}
```

**Endcapture**

```
endcapture + tab >>>

{% endcapture %}
```

**Endfor**

```
endfor + tab >>>

{% endfor %}
```

**Endif**

```
endif + tab >>>

{% endif %}
```

**Endraw**

```
endraw + tab >>>

{% endraw %}
```

**For**

```
for + tab >>>

{% for $1 in $2 %}
	$3
{% endfor %}
```

For a full list, check out the "Snippets" folder.
