#!/usr/bin/env python
""" generated source for module TrajectoryParser """
import csv
from Trajectory import Trajectory
from STPoint import STPoint
class TrajectoryParser(object):
    """ generated source for class TrajectoryParser """
    inputFile =""
    reader = None
    delim = ","

    def __init__(self, path):
        """ generated source for method __init__ """

        try:
            self.reader = csv.reader(open(path), delimiter=',')

        except Exception as e:
            print("Cannot find File.")

    def get_traj_set(self):
        """ generated source for method get_traj_set """
        result = []
        prev_id = 1
        try:

            tmp = None
            index = 0
            for line in self.reader:
                if index == 0:
                    index = index + 1
                    continue
                obj_id = int(line[0])
                if tmp == None:
                    tmp = Trajectory(obj_id)

                if tmp != None and obj_id != prev_id:
                    result.append(tmp)
                    tmp = Trajectory(obj_id)
                    prev_id = obj_id
                point = STPoint(obj_id, float(line[1]), float(line[2]), float(line[3]))
                tmp.points.append(point)
        except Exception as e:
            print(e.message)
        return result