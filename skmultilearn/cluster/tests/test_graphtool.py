import numpy as np
import scipy.sparse as sp
import unittest
from sklearn.datasets import make_multilabel_classification
from skmultilearn.cluster.graphtool import GraphToolCooccurenceClusterer


class GraphtoolClustererBaseTests(unittest.TestCase):

    def test_weight_is_not_bool_exception(self):
        self.assertRaises(
            ValueError, GraphToolCooccurenceClusterer, 'not bool', True)

    def test_allow_overlap_is_not_bool_exception(self):
        self.assertRaises(
            ValueError, GraphToolCooccurenceClusterer, True, 'not bool')

    def test_actually_works_on_proper_params(self):
        X, y = make_multilabel_classification(
            sparse=True, return_indicator='sparse')
        assert sp.issparse(y)

        for allow_overlap in [True, False]:
            for weighted in [True, False]:
                clusterer = GraphToolCooccurenceClusterer(
                    weighted=weighted, allow_overlap=allow_overlap)
                self.assertEqual(clusterer.allow_overlap, allow_overlap)
                self.assertEqual(clusterer.is_weighted, weighted)
                partition = clusterer.fit_predict(X, y)
                self.assertIsInstance(partition, np.ndarray)

if __name__ == '__main__':
    unittest.main()
