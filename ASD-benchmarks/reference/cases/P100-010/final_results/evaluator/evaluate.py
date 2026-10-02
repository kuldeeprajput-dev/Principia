from pathlib import Path
import sys
root=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(root/'evaluation'))
from benchmark import main
if __name__=='__main__':
 if '--task'not in sys.argv and len(sys.argv)>1 and sys.argv[1]in['example','validate','score','replay','prepare','verify']:sys.argv.extend(['--task','P100-010.original.v1'])
 main()
