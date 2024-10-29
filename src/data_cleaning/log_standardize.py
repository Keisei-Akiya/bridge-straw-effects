import numpy as np

def log_standardize(data):
    """
    Log standardize the data

    Parameters
    ----------
    data : np.array
        The data to be log standardized

    Returns
    -------
    np.array
        The log standardized data
    """

    log_data = np.log(data + 1)

    standard_data = (log_data - np.mean(log_data)) / np.std(log_data)

    return standard_data