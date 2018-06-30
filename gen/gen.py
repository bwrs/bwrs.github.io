import pypandoc
import argparse
import json
import pathlib
import os
import os.path
import shutil


### PARSE CLI ARGUMENTS ###

parser = argparse.ArgumentParser(description="Convert `data` to `web`.")
parser.add_argument("--data", nargs="?", default="data", help="The Markdown data whence the webpages are produced.")
parser.add_argument("--web", nargs="?", default="web", help="The directory containing the tree of webpages.")
parser.add_argument("--template", nargs="?", default="gen/template.html", help="The path to `template.html`.")

args=parser.parse_args()

### LOAD CONFIG FILES ###

with open(args.template,"r") as templatefile:
    template=templatefile.read()

    
### CONVERSION PROTOCOL ###

#read metadata
def get_metadata(jsonpath):
    print("get_metadata({})".format(jsonpath))
    with open(jsonpath,"r") as jsonfile:
        metadata=json.loads(jsonfile.read())

    #fill in defaults
    if "webtoc" not in metadata: metadata["webtoc"]=1
    if "pagetoc" not in metadata: metadata["pagetoc"]=3
    if "short" not in metadata["title"]: metadata["title"]["short"]=metadata["title"]["text"]
    if "toc" not in metadata["title"]: metadata["title"]["toc"]=metadata["title"]["text"]
    if "parent" not in metadata["title"]: metadata["title"]["parent"]=metadata["title"]["short"]

    return metadata

#helper function to make indentation for `make_webtoc`
def nest_webtoc(webtoc):
    print("nest_webtoc({})".format(webtoc))
    if webtoc=="": return ""

    webtoc=webtoc.split("\n")
    return "".join(["\n  "+line for line in webtoc])

#produce `webtoc`
#depth=False returns no `webtoc`
#depth=True returns a deep `webtoc`
def make_webtoc(folder,depth,relative=None):
    print("make_webtoc({}, {}, {})".format(folder,depth,relative))
    if relative==None: relative=folder
    if depth==False or depth==0: return ""

    #get contents of `folder`
    contents=os.scandir(folder)
    #remove mere files
    contents=[f for f in contents if f.is_dir()]

    #fetch titles
    contents=[{"path":f.path, "name":get_metadata(os.path.join(f.path,"metadata.json"))["title"]["toc"]} for f in contents]

    #prepare hand-me-down depth
    newdepth=depth-1 if type(depth)==int else depth
    #make `webtoc`
    webtoclist=[' 1. <a href={} class="webtoci">{}</a>'.format(os.path.relpath(f["path"],relative),f["name"])+nest_webtoc(make_webtoc(f["path"],newdepth,relative)) for f in contents]

#convert a page of Markdown in `data` to a page of HTML in `web`
def make_page(folder):
    print("make_page({})".format(folder))
    #set file paths
    mdpath=os.path.join(folder,"content.md")
    jsonpath=os.path.join(folder,"metadata.json")
    
    #get the metadata
    metadata=get_metadata(jsonpath)

    #get the tab title
    shorttitle=metadata["title"]["short"]
    
    #get the actual content, with the pagetoc if sought
    if metadata["pagetoc"]>0:
        content=pypandoc.convert_file(mdpath,"html", extra_args=["--toc","--toc-depth={}".format(int(metadata["pagetoc"]))])
    else:
        content=pypandoc.convert_file(mdpath,"html")

    #get the relative path to the stylesheet
    stylesheetpath=os.path.relpath("main.css",folder)

    #make a list of the page's parents, with parent first, then grandparent, &c.
    parentpaths=[]
    parentpath=os.path.relpath(folder,os.path.join(args.data,".."))
    while parentpath!="" and parentpath!="/":
        #strip trailing "/"
        if parentpath[-1]=="/": parentpath=parentpath[:-1]
        parentpath=os.path.split(parentpath)[0]
        if parentpath not in ["","/"]:
            parentpaths.append(parentpath)

    #make the parents section of the `<nav>`
    parentpaths.reverse()
    parents=[]
    print("parentpaths:",parentpaths)
    for path in parentpaths:
        pathdata=get_metadata(os.path.join(path,"metadata.json"))
        parents.append('<a class="parent" href="{}">{}</a>/'.format(os.path.relpath(path,folder),pathdata["title"]["parent"]))
    parents="".join(parents)

    #maketitle
    titlehtml='<h1 class="titletext">{}</h1>'.format(metadata["title"]["text"])
    if "sub" in metadata["title"]: titlehtml+='\n\n<h2 class="titlesub">{}</h2>'.format(metadata["title"]["sub"])
    if "date" in metadata["title"] and "author" in metadata["title"]: titlehtml+='\n\n<h4 class="titleauthordate">{}, {}</h4>'.format(metadata["title"]["author"],metadata["title"]["date"])
    elif "date" in metadata["title"]: titlehtml+='\n\n<h4 class="titleauthordate">{}</h4>'.format(metadata["title"]["date"])
    elif "author" in metadata["title"]:titlehtml+='\n\n<h4 class="titleauthordate">{}</h4>'.format(metadata["title"]["author"])
    title=titlehtml

    #choose the webtoc depth
    if metadata["webtoc"]=="none": depth=False
    elif metadata["webtoc"]=="deep": depth=True
    else: depth=int(metadata["webtoc"])
    #make the webtoc
    webtoc=make_webtoc(folder,depth)

    return template.format(shorttitle=shorttitle,stylesheetpath=stylesheetpath,parents=parents,title=title,webtoc=webtoc,content=content)

### ACTUALLY MAKE `web` ###

#empty `web`
shutil.rmtree(args.web)
os.mkdir(args.web)

#convert a directory
def convert_dir(datadir,webdir):
    print("convert_dir({}, {})".format(datadir,webdir))
    #make the page
    indexpath=os.path.join(webdir,"index.html")
    with open(indexpath,"w") as f:
        f.write(make_page(datadir))

    #get contents of `datadir`
    contents=os.scandir(datadir)
    #remove mere files
    contents=[f for f in contents if f.is_dir()]
    for f in contents:
        #make the corresponding directory in `web`
        os.mkdir(os.path.join(webdir,f.name))
        #convert into it
        convert_dir(f.path,os.path.join(webdir,f.name))

#transfer `data` into `web`
convert_dir(args.data,args.web)
