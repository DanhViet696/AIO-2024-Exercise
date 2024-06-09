def Calculate(TP,FP,FN):
    #Check TP,FP,FN is of type int or not
    if not isinstance(TP, int):
        print('TP must be int')
        return
    if not isinstance(FP, int):
        print('FP must be int')
        return
    if not isinstance(FN, int):
        print('FN must be int')
        return
    #Check TP,FP,FN greater than Zero or not
    if TP <= 0 or FP <= 0 or FN <= 0:
        print('TP and FP and FN must be greater than zero')
        return
    #Calculate Precision and Recall
    Precision= TP/(TP+FP)
    print(Precision)
    Recall= TP/(TP+FN)
    print(Recall)
    # Calculate F1_score
    F1_score= 2*(Precision*Recall)/(Precision+Recall)
    print(F1_score)
Calculate(4,5,6)