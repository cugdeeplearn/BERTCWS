import numpy as np
 
y_true = np.array([0, 1, 1, 0, 1, 0])
y_pred = np.array([1, 1, 1, 0, 0, 1])
 
#true positive
TP = np.sum(np.logical_and(np.equal(y_true,1),np.equal(y_pred,1)))
print(TP)
 
#false positive
FP = np.sum(np.logical_and(np.equal(y_true,0),np.equal(y_pred,1)))
print(FP)
 
#true negative
TN = np.sum(np.logical_and(np.equal(y_true,1),np.equal(y_pred,0)))
print(TN)
 
#false negative
FN = np.sum(np.logical_and(np.equal(y_true,0),np.equal(y_pred,0)))
print(FN)