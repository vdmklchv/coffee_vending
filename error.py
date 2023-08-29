class ItemError(Exception):
    """Raised when user chooses incorrect menu entry"""
    pass


class NotEnoughResourcesError(Exception):
    """Raised when machine doesn't have enough resources to make a drink"""
    pass


class UnknownIngredientError(Exception):
    """Raised when ingredient is not on the list of available resources for machine"""
    pass
