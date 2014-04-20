#Below is hotfix for MySQL connector 1.1.6
 
import warnings
 
origin_filterwarnings = warnings.filterwarnings
 
default_param = origin_filterwarnings.__defaults__
 
default_param = list(default_param[:-1])
default_param.append(True)
 
origin_filterwarnings.__defaults__ = tuple(default_param)