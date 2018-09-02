#!/usr/bin/env python
""" generated source for module Convoy """

class Convoy(object):
    """ generated source for class Convoy """
    assigned = bool()
    startTime = float()
    endTime = float()
    lifetime = int()
    cluster = []

    def __init__(self, assigned=None, lifetime=None, cluster=None):
        """ generated source for method __init__ """
        if assigned:
            self.assigned = assigned
        else:
            self.assigned = False
        if lifetime:
            self.lifetime = lifetime
        else:
            self.lifetime = 1

        if cluster:
            self.cluster = cluster


    def isAssigned(self):
        """ generated source for method isAssigned """
        return self.assigned

    def setAssigned(self, assigned):
        """ generated source for method setAssigned """
        self.assigned = assigned

    def getStartTime(self):
        """ generated source for method getStartTime """
        return self.startTime

    def setStartTime(self, startTime):
        """ generated source for method setStartTime """
        self.startTime = startTime

    def getEndTime(self):
        """ generated source for method getEndTime """
        return self.endTime

    def setEndTime(self, endTime):
        """ generated source for method setEndTime """
        self.endTime = endTime

    def getLifetime(self):
        """ generated source for method getLifetime """
        return (self.endTime) - (self.startTime) + 1

    def setLifetime(self, lifetime):
        """ generated source for method setLifetime """
        self.lifetime = lifetime

    def toString(self):

        res = "Start_time: " + str(self.getStartTime()) + ",\tEnd_Time: " + str(self.getEndTime()) + "\t(" + str(self.getLifetime()) + ")\nobj_list: ";

        # Collections.sort(this);

        # res += str(self.cluster[0])

        for oid in self.cluster:

            res += ", " + str(oid)


        res += '\n'

        return res

    def intersection(self,  c):
        """ generated source for method intersection """
        c1 = Convoy()
        c1.startTime = c.startTime
        c1.cluster = []
        tmp = c1
        i = 0
        while i < len(self.cluster):
            j = 0
            while j < len(c.cluster):
                if self.cluster[i] == c.cluster[j]:
                    tmp.cluster.append(c.cluster[j])
                j += 1
            i += 1
        return tmp

