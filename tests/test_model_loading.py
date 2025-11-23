# -*- coding: utf-8 -*-
"""
Practice in CICD and deployment

@author: Diogo, mock project
"""

import os
import pickle

MODEL_DIR = "src/serving/model/3b1a41221fc44548aed629fa42b762e0/artifacts"

def test_model_files_exist():
    assert os.path.exists(f"{MODEL_DIR}/model")
    assert os.path.exists(f"{MODEL_DIR}/preprocessing.pkl")
    assert os.path.exists(f"{MODEL_DIR}/feature_columns.txt")

def test_model_can_load():
    with open(f"{MODEL_DIR}/model", "rb") as f:
        model = pickle.load(f)
    assert model is not None
