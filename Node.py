

class Node:
    def __init__(self, _id, location=None, weight=None, info=None, tag=None):
        self._id = _id
        self._location = location
        self._weight = weight
        self._info = info
        self._tag = tag
        self._last_change = None

    @property
    def id(self):
        return self._id

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, tag):
        self._tag = tag

    @property
    def last_change(self):
        return self._last_change

    @last_change.setter
    def last_change(self, last_change):
        self._last_change = last_change

    def __repr__(self):
        return 'id ={} location={}'.format(self.id, self.location)





