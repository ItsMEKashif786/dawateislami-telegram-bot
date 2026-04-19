import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)
os.chdir(script_dir)
import config
import bot_