FROM python:3.10
WORKDIR /app
COPY . /app/
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir .
EXPOSE 5000
CMD python app.py