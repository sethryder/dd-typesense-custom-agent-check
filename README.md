# dd-typesense-custom-agent-check
A [Datadog](https://www.datadoghq.com/) custom agent check for [Typesense](https://typesense.org/).

![Example metrics](/example_metrics.png)

## Install

### Check Location

Upload the check script (`typesense.py`) to `/etc/datadog/checks.d/typesense.py`.

### Configure

Create a configuration file located at `/etc/datadog/conf.d/typesense.yaml`. Check `typesense.yaml` in the repo as an example.

## typesense_host

If you are monitoring instances hosted in Typesense Cloud (or on another host) the check adds a custom `typesense_host` tag that you can use to get the actual hostnames of the instances.
