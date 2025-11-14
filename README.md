**Project**: Bank Transaction Fraud Detection

- **Description**: A small Streamlit app that loads a pre-trained scikit-learn model and predicts whether a bank transaction is fraudulent based on user-provided transaction fields.

**Files**:

- `app.py`: Streamlit application entrypoint.
- `Fraud_detection.csv`: (dataset file included in repo)
- `Fraud_detection.pkl`: Pickled scikit-learn model used by the app (expected in project root).
- `requirements.txt`: Python dependencies (created in the project root).

**Requirements**:

- Python 3.10+ (this project was developed and tested with Python 3.14 on Windows)
- `streamlit`
- `scikit-learn`
- `pandas`
- `joblib`

**Quick Setup**

1. (Optional) Create a virtual environment:

```bash
python -m venv .venv
# Activate on Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or on WSL / bash
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Run the app**

```bash
streamlit run app.py
```

Then open the URL Streamlit prints (usually http://localhost:8501) in your browser.

**Model / Version Notes**

- The pickled model (`Fraud_detection.pkl`) was created with scikit-learn 1.6.1. Loading it in a different scikit-learn version (e.g., 1.7.2) can produce InconsistentVersionWarning messages and — in some cases — unpickling errors.
- To mitigate this, `app.py` includes a small compatibility helper that attempts to patch a missing internal symbol before unpickling. This is a pragmatic workaround for running the app with a newer scikit-learn, but it carries risk: model behavior could differ.

Recommended, more robust options:

- Re-train and re-pickle the model using your current scikit-learn version.
- Run the app in an environment with the same scikit-learn version that was used to create the pickle (1.6.1). Note: installing older scikit-learn on Windows/Python versions may require build tools.

**Troubleshooting**

- If you see warnings about `Thread 'MainThread': missing ScriptRunContext!` or `Session state does not function when running a script without 'streamlit run'`, make sure you start the app via `streamlit run app.py` (don't execute `app.py` directly with `python`).
- If the model fails to load with an AttributeError about sklearn internals, consider rebuilding the model with your current environment or running inside an environment matching the original sklearn version.

**Development**

- To update dependencies, edit `requirements.txt` and re-run `pip install -r requirements.txt`.

**License & Attribution**

- This repository is a demo project. Add a license file if you plan to publish or share.

If you'd like, I can:

- Pin exact working versions in `requirements.txt` for your environment, or
- Add a small README section showing example inputs and expected output for the app UI.
