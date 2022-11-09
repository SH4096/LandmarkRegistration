#
# RegistrationState
#

class RegistrationState:
  """ Holds parameters of registration.
  An instance of this class is passed to virtual methods
  """

  # DRML volume nodes
  fixed = None
  moving = None
  transformed = None

  # DRML Markup Point List Nodes
  fixedPoints = None
  movingPoints = None
  transformedPoints = None

  # DRML Linear Transform Node
  transform = None

