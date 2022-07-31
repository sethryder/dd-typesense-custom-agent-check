# dd-typesense-custom-agent-check
A custom [Typesense](https://typesense.org/) agent check for [Datadog](https://www.datadoghq.com/). 

![Example metrics](/example_metrics.png)

## Install

### Check Location

Upload the check script (`typesense.py`) to `/etc/datadog/checks.d/typesense.py`.

### Configure

Create a configuration file located at `/etc/datadog/conf.d/typesense.yaml`. Check `typesense.yaml` in the repo as an example.

## typesense_host tag

If you are monitoring instances hosted in Typesense Cloud (or on another host) the check adds a custom `typesense_host` tag that you can use.
