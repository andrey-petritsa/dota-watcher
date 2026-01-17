FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    chromium-common \
    # Для сборки некоторых Python пакетов
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry и сразу добавляем в PATH
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION="1.8.3"
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN /opt/poetry/bin/poetry config virtualenvs.create false \
    && /opt/poetry/bin/poetry install --no-interaction --no-ansi --no-root

RUN /opt/poetry/bin/poetry run playwright install chromium

COPY src/ ./src/
COPY last_event_id.txt ./

ENV PYTHONPATH="/app/src"
ENV NO_SANDBOX=1
ENV CHROMIUM_FLAGS="--no-sandbox --disable-dev-shm-usage"

CMD ["python", "-m", "src.details.main.main"]
