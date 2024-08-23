# This file will handle the checks prior to the model running

import torch


def gpu_available():

    if not torch.cuda.is_available():
        print("No valid GPU. Have your updated drivers this boot?")
        return False
    else:
        return
