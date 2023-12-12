from .resources.JP.enum import JP_kana, JP_line, JP_kana_list
from .facemesh import FaceMesh

class DetectMouth:
    def __init__(self, image, assign):
        self.image = image
        self.landmarks_dict = FaceMesh(self.image).execute
        self.assign = assign
        self.leftmouth = self.landmarks_dict[61]
        self.rightmouth = self.landmarks_dict[291]
        self.uppermouth = self.landmarks_dict[13]
        self.lowermouth = self.landmarks_dict[14]
        print(self.leftmouth, self.rightmouth, self.uppermouth, self.lowermouth)
    
    @property
    def execute(self):
        result = JP_kana[self.assign]
        if result.value is None:
            mouthHorizontal = self.leftmouth["x"] - self.rightmouth["x"]
            mouthVertical = self.uppermouth["y"] - self.lowermouth["y"]
            HVdifference = abs(mouthHorizontal - mouthVertical)
            print(HVdifference)
            #if HVdifference <= 0.01:
                
            #if abs(mouthHorizontal - mouthVertical) 
            
        return str(result.value)