# Используем официальный образ Python 3.12
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    wget \
    unzip \
    ca-certificates \
    # Для cloudscraper с браузерным режимом
    chromium \
    chromium-driver \
    chromium-common \
    # Для сборки Python-пакетов
    gcc \
    python3-dev \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    # Node.js (может потребоваться для некоторых cloudscraper-режимов)
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g puppeteer \
    # Очистка кэша
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VERSION="1.8.3"
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

COPY src/ ./src/
COPY last_event_id.txt ./

# Устанавливаем переменные окружения для Chromium (чтобы работать в headless-режиме)
ENV PYTHONPATH="/app/src"
ENV CHROMIUM_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
ENV DISPLAY=:99
ENV NO_SANDBOX=1
ENV CHROMIUM_FLAGS="--no-sandbox --disable-setuid-sandbox --disable-dev-shm-usage --disable-gpu --disable-software-rasterizer"

CMD ["python", "-m", "src.details.main.main"]
