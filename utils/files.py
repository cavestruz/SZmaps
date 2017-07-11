import cPickle as pickle

def dump_pkl(pklfile, obj) :
    '''Save a python object'''

    with open(pklfile,'wb') as output :
        pickle.dump(obj, output, -1)

def load_pkl(pklfile) :
    '''Returns a trained model that can make predictions'''

    with open(pklfile,'r') as output :
        return pickle.load(output)
