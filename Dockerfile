FROM python:3.8
ENV C_FORCE_ROOT 1
# Install PostgreSQL dependencies
RUN apt-get update && \
    apt-get install -y postgresql-client libpq-dev && \
    rm -rf /var/lib/apt/lists/*
# Step 1: Install any Python packages
# ----------------------------------------
ENV PYTHONUNBUFFERED 1
RUN mkdir /var/app
WORKDIR  /var/app
COPY requirements.txt /var/app/requirements.txt
RUN pip install -r requirements.txt
# Step 2: Copy Django Code
# ----------------------------------------
COPY . /var/app/
EXPOSE 8080
RUN chmod +x /var/app/runserver.sh
RUN chmod +x /var/app
CMD ["/var/app/runserver.sh"]
