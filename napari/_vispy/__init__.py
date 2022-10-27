import logging

from vispy import app

from napari._qt import API_NAME

# set vispy application to the appropriate qt backend
app.use_app(API_NAME)
del app

# set vispy logger to show warning and errors only
vispy_logger = logging.getLogger('vispy')
vispy_logger.setLevel(logging.WARNING)


from .camera import VispyCamera
from .canvas import VispyCanvas
from .overlays.axes import VispyAxesOverlay
from .overlays.interaction_box import VispyInteractionBox
from .overlays.scale_bar import VispyScaleBarOverlay
from .overlays.text import VispyTextOverlay
from .utils.quaternion import quaternion2euler
from .utils.visual import create_vispy_layer
