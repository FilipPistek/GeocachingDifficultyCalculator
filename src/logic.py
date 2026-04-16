import joblib
import pandas as pd
import os

class GeocachingPredictor:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        models_dir = os.path.join(project_root, 'models')

        try:
            self.model = joblib.load(os.path.join(models_dir, 'model.pkl'))
            self.scaler = joblib.load(os.path.join(models_dir, 'scaler.pkl'))
            self.le_type = joblib.load(os.path.join(models_dir, 'le_type.pkl'))
            self.le_size = joblib.load(os.path.join(models_dir, 'le_size.pkl'))
        except FileNotFoundError:
            raise Exception(f".pkl soubory nenalezeny!")

    def predict(self, cache_type, size, terrain, lat, lon, is_drive_in, is_puzzle):
        type_e = self.le_type.transform([cache_type])[0]
        size_e = self.le_size.transform([size])[0]

        features = ['Type_E', 'Size_E', 'Terr_N', 'Lat_N', 'Lon_N', 'Is_Drive_In', 'Is_Puzzle']
        data = pd.DataFrame([[type_e, size_e, float(terrain), float(lat), float(lon), int(is_drive_in), int(is_puzzle)]], columns=features)

        data_scaled = self.scaler.transform(data)

        prediction = self.model.predict(data_scaled)
        return prediction[0]