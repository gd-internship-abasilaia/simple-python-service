from datetime import datetime
import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
dt = datetime.strftime(datetime.now(), "%Y%m%d.%H%M%S")
newname = 'dist/Python-Calculator-0.4-'+dt+'.tar.gz'
os.rename('./dist/Python-Calculator-0.4-SNAPSHOT.tar.gz', newname)
newname2 = 'dist/Python-Calculator-0.4-'+dt+'.whl'
os.rename('./dist/Python_Calculator-0.4_SNAPSHOT-py2-none-any.whl', newname2)
