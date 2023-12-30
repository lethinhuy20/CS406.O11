#!/bin/bash

# Navigate to the directory
cd webthoitrang/

# Create virtual environment and activate it
python -m venv venv
source venv/Scripts/activate

# Install requirements
pip install -r requirements.txt

# Check for fclip file and download if missing
if [[ ! -f app/faiss_retrieval/indexes/fclip_B32* ]]; then
  gdown 1Xfr6oqZHQrpFOhEqLkt1fuIbSAuxsKgq  # Download .bin
  mv fclip_B32* app/faiss_retrieval/indexes
fi

# Check for zip files and download if missing
if [[ ! -f media/train_set.zip || ! -f media/test_set.zip ]]; then
  gdown 1y5xndjRW3iVxL254jYPd6Vm86KuJQ75S
  gdown 1fix1hdVz3cAKv9vXjS1iJl6b6k1f-gjq
  mv *.zip media/
fi

# Unzip zip files (only if they were downloaded)
if [[ -f media/train_set.zip ]]; then
  unzip -q media/train_set.zip
fi
if [[ -f media/test_set.zip ]]; then
  unzip -q media/test_set.zip
fi

# Run Django commands
if [[ "$1" == "reset-db" ]]; then
  python prep_db.py
  python manage.py makemigrations
  sh reset_db.sh
else
    python manage.py runserver --noreload
fi 