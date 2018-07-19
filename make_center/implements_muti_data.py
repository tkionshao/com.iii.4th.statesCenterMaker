import clearDataFunction
from glob import glob
import sys

# FIND FILE ENDWITH "_clr.csv"
path = sys.argv[1]
pathes = glob(path+'/*_clr.csv')

for path in pathes:
    print(path)
    clearDataFunction.bigTableProducer(path)