import os, imp, inspect

#### UPDATE HERE: Add your module path
module_path = ''

def getdocs():
    """ Returns a list of tuples with function name and function docs.
    """
    funcs = inspect.getmembers(mr, inspect.isfunction)
    docs = []
    for func in funcs:
        if func[1].func_doc == None:
            docs.append([func[1].__name__, "No documentation"])
        else:
            docs.append([func[1].__name__, func[1].func_doc])

    return docs


def createfiles(items):
    """ Creates Markdown files using tuples. item[0] is filename and item[1] is file contents.
    In this case, function name is filename and documentation is file contents.
    """

    for item in items:
        file = open(item[0]+'.md','w')
        file.write(item[1])
        file.close


def main(module_path):
    # markdown files will be added here
    dir_path = os.path.dirname(os.path.realpath(module_path))
    os.chdir(dir_path)

    # import module
    m = imp.load_source('m', module_path)
    
    # get all functions
    docs = getdocs()
    
    # create an .md file for each function
    createfiles(docs)


if __name__ == '__main__':
    main(module_path)
