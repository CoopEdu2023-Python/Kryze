import sys
import os
current_directory = os.path.dirname(__file__)
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)
from .. import wordcloud_generate