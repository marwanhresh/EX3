class Edge:
    def __init__(self, src, dest, weight, info=None, tag=None):
        self._src = src
        self._dest = dest
        self._weight = weight
        self._info = info
        self._tag = tag

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, src):
        self._src = src

    @property
    def dest(self):
        return self._dest

    @dest.setter
    def dest(self, dest):
        self._dest = dest

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

    def __repr__(self):
        return 'src ={} dest={} w={}'.format(self.src, self.dest, self.weight)





