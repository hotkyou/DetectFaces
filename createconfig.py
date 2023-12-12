from configparser import ConfigParser

class CreateConfig:
    def createini():
        config = ConfigParser()
        config['DEFAULT'] = {
            'max_num_faces': 1,
            'refine_landmarks': True,
            'min_detection_confidence': 0.5,
            'min_tracking_confidence': 0.5
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)