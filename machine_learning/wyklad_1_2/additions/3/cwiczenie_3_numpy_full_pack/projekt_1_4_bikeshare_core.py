
from __future__ import annotations

import numpy as np
import pandas as pd


DISTRICTS = ["Centrum", "Polnoc", "Poludnie", "Wschod", "Zachod", "Mokotow", "Praga", "Wola"]


def make_bikeshare_data(
    n_trips: int = 20000,
    n_stations: int = 40,
    n_days: int = 30,
    seed: int = 0,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Generuje syntetyczny zestaw danych:
    - trips: surowe przejazdy z GPS i metadanymi uzytkownika
    - stations: stacje z lokalizacja i pojemnoscia
    - weather: pogoda godzinowa

    Dane sa celowo "lekko brudne":
    - weather ma braki w temp_c i precip_mm
    - station_name zawiera niespojny zapis
    - coupon_code ma spacje / rozny case / NaN
    """
    rng = np.random.default_rng(seed)

    # --- stations
    district_idx = rng.integers(0, len(DISTRICTS), size=n_stations)
    districts = np.array(DISTRICTS, dtype=object)[district_idx]

    # Sztuczne centrum "miasta"
    lat = 52.20 + rng.normal(0.0, 0.035, size=n_stations)
    lon = 21.00 + rng.normal(0.0, 0.055, size=n_stations)
    capacity = rng.integers(10, 45, size=n_stations)

    dirty_names = []
    for i, d in enumerate(districts):
        if i % 3 == 0:
            dirty_names.append(f"st_{i:02d} | {d.lower()}  ")
        elif i % 3 == 1:
            dirty_names.append(f" ST-{i:02d} / {d.upper()}")
        else:
            dirty_names.append(f"Station {i:02d} - {d}")

    stations = pd.DataFrame(
        {
            "station_id": np.arange(n_stations, dtype=int),
            "station_name": dirty_names,
            "district": districts,
            "lat": lat,
            "lon": lon,
            "capacity": capacity,
        }
    )

    # --- weather hourly
    hours = pd.date_range("2024-05-01", periods=n_days * 24, freq="h")
    t = np.arange(len(hours))
    daily_cycle = 8 * np.sin(2 * np.pi * (t % 24) / 24 - 0.8)
    weekly_cycle = 3 * np.sin(2 * np.pi * t / (24 * 7))
    temp_c = 16 + daily_cycle + weekly_cycle + rng.normal(0, 1.2, size=len(hours))

    precip_mm = rng.gamma(shape=1.4, scale=0.9, size=len(hours))
    precip_mm[rng.random(len(hours)) < 0.76] = 0.0

    wind_kmh = 12 + 5 * np.sin(2 * np.pi * t / 24 + 0.5) + rng.normal(0, 1.5, size=len(hours))
    wind_kmh = np.clip(wind_kmh, 1, None)

    weather = pd.DataFrame(
        {
            "timestamp_hour": hours,
            "temp_c": temp_c,
            "precip_mm": precip_mm,
            "wind_kmh": wind_kmh,
        }
    )

    # celowe braki
    mask_temp = rng.random(len(weather)) < 0.06
    mask_precip = rng.random(len(weather)) < 0.05
    weather.loc[mask_temp, "temp_c"] = np.nan
    weather.loc[mask_precip, "precip_mm"] = np.nan

    # --- trips
    hour_weights = np.array(
        [0.01,0.005,0.003,0.003,0.005,0.015,0.045,0.08,0.085,0.06,0.04,0.04,
         0.045,0.05,0.055,0.06,0.08,0.095,0.09,0.065,0.04,0.025,0.015,0.009]
    )
    hour_weights = hour_weights / hour_weights.sum()

    days = rng.integers(0, n_days, size=n_trips)
    hours_choice = rng.choice(np.arange(24), size=n_trips, p=hour_weights)
    minutes = rng.integers(0, 60, size=n_trips)
    seconds = rng.integers(0, 60, size=n_trips)
    start_ts = (
        pd.Timestamp("2024-05-01")
        + pd.to_timedelta(days, unit="D")
        + pd.to_timedelta(hours_choice, unit="h")
        + pd.to_timedelta(minutes, unit="m")
        + pd.to_timedelta(seconds, unit="s")
    )

    true_start_station_id = rng.integers(0, n_stations, size=n_trips)
    true_end_station_id = (true_start_station_id + rng.integers(1, n_stations, size=n_trips)) % n_stations

    start_lat = lat[true_start_station_id]
    start_lon = lon[true_start_station_id]
    end_lat = lat[true_end_station_id]
    end_lon = lon[true_end_station_id]

    # surowe GPS wokol stacji
    raw_start_lat = start_lat + rng.normal(0, 0.0017, size=n_trips)
    raw_start_lon = start_lon + rng.normal(0, 0.0022, size=n_trips)
    raw_end_lat = end_lat + rng.normal(0, 0.0017, size=n_trips)
    raw_end_lon = end_lon + rng.normal(0, 0.0022, size=n_trips)

    # dystans w km (przyblizony)
    dx_km = (end_lon - start_lon) * 67.0
    dy_km = (end_lat - start_lat) * 111.0
    distance_km = np.sqrt(dx_km**2 + dy_km**2)

    user_type = rng.choice(["member", "casual"], size=n_trips, p=[0.68, 0.32])

    # pogoda dla godziny startu
    weather_idx = days * 24 + hours_choice
    temp_for_trip = np.take(np.nan_to_num(temp_c, nan=np.nanmean(temp_c)), weather_idx)
    rain_for_trip = np.take(np.nan_to_num(precip_mm, nan=0.0), weather_idx)

    speed_kmh = np.where(user_type == "member", 16.5, 13.5)
    speed_kmh = speed_kmh - 0.20 * np.clip(rain_for_trip, 0, 10) + 0.04 * np.clip(temp_for_trip - 12, -10, 10)
    speed_kmh = np.clip(speed_kmh, 9.5, 22.0)

    duration_min = 3.0 + 60 * distance_km / speed_kmh + rng.gamma(2.0, 1.3, size=n_trips)
    duration_min = np.clip(duration_min, 2.0, 120.0)

    end_ts = start_ts + pd.to_timedelta(duration_min, unit="m")
    bike_id = rng.integers(0, max(120, n_stations * 3), size=n_trips)

    coupon_pool = np.array(["SUMMER10 ", " bike5", "WELCOME ", np.nan, "vip ", "NONE"], dtype=object)
    coupon_code = rng.choice(coupon_pool, size=n_trips, p=[0.18, 0.11, 0.08, 0.52, 0.04, 0.07])

    trips = pd.DataFrame(
        {
            "trip_id": np.arange(n_trips, dtype=int),
            "bike_id": bike_id,
            "start_ts": pd.to_datetime(start_ts),
            "end_ts": pd.to_datetime(end_ts),
            "raw_start_lat": raw_start_lat,
            "raw_start_lon": raw_start_lon,
            "raw_end_lat": raw_end_lat,
            "raw_end_lon": raw_end_lon,
            "user_type": user_type,
            "coupon_code": coupon_code,
            "duration_min_true": duration_min,
            "distance_km_true": distance_km,
            "true_start_station_id": true_start_station_id,
            "true_end_station_id": true_end_station_id,
        }
    )

    return trips, stations, weather


def assign_nearest_station_loop(
    raw_lat: np.ndarray,
    raw_lon: np.ndarray,
    station_lat: np.ndarray,
    station_lon: np.ndarray,
) -> np.ndarray:
    """Wolna wersja O(n_points * n_stations) z podwojna petla w Pythonie."""
    out = np.empty(len(raw_lat), dtype=int)
    for i in range(len(raw_lat)):
        best_j = -1
        best_d = float("inf")
        for j in range(len(station_lat)):
            d = (raw_lat[i] - station_lat[j]) ** 2 + (raw_lon[i] - station_lon[j]) ** 2
            if d < best_d:
                best_d = d
                best_j = j
        out[i] = best_j
    return out


def revenue_loop(duration_min: np.ndarray, user_type: np.ndarray) -> np.ndarray:
    """Wolna wersja liczenia przychodu w petli."""
    out = np.empty(len(duration_min), dtype=float)
    for i in range(len(duration_min)):
        base = 2.5 if user_type[i] == "casual" else 1.0
        per_min = 0.23 if user_type[i] == "casual" else 0.12
        out[i] = base + per_min * max(duration_min[i] - 5.0, 0.0)
    return out


def daily_trip_counts_loop(start_ts: pd.Series) -> pd.Series:
    """Wolna wersja zliczania przejazdow per dzien."""
    counts: dict[pd.Timestamp, int] = {}
    for ts in pd.to_datetime(start_ts):
        day = pd.Timestamp(ts).normalize()
        counts[day] = counts.get(day, 0) + 1
    s = pd.Series(counts, dtype=int)
    return s.sort_index()


def normalize_hour(ts: pd.Series) -> pd.Series:
    return pd.to_datetime(ts).dt.floor("h")


def time_one(fn, *args, repeat: int = 3, **kwargs) -> float:
    import time

    best = float("inf")
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn(*args, **kwargs)
        best = min(best, time.perf_counter() - t0)
    return best
