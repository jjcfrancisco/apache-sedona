FROM jupyter/base-notebook

LABEL Frank Jimenez <jjcfrank@gmail.com>

# Sets root user for the building process
USER root

# Installs Java, GDAL and other dependencies
RUN apt-get update \
    && apt-get install -y \
    openjdk-8-jre \
    ca-certificates-java \
    libgdal-dev \
    ant \
    wget \
    tar \
    bash \
    nmap \
    vim \
    && apt-get clean \
    && update-ca-certificates -f

# Downloads Spark
RUN mkdir -p /opt/spark/
RUN wget https://archive.apache.org/dist/spark/spark-3.0.3/spark-3.0.3-bin-hadoop3.2.tgz
RUN tar -xvzf spark-3.0.3-bin-hadoop3.2.tgz && \
    mv spark-3.0.3-bin-hadoop3.2/* /opt/spark/ && \
    rm -r spark-3.0.3-bin-hadoop3.2.tgz && \
    rm -r spark-3.0.3-bin-hadoop3.2/

# Downloads Postgres jars
RUN mkdir -p /opt/spark/extra_jars/
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.25.jre6.jar && mv postgresql-42.2.25.jre6.jar /opt/spark/extra_jars/

# Set PATHs
ENV SPARK_HOME /opt/spark
ENV PATH $PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
RUN export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"
ENV JAVA HOME="/usr/lib/jvm/java-8-openjdk-amd64"
RUN export PATH=$PATH:$SPARKHOME/bin
RUN export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
RUN export PYSPARK_PYTHON=python3
RUN export PATH=$PATH:$JAVA_HOME/bin

# Adds custom log4j.properties for Spark
COPY log4j.properties /opt/spark/conf/

# Install Python libraries via Conda
COPY environment.yml .
RUN conda env update --name base --file environment.yml --prune

# Sets non-root user by default
USER $NB_UID

#Sets Jupyter Lab instead of using the default Jupyter Notebook commands
ENV JUPYTER_ENABLE_LAB=yes







    







