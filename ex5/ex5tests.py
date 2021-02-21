from autotest import TestSet

import testrunners

import sys
from importlib import import_module
from io import StringIO

defaults = {'modulename':'wordsearch',
            'runner':testrunners.functionname_runner,
            'ans':[True],
            }

cases = {'checkinput':{'fname':'check_input_args',
                   },
         'readwordlist':{'fname':'read_wordlist_file',
                   },
         'readmatrix':{'fname':'read_matrix_file',
                   },
         'choose':{'fname':'find_words_in_matrix',
           },
         'writeoutput':{'fname':'write_output_file',
           },
     }

tsets = {'ex5':TestSet({},cases),
}
