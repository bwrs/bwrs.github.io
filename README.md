# bwrs.github.io
My personal webpage.

## Directory structure

### `data`
The content of the webpages, written in Markdown; this folder, and those within it, each contain `content.md` and `metadata.json`, which are used to produce the corresponding HTML file in `web`. I may extend this syntax later to allow leaves of the tree to simply be written as Markdown files.

#### `content.md`
This produces the body of the text of the webpage.

#### `metadata.json`
This is a dictionary with these keys:

 - `webtoc`, controlling the `toc` of pages within the directory, taking one of
   - `none`; prints no table of contents
   - an integer; print a table of contents that many layers deep; this, as 1, is the default
   - `deep`; prints all the pages below it in the tree to the toc
 - `pagetoc`, taking a number, indicating the depth of the toc, having default value 3.
 - `title`, taking a further JSON object, having keys:
   - `text`, the title itself
   - `sub`, the subtitle (default: omission in the HTML)
   - `short`, the title for the tab (default: `text`)
   - `toc`, the title used for tables of content (default: `text`)
   - `parent`, the title used for parents in the `<nav>` section (default: `short`)
   - `date`, the date, in format `yyyy-mm-dd` (default: omission in the HTML)
   - `author`, the author, if not me (BWRS) (default: omission in the HTML)

### `files`
Files referred to by the webpages.

### `gen`
The tools that convert `data` into `web`.

### `web`
The webpages, other than the top-level `index.html`. A set of folders, each containing their own `index.html`.

### `main.css`
The CSS file.
