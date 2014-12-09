
import sys

if (sys.version_info[0] > 3) or (sys.version_info[0] == 3):
    from . shotgun_python3 import (Shotgun, ShotgunError, ShotgunFileDownloadError, Fault, 
                         ProtocolError, ResponseError, Error, __version__)
    from . shotgun_python3 import SG_TIMEZONE as sg_timezone
else:
    from . shotgun import (Shotgun, ShotgunError, ShotgunFileDownloadError, Fault, 
                         ProtocolError, ResponseError, Error, __version__)
    from . shotgun import SG_TIMEZONE as sg_timezone

