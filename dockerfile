FROM python:3.10-slim
ENV TOKEN='8177511854:AAGGmlbclo4XpZG8y-_uY54_gvSvMCBCSkY'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python","bot.py" ]