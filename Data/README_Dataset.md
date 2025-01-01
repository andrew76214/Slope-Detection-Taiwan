# GNSS GPS Data Overview

This document provides an overview of the GNSS GPS data structure and the meanings of each field in the dataset. This dataset is typically used for monitoring surface dynamics, analyzing crustal deformation, and studying seismic activities.

## Folder Structure

Each CSV file represents data from a single observation station.

<details>
  <summary>Folder Architecture</summary>

```
./Slope-Detection-Taiwan/Data
├─EDA.ipynb
├─README_dataset.md
|
├─Kaohsiung
|   ├─g2.csv
|   ├─g3.csv
|   └─g4.csv
|
├─Nantou
|   ├─cn01.csv
|   ├─cn02.csv
|   └─cn04.csv
|
└─Taipei
    ├─h23-g1.csv
    ├─h23-g2.csv
    └─rain.csv
```
</details>

## Data Structure
The dataset consists of the following fields:

| Field Name     | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `date_time`    | Timestamp indicating the date and time of the recorded data.               |
| `E`            | East coordinate value (e.g., in meters), representing movement or position in the east-west direction. |
| `N`            | North coordinate value, representing movement or position in the north-south direction. |
| `H`            | Height value, representing elevation relative to a reference surface (e.g., mean sea level). |
| `Angle`        | Angle value, potentially representing azimuth, elevation, or other directional metrics. |
| `Axis`         | Axis information, possibly indicating the principal direction of movement or reference axis. |
| `Plate`        | Plate name, specifying the tectonic plate associated with the station (e.g., Eurasian Plate). |
| `EMove`        | Eastward movement, cumulative distance moved in the eastward direction.    |
| `NMove`        | Northward movement, cumulative distance moved in the northward direction.  |
| `HMove`        | Height movement, cumulative elevation change.                              |
| `TotalMove`    | Total movement, the combined magnitude of movement in all directions. Calculated as \( \sqrt{EMove^2 + NMove^2 + HMove^2} \). |
| `EDay`         | Daily eastward movement, the change in the east coordinate over a day.     |
| `NDay`         | Daily northward movement, the change in the north coordinate over a day.   |
| `HDay`         | Daily height movement, the change in height over a day.                   |

## Usage
This dataset can be used for:
- Monitoring ground motion over time.
- Studying tectonic plate dynamics and crustal deformation.
- Analyzing seismic activity and its effects on the Earth's surface.
- Supporting geodetic and geophysical research.

## Example Data
Below is an example of how the data might appear:

```csv
"date_time";"E";"N";"H";"Angle";"Axis";"Plate";"EMove";"NMove";"HMove";"TotalMove";"EDay";"NDay";"HDay"
2025-01-01T00:00:00;123.456;789.012;345.678;45.0;X;Eurasian;0.123;0.456;0.789;1.234;0.001;0.002;0.003
2025-01-02T00:00:00;123.457;789.014;345.680;46.0;Y;Eurasian;0.124;0.458;0.790;1.235;0.001;0.002;0.003
```

## Notes
- Ensure proper formatting and parsing of the dataset before use.
- Units of measurement (e.g., meters, degrees) should be confirmed based on the dataset's source documentation.
- Interpretations of `Angle` and `Axis` fields may vary depending on the specific application.

## Contributing
If you have suggestions or improvements for this README, feel free to submit a pull request.

---

**Author:** 瑞模德科技有限公司
**License:** MIT

