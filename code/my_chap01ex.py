"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent dataself.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass

def CrossValidate(preg,resp):
    """Cross validate the pregnancy numbers
    between the pregnancy file and the respondent one.
    """
    pass


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = ReadFemResp()
    #assert resp.pregnum.value_counts()[1] == 1267
    print(nsfg.MakePregMap(nsfg.ReadFemPreg()))
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
