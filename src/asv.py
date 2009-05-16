import sys
import os
import re
current_dir = os.getcwd()
lib_path = re.sub('[^/]*/?$', "lib", current_dir)
sys.path.append(lib_path)

import Phidgets
