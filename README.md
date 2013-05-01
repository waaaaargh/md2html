# md2html

## What does it?

Put simply: It converts markdown to html and puts it into a jinja2-formatted template. Oh, and it automagically scans for a first-level-heading in your markdown and sets it as your page title.

## Setup

You might want to check if you have the ```jinja2``` and ```markdown``` packages installed. Many OSs have them in their repositories. If you use Windows or Mac OS, you probably have to install them via ```pip```.

## Usage

### Invocation
```
$ md2html.py markdown template [ -o output.html ] [ -t "My Custom title" ]
```

### Parameters
  * ```markdown```: Path to the markdown file
  * ```template```: Path to the jinja file. The HTML output is passed to jinja as ```html```, the title as ```title```.
  * ```-o | --output```: Path to write the output file to. If no filename is given the filename will be derived from 
    the input file name.
  * ```-t | --title```: Overwrite the automagically detected title attribute. If the title attribute is empty and no title attribute is set, the title attribute is left empty.

  
