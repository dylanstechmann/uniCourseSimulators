FROM python:3.12-slim AS content-validation
COPY content/ /content/
COPY tools/validate_content.py /validation/validate_content.py
RUN pip install --no-cache-dir 'jsonschema>=4.23,<5' && python /validation/validate_content.py --root /

FROM python:3.12-slim AS runtime
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 CONTENT_ROOT=/content
WORKDIR /app
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./
COPY --from=content-validation /content/ /content/
RUN useradd --create-home --uid 10001 courselab && chown -R courselab:courselab /app
USER courselab
EXPOSE 8000
CMD ["uvicorn", "courselab.main:app", "--host", "0.0.0.0", "--port", "8000"]
