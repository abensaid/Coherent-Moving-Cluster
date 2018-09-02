import STPoint
from Cluster import Cluster

class DBSCAN:
    @staticmethod
    def initial_format(datalist):
        for point in datalist:
            if not point.isUnClassfied():
                point.setCluster_id(0)


    @staticmethod
    def dbscan_to_cluster(datalist, eps, minPts):
        DBSCAN.initial_format(datalist)
        num_cluster = DBSCAN.dbscan(datalist, eps, minPts)
        result = []
        for point in datalist:
            if point.getCluster_id() == -1:
                continue
            find_cluster = False

            for cluster_set in result:
                if cluster_set.getCluster_id() == point.getCluster_id():
                    cluster_set.oids.append(point.getOid())
                    find_cluster = True
                    break
            if not find_cluster:
                new_c_id = point.getCluster_id()
                new_cluster = Cluster(new_c_id)
                new_cluster.oids.append(point.getOid())
                result.append(new_cluster)

        return result



    @staticmethod
    def dbscan(datalist, eps, minPts):
        cluster_Id = 1
        for point in datalist:
            if point.isUnClassfied():
                if DBSCAN.expandCluster(datalist, point, cluster_Id, eps, minPts):
                    cluster_Id = cluster_Id + 1
        cluster_Id = cluster_Id -1
        return cluster_Id



    @staticmethod
    def expandCluster(datalist, point, clu_Id, eps, minPts):
        seeds = DBSCAN.regionQuery(datalist, point, eps)
        if len(seeds) < minPts:
            DBSCAN.chg_clu_id(point, -1)
            return False
        else:
            for tup in seeds:
                DBSCAN.chg_clu_id(tup, clu_Id)
            seeds.remove(point)

            while True:
                currentP = seeds[0]
                result = DBSCAN.regionQuery(datalist, currentP, eps)
                if len(result) >= minPts:
                    for resultP in result:
                        if resultP.isUnClassfied():
                            seeds.append(resultP)
                            DBSCAN.chg_clu_id(resultP, clu_Id)
                        else:
                            if resultP is None:
                                DBSCAN.chg_clu_id(resultP, clu_Id)
                del seeds[0]
                if not seeds:
                    break
            return True



    @staticmethod
    def regionQuery(datalist, query, eps):
        result = []
        for point in datalist:
            if query.distance(point.x, point.y) <= eps:
                result.append(point)
        return result



    @staticmethod
    def chg_clu_id(data, cluster_id):
        data.setCluster_id(cluster_id)



    @staticmethod
    def validate_parameter(eps, minPts):
        if eps < 0 or minPts < 1 :
            return False
        else:
            return True



