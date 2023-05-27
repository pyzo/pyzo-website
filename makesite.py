"""
Script to build a website from a bunch of markdown files.
Inspired by https://github.com/sunainapai/makesite
Tweaked for pyzo.org
"""

import os
import shutil
import webbrowser

import markdown
import pygments
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name


TITLE = "Pyzo"

NAV = {
    "Quickstart": "start",
    "About Python": {
        "": "about_python",
        "Why Python": "whypython",
        "Python 3": "python3",
        "Python vs Matlab": "python_vs_matlab",
        "Speed": "speed",
        "For whom": "forwhom",
    },
    "About Pyzo": {
        "": "about_pyzo",
        "Mission": "mission",
        "Features": "features",
        "Themes": "pyzo_themes",
        "Screenshots": "screenshots",
        "Release notes": "https://github.com/pyzo/pyzo/wiki/Release_notes",
    },
    "Guide": {
        "": "guide",
        "Short introduction": "pyzo_intro",
        "Installing additional packages": "install_packages",
        "Configuring shells": "shellconfig",
        "Interactive vs script mode": "interactive_vs_script",
        "FAQ": "faq",
    },
    "Learn": "learn",
}

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(THIS_DIR, "output")
STATIC_DIR = os.path.join(THIS_DIR, "static")
PAGES_DIR = os.path.join(THIS_DIR, "pages")


def create_menu(page):
    """ Create the menu for the given page.
    """
    menu = []
    # menu.append('<span class="header">Topics</span>')
    for title, target in NAV.items():
        if isinstance(target, str):
            if target.startswith(("https://", "http://", "/")):
                menu.append(f"<a href='target'>{title}</a>")
            else:
                menu.append(f"<a href='{target}.html'>{title}</a>")
                if target == page.name:
                    menu[-1] = menu[-1].replace("<a ", '<a class="current" ')
                    menu += [
                        f"<a class='sub' href='#{title.lower()}'>{title}</a>"
                        for level, title in page.headers
                        if level == 2
                    ]
        elif isinstance(target, dict):
            menu.append(f"<a href='{target['']}.html'>{title}</a>")
            if target[""] == page.name:
                menu[-1] = menu[-1].replace("<a ", '<a class="current" ')
            if any(page.name == subtarget for subtarget in target.values()):
                for subtitle, subtarget in target.items():
                    if not subtitle:
                        continue
                    if subtarget.startswith(("https://", "http://", "/")):
                        menu.append(f"<a class='sub' href='{subtarget}'>{subtitle}</a>")
                    else:
                        menu.append(
                            f"<a class='sub' href='{subtarget}.html'>{subtitle}</a>"
                        )
                        if subtarget == page.name:
                            menu[-1] = menu[-1].replace("class='", "class='current ")
        else:
            raise RuntimeError(f"Unexpected NAV entry {type(target)}")

    return "<br />".join(menu)


def create_assets():
    """ Returns a dict of all the assets representing the website.
    """
    assets = {}

    # Load all static files
    for root, dirs, files in os.walk(STATIC_DIR):
        for fname in files:
            filename = os.path.join(root, fname)
            with open(filename, "rb") as f:
                assets[os.path.relpath(filename, STATIC_DIR)] = f.read()

    # Collect pages
    pages = {}
    for fname in os.listdir(PAGES_DIR):
        if fname.lower().endswith(".md"):
            name = fname.split(".")[0].lower()
            with open(os.path.join(PAGES_DIR, fname), "rb") as f:
                md = f.read().decode()
            pages[name] = Page(name, md)

    # todo: Collect blog posts

    # Get template
    with open(os.path.join(THIS_DIR, "template.html"), "rb") as f:
        html_template = f.read().decode()

    with open(os.path.join(THIS_DIR, "style.css"), "rb") as f:
        css = f.read().decode()
    css += "/* Pygments CSS */\n" + HtmlFormatter(style="vs").get_style_defs(
        ".highlight"
    )

    # Generate pages
    for page in pages.values():
        page.prepare(pages.keys())
        title = TITLE if page.name == "index" else TITLE + " - " + page.name
        menu = create_menu(page)
        html = html_template.format(
            title=title, style=css, body=page.to_html(), menu=menu
        )
        print("generating", page.name + ".html")
        assets[page.name + ".html"] = html.encode()

    # Fix backslashes on Windows
    for key in list(assets.keys()):
        if "\\" in key:
            assets[key.replace("\\", "/")] = assets.pop(key)

    return assets


def main():
    """ Main function that exports the page to the file system.
    """
    # Create / clean output dir
    if os.path.isdir(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    os.mkdir(OUT_DIR)

    # Write all assets to the directory
    for fname, bb in create_assets().items():
        filename = os.path.join(OUT_DIR, fname)
        dirname = os.path.dirname(filename)
        if not os.path.isdir(dirname):
            os.makedirs(dirname)
        with open(filename, "wb") as f:
            f.write(bb)


class Page:
    """ Representation of a page. It takes in markdown and produces HTML.
    """

    def __init__(self, name, markdown):
        self.name = name
        self.md = markdown
        self.parts = []
        self.headers = []

    def prepare(self, page_names):
        # Convert markdown to HTML
        self.md = self._fix_links(self.md, page_names)
        self.md = self._highlight(self.md)
        self._split()  # populates self.parts and self.headers

    def _fix_links(self, text, page_names):
        """ Fix the markdown links based on the pages that we know.
        """
        for n in page_names:
            text = text.replace(f"]({n})", f"]({n}.html)")
            text = text.replace(f"]({n}.md)", f"]({n}.html)")
        return text

    def _highlight(self, text):
        """ Apply syntax highlighting.
        """
        lines = []
        code = []
        for i, line in enumerate(text.splitlines()):
            if line.startswith("```"):
                if code:
                    formatter = HtmlFormatter()
                    try:
                        lexer = get_lexer_by_name(code[0])
                    except Exception:
                        lexer = get_lexer_by_name("text")
                    lines.append(
                        pygments.highlight("\n".join(code[1:]), lexer, formatter)
                    )
                    code = []
                else:
                    code.append(line[3:].strip())  # language
            elif code:
                code.append(line)
            else:
                lines.append(line)
        return "\n".join(lines).strip()

    def _split(self):
        """ Split the markdown into parts based on sections.
        Each part is either text or a tuple representing a section.
        """
        text = self.md
        self.parts = parts = []
        self.headers = headers = []
        lines = []

        # Split in parts
        for line in text.splitlines():
            if line.startswith(("# ", "## ", "### ", "#### ", "##### ")):
                # Finish pending lines
                parts.append("\n".join(lines))
                lines = []
                # Process header
                level = len(line.split(" ")[0])
                title = line.split(" ", 1)[1]
                title_short = title.split("(")[0].split("<")[0].strip().replace("`", "")
                headers.append((level, title_short))
                parts.append((level, title_short, title))
            else:
                lines.append(line)
        parts.append("\n".join(lines))

        # Now convert all text to html
        for i in range(len(parts)):
            if not isinstance(parts[i], tuple):
                parts[i] = markdown.markdown(parts[i], extensions=[]) + "\n\n"

    def to_html(self):
        htmlparts = []
        for part in self.parts:
            if isinstance(part, tuple):
                level, title_short, title = part
                title_html = (
                    title.replace("``", "`")
                    .replace("`", "<code>", 1)
                    .replace("`", "</code>", 1)
                )
                ts = title_short.lower()
                if part[0] == 2 and title_short:
                    htmlparts.append(
                        "<a class='anch' name='{}' href='#{}'>".format(ts, ts)
                    )
                    htmlparts.append("<h%i>%s</h%i>" % (level, title_html, level))
                    htmlparts.append("</a>")
                else:
                    htmlparts.append("<h%i>%s</h%i>" % (level, title_html, level))
            else:
                htmlparts.append(part)
        return "\n".join(htmlparts)


def copydir(src, dst):
    """ Like shutil.copytree, but directories are ok to already exist.
    """
    for item in os.listdir(src):
        s, d = os.path.join(src, item), os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.isdir(d):
                os.mkdir(d)
            copydir(s, d)
        else:
            shutil.copy(s, d)


if __name__ == "__main__":
    main()
    # webbrowser.open(os.path.join(OUT_DIR, "index.html"))
