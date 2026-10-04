import numpy as np
import pandas as pd
from pandas import DataFrame

rank = {
    "name":   ["Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia"],
    "age":    [25,  29,     22,    28,    33,      27,    24,      31],
    "gender": ["Male","Female","Male","Female","Male","Female","Male","Female"],
    "rank": [1,2,3,4,5,6,7,8]
}

rank_df = DataFrame(rank)
rank_df