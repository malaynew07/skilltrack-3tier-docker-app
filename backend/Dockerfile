    # ---------- STAGE 1 : builder ----------
FROM python:3.11 AS builder

    #creating Working dir.
WORKDIR /app

    #copying all code and requirment files
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . .

   
# ---------- STAGE 2 : runtime ----------
FROM python:3.11-slim

  #creating working dir.
WORKDIR /app

  #copying all redpendancy
COPY --from=builder /install /usr/local

  #App code copy
COPY . .
   #exposing port
EXPOSE 5000

   #exicuting commands
CMD ["python", "app.py"]
