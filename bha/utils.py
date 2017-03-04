from __future__ import absolute_import, division, print_function
import os
import zipfile, tempfile, urllib, shutil
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
    if os.path.exists(data_path):
        print('\nDataset found in {}\n'.format(data_path))
    else:
        temp1 = tempfile.mkdtemp()
        # download zip
        url = '' # we need to upload data to somewhere
        (path, _) = urllib.request.urlretrieve(url)
        # unzip
        with zipfile.ZipFile(path, "r") as z:
            z.extractall(temp1, [x for x in z.namelist()])
        # create subjects folder
        # copy the data to subjects folder
        shutil.copytree(temp1, data_path)
        shutil.rmtree(temp1)
    return
