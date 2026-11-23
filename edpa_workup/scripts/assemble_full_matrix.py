from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent / "edpa_workup"
base = pd.read_csv(ROOT / "master_feature_matrix.csv")
sources = [
    ("segment0", "segment0_feature_matrix.csv"),
    ("segment1", "segment1_feature_matrix.csv"),
    ("spurs", "spurs_feature_matrix.csv"),
]
out = base.copy()
for prefix, filename in sources:
    src = pd.read_csv(ROOT / filename)
    if src.feature_id.duplicated().any():
        raise ValueError(f"Duplicate feature IDs in {filename}")
    cols = [c for c in src.columns if c != "feature_id"]
    rename = {c: f"{prefix}_{c}" for c in cols}
    out = out.merge(src.rename(columns=rename), left_on="feature_id", right_on="feature_id", how="left", validate="one_to_one")

expected = set(base.feature_id)
if len(base) != 52 or set(out.feature_id) != expected or out.feature_id.duplicated().any():
    raise ValueError("Feature matrix row integrity check failed")
out.to_csv(ROOT / "full_feature_matrix.csv", index=False)
print(f"Wrote 52 feature rows with base screen plus route-specific detailed ledgers to {ROOT / 'full_feature_matrix.csv'}")
