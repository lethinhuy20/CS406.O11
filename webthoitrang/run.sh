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


# Check for existence of extracted folders and zip files
if [[ -d media/train ]] && [[ -f media/train_set.zip ]]; then
  echo "train_set.zip already extracted to media/train"
elif [[ -f media/train_set.zip ]]; then
  unzip -q media/train_set.zip -d media  # Unzip to media/
fi

if [[ -d media/test ]] && [[ -f media/test_set.zip ]]; then
  echo "test_set.zip already extracted to media/test"
elif [[ -f media/test_set.zip ]]; then
  unzip -q media/test_set.zip -d media  # Unzip to media/
fi

# Run Django commands
if [[ "$1" == "reset-db" ]]; then
  python prep_db.py
  python manage.py makemigrations
  sh reset_db.sh
fi 

python manage.py runserver --noreload