#!/usr/bin/env python
""" generated source for module STPoint """
import math

class STPoint:
    """ generated source for class STPoint """
    cluster_id = int()
    oid = int()
    t = float()
    x = float()
    y = float()

    def __init__(self, oid=None, t=-1, x=0, y=0):
        self.t = t
        self.oid = oid
        self.x = x
        self.y = y

    def getT(self):
        """ generated source for method getT """
        return self.t

    def getOid(self):
        """ generated source for method getOid """
        return self.oid

    def getCluster_id(self):
        """ generated source for method getCluster_id """
        return self.cluster_id

    def isUnClassfied(self):
        """ generated source for method isUnClassified """
        return (self.cluster_id == 0)

    def isNoise(self):
        """ generated source for method isNoise """
        return (self.cluster_id == -1)

    def setCluster_id(self, cluster_id):
        """ generated source for method setCluster_id """
        self.cluster_id = cluster_id

    def distance(self, x2, y2):
        x2 = x2 - self.x
        y2 = y2 - self.y
        sum = x2 * x2 + y2 * y2
        return math.sqrt(sum)
