import pypandoc
import argparse
import json
import pathlib
import os
import shutil


### PARSE CLI ARGUMENTS ###

parser = argparse.ArgumentParser(description="Convert `data` to `web`.")
parser.add_argument("--data", nargs="?", default="data", help="The Markdown data whence the webpages are produced.")
parser.add_argument("--web", nargs="?", default="web", help="The directory containing the tree of webpages.")

args=parser.parse_args()

### LOAD CONFIG FILES ###

with open("template.html","r") as templatefile:
    template=templatefile.read()

    
### CONVERSION PROTOCOL ###

#convert a page of Markdown in `data` to a page of HTML in `web`
def make_page(mdpath,jsonpath,depth): #depth = 0 for the homepage,1 for the next layer, &c.
    #get the actual content
    content=pypandoc.convert_file(mdpath,"html")
    #get the metadata
    with open(jsonpath,"r") as jsonfile:
        metadata=json.loads(jsonfile.read())

    #fill in defaults
    if "toc" not in metadata: metadata["toc"]="shallow"
    if "short" not in metadata["title"]: metadata["title"]["short"]=metadata["title"]["text"]
    if "toc" not in metadata["title"]: metadata["title"]["toc"]=metadata["title"]["text"]
    if "parent" not in metadata["title"]: metadata["title"]["parent"]=metadata["title"]["short"]

    stylesheetpath=("../"*(depth+1))+"main.css"
    
    

### ACTUALLY MAKE `web` ###

#empty `web`
shutil.rmtree(args.web)

#transfer `data` into `web`
def 








