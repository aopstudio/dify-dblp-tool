from collections.abc import Generator
from typing import Any

import requests

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

DBLP_PUBL_API_URL = "https://dblp.org/search/publ/api"

class DblpPublSearchTool(Tool):
    def _parse_response(self, response: dict) -> dict:
        result = {
           "hits": response.get("result", {}).get("hits", {})
        }
        return result

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        h = tool_parameters.get("h", 30)
        f = tool_parameters.get("f", 0)

        params = {
            "q": tool_parameters["q"],
            "h": h,
            "f": f,
            "format": "json"
        }
        try:
            response = requests.get(url=DBLP_PUBL_API_URL, params=params)
            response.raise_for_status()
            valuable_res = self._parse_response(response.json())
            yield self.create_json_message(valuable_res)
        except requests.exceptions.RequestException as e:
            yield self.create_text_message(
                f"An error occurred while invoking the tool: {str(e)}.")
