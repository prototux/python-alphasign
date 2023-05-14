from .all import All
from .alpha_2x0c import Alpha2X0C


# Sign Types
class SignType(dict):
    All = All
    Alpha_2X0C = Alpha2X0C

    @staticmethod
    def exists(name):
        return name in [x for x in dir(SignType) if not x.startswith("__")]

    def __getattr__(self, item):
        return getattr(SignType, item)
