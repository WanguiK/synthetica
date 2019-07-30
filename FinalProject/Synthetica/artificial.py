import logging
import random
import pandas as pd
from tabulate import tabulate

from .trumania.trumania.core import util_functions as util_functions
from .trumania.trumania.core import circus
from .trumania.trumania.core.random_generators import SequencialGenerator, NumpyRandomGenerator


util_functions.setup_logging()

logging.info("building student dataset")


randint = ['age', 'medu', 'fedu', 'famrel', 'traveltime', 'studytime', 'failures', 'freetime', 'walc', 'dalc', 'health', 'absences', 'g1', 'g2', 'g3']
choices = ['sex', 'address', 'pstatus', 'mjob', 'fjob','guardian', 'famsize', 'reason', 'schoolsup', 'famsup','activities', 'paidclass', 'internet']

def build_circus():
    seed = random.randrange(1, 1000)
    return circus.Circus(
        name="Student Dataset",
        master_seed=seed,
        start=pd.Timestamp("1 Jan 2017 00:00"),
        step_duration=pd.Timedelta("1h")
    )


def create_student_population(the_circus, size, metadata = []):    
    student = the_circus.create_population (
        name = "Student Information", 
        size = size,
        ids_gen = SequencialGenerator()
    )
    length = len(metadata)
    opt = []
    for i in range(length):
        opt = metadata[i][2].replace(' ','')
        opt = opt.split (",")
        title = metadata[i][1]
        if metadata[i][0] in choices:
            name = 'gen' + str(i)
            name = NumpyRandomGenerator(
                method = "choice",
                a = opt,
                seed = next(the_circus.seeder)
            )
        elif metadata[i][0] in randint:
            for i in range(0, len(opt)): 
                opt[i] = int(opt[i])
            name = 'gen' + str(i)
            name = NumpyRandomGenerator(
                method = "randint",
                low = min(opt), 
                high = max(opt),
                seed = next(the_circus.seeder)
            )
        student.create_attribute(title, init_gen = name)
    table = tabulate (
            student.to_dataframe(),
            headers='keys', 
            tablefmt='html'
    )
    return table

def generate(s, m):
    dataset_circus = build_circus()
    table = create_student_population(dataset_circus, s, m)
    return table


# meta = 
# opt = meta[i][2].replace(' ','')
# opt = opt.split (",")