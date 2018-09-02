#!/usr/bin/env python
""" generated source for module Trajectory """
import STPoint

class Trajectory(object):
    """ generated source for class Trajectory """
    o_id = int()
    points = []

    def __init__(self, o_id):
        """ generated source for method __init__ """
        self.o_id = o_id
        self.points = []

    def getPointAt(self, t):
        """ generated source for method getPointAt """
        # iter = self.points.iterator()
        for point in self.points:
            if point.getT() == t:
                return point
        return None

    def getPoints(self):
        """ generated source for method getPoints """
        return self.points

    def getO_id(self):
        """ generated source for method getO_id """
        return self.o_id