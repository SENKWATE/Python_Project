import datetime


def julian_2_standard_date(julian_date_input):
    """
     This function take julian date as an input and converts it into a standard 
     date in the format of: day/month/year
    """
    if len(julian_date_input) > 5:
        julian_date_input = julian_date_input[2:]
    
    return datetime.datetime.strptime(julian_date_input, '%y%j').date().strftime('%d-%m-%Y')
    
