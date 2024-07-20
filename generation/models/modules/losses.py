import torch
from utils.core import imresize

class ConsistencyLoss(torch.nn.Module):
    def __init__(self, scale=0.5, criterion=torch.nn.MSELoss()):
        super(ConsistencyLoss, self).__init__()
        self.scale = scale
        self.criterion = criterion

    def forward(self, inputs, targets):
        targets = imresize(targets, scale=self.scale)
        inputs = imresize(inputs, scale=self.scale)

        loss = self.criterion(inputs, targets.detach())

        return loss
    
class TotalVariationLoss(torch.nn.Module):
    def __init__(self, tv_weight):
        super(TotalVariationLoss, self).__init__()
        self.tv_weight = tv_weight

    def forward(self, img):
        """ Compute total variation loss.

        Inputs:
        - img: PyTorch Variable of shape (1, 3, H, W) holding an input image.
        - tv_weight: Scalar giving the weight w_t to use for the TV loss.

        Returns:
        - loss: PyTorch Variable holding the total variation loss.
        """
        tv_h = ((img[:, :, 1:, :] - img[:, :, :-1, :]) ** 2).sum()
        tv_w = ((img[:, :, :, 1:] - img[:, :, :, :-1]) ** 2).sum()
        loss = self.tv_weight * (tv_h + tv_w)
        return loss
