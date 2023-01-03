import numpy as np

def calculate(list):
    if len(list) <9:
        raise ValueError('List must contain nine numbers.')
    else:
        
        calculations = { 'mean' : '', 'variance' : '','standard deviation' : '', 'max' : '', 'min' : '', 'sum' : ''}  
    

        mat = np.array([list[0:3], list[3:6], list[6:9]])
        mat_min = mat.min()
        mat_max = mat.max()
        mat_sum = mat.sum()
        mat_mean = mat.mean()
        mat_var = mat.var()
        mat_std = mat.std()
    
        mat_minr = mat.min(0)
        mat_maxr = mat.max(0)
        mat_sumr = mat.sum(0)
        mat_meanr = mat.mean(0)
        mat_varr = mat.var(0)
        mat_stdr= mat.std(0)
    
        mat_minc = mat.min(1)
        mat_maxc = mat.max(1)
        mat_sumc = mat.sum(1)
        mat_meanc = mat.mean(1)
        mat_varc = mat.var(1)
        mat_stdc = mat.std(1)

        calculations.update({ "min": [mat_minr.tolist(), mat_minc.tolist(), mat_min]})

        calculations.update({"max": [mat_maxr.tolist(), mat_maxc.tolist(), mat_max]})

        calculations.update({"sum": [mat_sumr.tolist(), mat_sumc.tolist(), mat_sum]})

        calculations.update({"mean": [mat_meanr.tolist(), mat_meanc.tolist(), mat_mean]})

        calculations.update({"variance": [mat_varr.tolist(), mat_varc.tolist(), mat_var]})

        calculations.update({"standard deviation": [mat_stdr.tolist(), mat_stdc.tolist(), mat_std]})




    return calculations
