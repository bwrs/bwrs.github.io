# bwrs.github.io
My personal webpage.

##Directory structure

###`data`
The content of the webpages, written in Markdown; this folder, and those within it, each contain `content.md` and `metadata.json`, which are used to produce the corresponding HTML file in `web`. I may extend this syntax later to allow leaves of the tree to simply be written as Markdown files.

####`content.md`
This produces the body of the text of the webpage.

####`metadata.md`
This is a dictionary with these keys:

 - `toc`, taking one of
   - `none`; prints no table of contents
   - `shallow`; default, prints only the next layer of folders
   - `deep`; prints all the pages below it in the tree to the toc
 - `title`, taking a further JSON object, having keys:
   - `text`, the title itself
   - `sub`, the subtitle (default: omission in the HTML)
   - `short`, the title for the tab (default: `text`)
   - `toc`, the title used for tables of content (default: `text`)
   - `parent`, the title used for parents in the `<nav>` section (default: `short`)
   - `date`, the date, in format `yyyy-mm-dd`
   - `author`, the author, if not me (BWRS) (default: omission in the HTML)

###`files`
Files referred to by the webpages.

###`gen`
The tools that convert `data` into `web`.

###`web`
The webpages, other than the top-level `index.html`. A set of folders, each containing their own `index.html`.

