from __future__ import annotations
import numpy as np

def confidence_attack(target_prob: float, member_probs: np.ndarray, nonmember_probs: np.ndarray) -> dict:
    members=np.asarray(member_probs,dtype=float); non=np.asarray(nonmember_probs,dtype=float)
    if members.size==0 or non.size==0: raise ValueError('datasets must be non-empty')
    threshold=float(target_prob)
    member_tpr=float(np.mean(members >= threshold)); nonmember_fpr=float(np.mean(non >= threshold))
    return {'threshold':threshold,'member_tpr':member_tpr,'nonmember_fpr':nonmember_fpr,'advantage':member_tpr-nonmember_fpr}

def entropy(probabilities: np.ndarray)->np.ndarray:
    p=np.clip(np.asarray(probabilities,dtype=float),1e-12,1.0); return -np.sum(p*np.log2(p),axis=-1)
