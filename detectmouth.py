import pickle
import lightgbm
import numpy as np
from .resources.JP.enum import *
from .facemesh import FaceMesh

class DetectMouth:
    def __init__(self, image):
        self.filename = 'DetectFaces/trustycat.pkl'
        self.image = image
        self.landmarks_dict = FaceMesh(self.image).execute
        self.leftmouth = self.landmarks_dict[61]
        self.rightmouth = self.landmarks_dict[291]
        self.uppermouth = self.landmarks_dict[13]
        self.lowermouth = self.landmarks_dict[14]
        self.landmarks = [0,11,12,13,14,15,16,17,37,38,39,40,41,42,61,62,72,73,74,76,77,78,80,81,82,84,
                85,86,87,88,89,90,91,95,96,146,178,179,180,181,183,184,185,191,267,268,269,270,
                271,272,291,292,302,303,304,306,307,308,310,311,312,314,315,316,317,318,319,320,
                321,324,325,375,402,403,404,405,407,408,409,415]
        self.mouth = []
        for i in self.landmarks:
            self.mouth.extend([self.landmarks_dict[i]["x"], self.landmarks_dict[i]["y"], self.landmarks_dict[i]["z"]])
        self.mouth = np.reshape(self.mouth, (1, -1))
    
    @property
    def execute(self):
        
        with open(self.filename, 'rb') as model_file:
            model = pickle.load(model_file)
            
        result = model.predict_proba(self.mouth)
        mouthresult = model.predict(self.mouth)
        resulta = np.array(result[0])
        result = resulta * 100

        for i, percentage in enumerate(result):
            print("Class {}: {:.2f}%".format(i, percentage))
        
        if mouthresult == 0:
            result = JP_kana["A"]
        elif mouthresult == 1:
            result = JP_kana["I"]
        elif mouthresult == 2:
            result = JP_kana["U"]
        elif mouthresult == 3:
            result = JP_kana["E"]
        elif mouthresult == 4:
            result = JP_kana["O"]
        else: 
            result = None
            
        return str(result.value)