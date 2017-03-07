from __future__ import absolute_import, division, print_function
import os
import shutil
import urllib.request as req
import bha

data_path = os.path.join(bha.__path__[0], 'data')


def fetch_bha_data():
    """
    Function that downloads average_networks data if it already does not
    exist in /bha/data/

    Parameters
    ----------
    None :
    Returns
    -------
    None :
    """
    file_path = os.path.join(data_path, 'average_networks.npz')
    if os.path.exists(file_path):
        print('\nDataset found in {}\n'.format(file_path))
    else:
        # download zip
        url = 'https://ndownloader.figshare.com/files/7716100'
        # we need to upload data to somewhere
        (path, _) = req.urlretrieve(url)
        # unzip
        # create subjects folder
        # copy the data to subjects folder
        shutil.copy(path, data_path + '/average_networks.npz')
    return
