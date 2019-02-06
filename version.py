import datetime
import os, sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
dt = str(datetime.datetime.utcnow())
newname = 'dist/Python-Calculator-0.4-'+dt+'.tar.gz'
os.rename('dist/Python-Calculator-0.4.SNAPSHOT.tar.gz', newname)
newname2 = 'dist/Python_Calculator-0.4_'+dt+'SNAPSHOT-py2-none-any.whl'
os.rename('dist/Python_Calculator-0.4.SNAPSHOT-py2-none-any.whl', newname2)
