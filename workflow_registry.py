class WorkflowRegistry:
    def publish(self, name: str, version: str, env_config: dict) -> None:
        """
        Registers a new workflow version.
        Rules:
        - If this is the first version for `name`, accept it.
        - Otherwise, `version` must be strictly greater than the latest version
          for this workflow. If not, raise a ValueError.
        """

    def get_latest(self, name: str) -> dict | None:
        """
        Returns the env_config of the latest version for this workflow name,
        or None if it does not exist.
        """
          
        return None 

    def diff_env(self, name: str, from_version: str, to_version: str) -> dict:
        """
        Compares the env_config of two versions of the same workflow.
        Returns a dict with the structure:

        {
          "added":   [list of keys present only in to_version],
          "removed": [list of keys present only in from_version],
          "changed": {
            key: {"from": old_value, "to": new_value},
            ...
          }
        }

        If either version does not exist, raise a ValueError.
        """

    def print_header():
      print ("Hai! This is an example usage of the Workflow Registry.\n")