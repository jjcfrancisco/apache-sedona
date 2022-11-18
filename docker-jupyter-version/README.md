# Installation

To build image:

```bash
docker build -t pyspark/apache-sedona-notebook .
```

To run container:

```bash
docker compose up

#or detached:
docker compose up -d
```


# Data sources

The data in the `sample-data` directory was downloaded from the USGS website - here's the link: https://mrdata.usgs.gov/mrds/