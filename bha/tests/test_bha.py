from __future__ import absolute_import, division, print_function
import os.path as op
import numpy as np
import numpy.testing as npt
import bha

data_path = op.join(bha.__path__[0], 'data')


def test_cross_modularity():
    """
    Testing the transformation of the data from raw data to functions
    used for fitting a function.

    """
    # We start with actual data. We test here just that reading the data in
    # different ways ultimately generates the same arrays.

    from bha.utils import fetch_bha_data
    from scipy import spatial, cluster

    if not op.exists(op.join(data_path, 'average_networks.npz')):
        fetch_bha_data()

    data = np.load(op.join(data_path, 'average_networks.npz'))
    struct_network = data.f.struct_network
    func_network = data.f.func_network

    # These parameters are based on the reference paper
    num_clusters = 20
    alpha = 0.45
    beta = 0.0
    struct_network = struct_network / np.max(struct_network)

    """
    Functional dendogram -> structure follows function
    """

    Y = spatial.distance.pdist(func_network, metric='cosine')
    Z = cluster.hierarchy.linkage(Y, method='weighted')
    T = cluster.hierarchy.cut_tree(Z, n_clusters=num_clusters)

    Xsf, Qff, Qsf, Lsf = bha.cross_modularity(func_network, struct_network,
                                              alpha, beta, T[:, 0])

    # data from matlab module
    npt.assert_almost_equal(Xsf, 0.2892, decimal=4)
    npt.assert_almost_equal(Lsf, 0.5263, decimal=4)


def test_modularity_index():
    from bha.utils import fetch_bha_data
    from scipy import spatial, cluster

    if not op.exists(op.join(data_path, 'average_networks.npz')):
        fetch_bha_data()

    data = np.load(op.join(data_path, 'average_networks.npz'))
    struct_network = data.f.struct_network
    func_network = data.f.func_network

    # These parameters are based on the reference paper
    num_clusters = 20
    struct_network = struct_network / np.max(struct_network)

    """
    Functional dendogram -> structure follows function
    """

    Y = spatial.distance.pdist(func_network, metric='cosine')
    Z = cluster.hierarchy.linkage(Y, method='weighted')
    T = cluster.hierarchy.cut_tree(Z, n_clusters=num_clusters)

    Qa = bha.modularity_index(np.abs(func_network), T[:, 0])
    Qb = bha.modularity_index(np.abs(struct_network), T[:, 0])

    npt.assert_almost_equal(Qa, 0.0893, decimal=4)
    npt.assert_almost_equal(Qb, 0.5148, decimal=4)
