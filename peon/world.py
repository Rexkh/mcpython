from types import (MobTypes, ItemTypes)
import smpmap


class World(smpmap.World):
    def __init__(self):
        self.columns = {}
        self.entities = {}

    def iter_entities(self, types=None):
        if isinstance(types, list):
            type_ids = [t if isinstance(t, int)
                        else MobTypes.get_id(t)
                        for t in types]
        for entity in self.entities.values():
            if types is None or entity._type in type_ids:
                yield entity

    def is_solid_block(self, x, y, z):
        _type = self.get_id(x, y, z)
        return None if _type is None else ItemTypes.is_solid(_type)

    def get_next_highest_solid_block(self, x, y, z):
        for y in xrange(int(y), -1, -1):
            if self.is_solid_block(x, y, z):
                return (x, y, z)

    @staticmethod
    def iter_adjacent(x, y, z):
        for dx in xrange(-1, 2):
            for dy in xrange(-1, 2):
                for dz in xrange(-1, 2):
                    if dx != 0 or dz != 0:
                        yield (x + dx, y + dy, z + dz)

    def iter_moveable_adjacent(self, x0, y0, z0):
        for x, y, z in self.iter_adjacent(x0, y0, z0):
            if self.is_moveable(x0, y0, z0, x, y, z):
                yield (x, y, z)

    def is_moveable(self, x0, y0, z0, x, y, z):
        if x0 == x or z0 == z:
            return self.is_standable(x, y, z)
        return all([
            self.is_empty(x0, y, z),
            self.is_empty(x, y, z0),
            self.is_standable(x, y, z),
        ])

    def is_standable(self, x, y, z):
        return all([
            self.is_empty(x, y, z),
            self.is_solid_block(x, y - 1, z),
        ])

    def is_empty(self, x, y, z):
        return all([
            not self.is_solid_block(x, y + 1, z),
            not self.is_solid_block(x, y, z),
        ])
