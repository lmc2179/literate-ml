from literate_python.tools import Document, Tangler, Weaver
from os import scandir, unlink
import subprocess
import shlex

for filename in scandir():
    if filename.name.endswith('.pyl'):
        stem = filename.name[:-4]
        d = Document(open(filename.name).read())
        python_filename = '{0}.py'.format(stem)
        latex_filename = '{0}.tex'.format(stem)
        Tangler().tangle_module(filename.name,
                                python_filename,
                                python_filename)
        Weaver().weave_module(filename.name,
                              latex_filename)
        proc=subprocess.Popen(shlex.split('pdflatex {0}'.format(latex_filename)))
        proc.communicate()
        unlink('{0}.aux'.format(stem))
        unlink('{0}.log'.format(stem))