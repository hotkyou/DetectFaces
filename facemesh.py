import mediapipe as mp
import configparser

class FaceMesh:
    def __init__(self, image):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.settings = dict(config["DEFAULT"])
        self.image = image
        self.facemeshInit()
    
    def facemeshInit(self):
        mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = mp_face_mesh.FaceMesh(
            max_num_faces=int(self.settings.get("max_num_faces", 1)),
            refine_landmarks=bool(self.settings.get("refine_landmarks", False)),
            min_detection_confidence=float(self.settings.get("min_detection_confidence", 0.5)),
            min_tracking_confidence=float(self.settings.get("min_tracking_confidence", 0.5))
        )

    @property
    def execute(self):
        # 画像を処理して顔の部位の値を取得
        results = self.face_mesh.process(self.image)
        landmark = results.multi_face_landmarks
        landmarks_dict = {}

        # 結果の処理
        if landmark:
            #冗長化のために複数顔を検出できるようにする##############
            if len(landmark) == 1:
                # landmarksは複数の顔の場合があるため、各顔の結果を取得
                for idx, point in enumerate(landmark[0].landmark):
                    landmarks_dict[idx] = {"x": point.x, "y": point.y, "z": point.z}
            else:
                landmarks_dict = {"error": "many detected"}
        else:
            landmarks_dict = None
            
        return landmarks_dict
