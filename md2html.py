#!/usr/bin/python

# Some quick plumbing to insert Markdown Input into my beloved blog template.

import sys
import argparse
import re

# external dependencies
import markdown
import jinja2

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Converts Markdown into HTML \
        and puts it into a template")
    parser.add_argument('markdown', metavar="markdown.md", help='markdown file')
    parser.add_argument('template', metavar="template.tpl", help='template \
            file (jinja2)')
    parser.add_argument('-o', '--output', metavar='output.html', help='location of \
            HTML output')
    parser.add_argument('-t', '--title', metavar='My Page Title',
                        help='Overwrite title autodetection')
    args = parser.parse_args()

    try:
        mdfile = open(args.markdown)
        md = mdfile.read()
    except Exception:
        print("Could not read markdown file. quitting")
        sys.exit(1)

    try:
        tplfile = open(args.template)
        tpltext = tplfile.read()
    except Exception:
        print("Could not read template file. quitting")
        sys.exit(1)

    html = markdown.markdown(md)
    tpl = jinja2.Template(tpltext)
    
    if not args.title:
        # autodetect title
        title = re.match('<h1>(.*)</h1>', html).groups()[0]
        if title is None:
            title=""
    else:
        title = args.title

    output = tpl.render(html=html, title=title)
    
    if args.output:
        outfile = args.output
    else:
        outfile =  '.'.join(args.markdown.split('.')[0:-1]) + ".html"


    out = open(outfile, 'w')
    out.write(output)
    out.close
