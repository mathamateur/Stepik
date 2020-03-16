class NonPositiveError(Exception):
    pass
class PositiveList(list):
    def append(self, object) -> None:
        if object > 0:
            super(PositiveList,self).append(object)
        else:
            raise NonPositiveError
