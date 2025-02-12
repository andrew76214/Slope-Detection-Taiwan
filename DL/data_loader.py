import pandas as pd
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import DataLoader as TorchDataLoader, TensorDataset

class DataLoader:
    def __init__(self, data_paths):
        self.data_paths = data_paths
        self.data = self.load_data()
        self.features = None
        self.X_train = None
        self.X_test = None
        self.y_train_totalmove = None
        self.y_test_totalmove = None
        self.y_train_E = None
        self.y_test_E = None
        self.y_train_N = None
        self.y_test_N = None
        self.y_train_H = None
        self.y_test_H = None

    def load_data(self):
        data_frames = [pd.read_csv(path, delimiter=';') for path in self.data_paths]
        data = pd.concat(data_frames, ignore_index=True)
        return data

    def preprocess_data(self):
        data = self.data
        if 'date_time' in data.columns:
            data['date_time'] = pd.to_datetime(data['date_time'])
        else:
            raise KeyError("'date_time' column is missing from the DataFrame")

        data['hour'] = data['date_time'].dt.hour
        data['minute'] = data['date_time'].dt.minute

        lag_features = ["TotalMove", "E", "N", "H"]
        for feature in lag_features:
            data[f"{feature}_lag1"] = data[feature].shift(1)
            data[f"{feature}_lag2"] = data[feature].shift(2)

        data.dropna(inplace=True)

        self.features = ["hour", "minute"] + [f"{feature}_lag1" for feature in lag_features] + [f"{feature}_lag2" for feature in lag_features]
        X = data[self.features]
        y_totalmove = data["TotalMove"]
        y_E = data["E"]
        y_N = data["N"]
        y_H = data["H"]

        self.X_train, self.X_test, self.y_train_totalmove, self.y_test_totalmove = train_test_split(X, y_totalmove, test_size=0.2, random_state=42)
        self.X_train, self.X_test, self.y_train_E, self.y_test_E = train_test_split(X, y_E, test_size=0.2, random_state=42)
        self.X_train, self.X_test, self.y_train_N, self.y_test_N = train_test_split(X, y_N, test_size=0.2, random_state=42)
        self.X_train, self.X_test, self.y_train_H, self.y_test_H = train_test_split(X, y_H, test_size=0.2, random_state=42)

        # Convert data to PyTorch tensors
        X_train_tensor = torch.tensor(self.X_train.values, dtype=torch.float32)
        X_test_tensor = torch.tensor(self.X_test.values, dtype=torch.float32)
        y_train_totalmove_tensor = torch.tensor(self.y_train_totalmove.values, dtype=torch.float32)
        y_test_totalmove_tensor = torch.tensor(self.y_test_totalmove.values, dtype=torch.float32)

        # Create DataLoader
        train_dataset = TensorDataset(X_train_tensor, y_train_totalmove_tensor)
        test_dataset = TensorDataset(X_test_tensor, y_test_totalmove_tensor)
        self.train_loader = TorchDataLoader(train_dataset, batch_size=32, shuffle=True)
        self.test_loader = TorchDataLoader(test_dataset, batch_size=32, shuffle=False)