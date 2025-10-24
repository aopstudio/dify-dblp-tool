# DBLP Search Plugin

## Overview

The DBLP Search Plugin allows you to query structured bibliographic data from [DBLP](https://dblp.org/) in real time. It supports searching for:

* **Publications** – individual papers, journal articles, and conference papers.
* **Authors** – search for researchers and editors, including disambiguation.
* **Venues** – search for publication sources, including journals and conference series.

The plugin returns structured results including titles, authors, venues, years, and URLs.

---

## Configuration

### 1. No API Key Required

DBLP provides open access to its search API, so no API key is required to use this plugin.

### 2. Install from Plugin Marketplace

The DBLP Search Plugin can be installed from the Plugin Marketplace. Ensure you have the plugin installed before using it.

### 3. Use the Plugin

You can use the DBLP plugin in the following application types:

#### Chatflow / Workflow Applications

Add a **DBLP tool node** to your Chatflow or Workflow, then configure the following parameters:

| Parameter | Type   | Description                         | Default  |
| --------- | ------ | ----------------------------------- | -------- |
| `q`       | string | Search query string                 | required |
| `h`       | number | Maximum number of results to return | 30       |
| `f`       | number | Start index for paginated results   | 0        |

You can choose the tool type: `publication`, `author`, or `venue`.

#### Agent Applications

Add the DBLP plugin to your Agent application. Then provide instructions such as:

* “Search for publications about `Transformers in NLP`”
* “Find authors with the name `Geoffrey Hinton`”
* “List venues related to `SIGMOD`”

The plugin will return structured search results with metadata, ready for further processing.

---

## Example Usage

```json
{
  "tool": "dblp_publ_search",
  "q": "Neural Networks",
  "h": 5,
  "f": 0
}
```

Returns the top 5 publications matching “Neural Networks”.

```json
{
  "tool": "dblp_author_search",
  "q": "Yann LeCun"
}
```

Returns authors matching “Yann LeCun”.

```json
{
  "tool": "dblp_venue_search",
  "q": "NeurIPS",
  "h": 10
}
```

Returns top 10 venues matching “NeurIPS”.

---

## Notes

* DBLP data is open and publicly accessible under CC0 license.
* Pagination is supported via the `f` parameter.
