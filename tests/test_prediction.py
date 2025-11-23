# -*- coding: utf-8 -*-
"""
Practice in CICD and deployment

@author: Diogo, mock project, test prediction
"""

import pickle
import numpy as np

MODEL_DIR = "src/serving/model/3b1a41221fc44548aed629fa42b762e0/artifacts"

def test_model_predicts():
    with open(f"{MODEL_DIR}/model", "rb") as f:
        model = pickle.load(f)

    # Dummy input (shape must match training pipeline)
    sample_input = np.random.rand(1, model.n_features_in_)

    pred = model.predict(sample_input)

    assert pred is not None